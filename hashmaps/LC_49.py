from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """Group strings that contain the same letters."""
        groups = defaultdict(list)

        for value in strs:
            groups[tuple(sorted(value))].append(value)

        return list(groups.values())
