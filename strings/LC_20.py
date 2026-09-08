class Solution:
    def isValid(self, s: str) -> bool:
        """Check if a string of brackets is valid.

        Use a stack: push expected closing bracket for each opening bracket and
        on encountering a closing bracket verify it matches the top of stack.
        """
        stack = []
        pairs = {'(': ')', '[': ']', '{': '}'}
        for ch in s:
            if ch in pairs:
                stack.append(pairs[ch])
            else:
                if not stack or stack.pop() != ch:
                    return False
        return not stack
