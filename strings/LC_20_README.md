LC 20 - Valid Parentheses

Problem: Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

Approach:
- Use a stack to keep expected closing brackets.
- For each opening bracket push its corresponding closing bracket; for a closing bracket, check the top of stack.

Time complexity: O(n)
Space complexity: O(n) (stack)
