LC-1047: Remove All Adjacent Duplicates In String

Approach:
- Use a stack (Python list) to iterate through characters.
- If the current character matches the stack top, pop the stack (removing the duplicate pair).
- Otherwise, push the current character onto the stack.
- After processing all characters, join the stack into the resulting string.

Time complexity: O(n)
Space complexity: O(n) (stack)
