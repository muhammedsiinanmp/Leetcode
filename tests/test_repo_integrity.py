"""
Repository-wide integrity checks.

Two guards:
  1. Every .py file in the repository must compile. A single file with a
     syntax error is enough to break any tool that imports or walks the
     tree, which is how the LC-1365 / Merge Sorted Array / Number of Good
     Pairs / FizzBuzz breakages went unnoticed.
  2. Every tests/test_*.py script must run successfully.

Run directly (python3 tests/test_repo_integrity.py) or under pytest.
"""
import os
import subprocess
import sys

repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, repo_root)

SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".venv", "venv"}

# This module runs every test script as a subprocess, so it must not run
# itself or it recurses forever.
SELF = os.path.basename(__file__)


def iter_python_files():
    for dirpath, dirnames, filenames in os.walk(repo_root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in sorted(filenames):
            if name.endswith(".py"):
                yield os.path.join(dirpath, name)


def test_all_files_compile():
    failures = []
    for path in iter_python_files():
        try:
            with open(path, "rb") as fh:
                compile(fh.read(), path, "exec")
        except SyntaxError as exc:
            failures.append(f"{os.path.relpath(path, repo_root)}:{exc.lineno}: {exc.msg}")
    assert not failures, "files failed to compile:\n" + "\n".join(failures)


def test_all_test_scripts_pass():
    tests_dir = os.path.join(repo_root, "tests")
    failures = []
    for name in sorted(os.listdir(tests_dir)):
        if not (name.startswith("test_") and name.endswith(".py")):
            continue
        if name == SELF:
            continue
        try:
            proc = subprocess.run(
                [sys.executable, os.path.join(tests_dir, name)],
                capture_output=True,
                text=True,
                cwd=repo_root,
                timeout=60,
            )
        except subprocess.TimeoutExpired:
            failures.append(f"{name}: timed out after 60s")
            continue
        if proc.returncode != 0:
            last = (proc.stderr.strip().splitlines() or ["<no stderr>"])[-1]
            failures.append(f"{name}: {last}")
    assert not failures, "test scripts failed:\n" + "\n".join(failures)


if __name__ == "__main__":
    test_all_files_compile()
    print("All repository files compile")
    test_all_test_scripts_pass()
    print("All test scripts pass")
