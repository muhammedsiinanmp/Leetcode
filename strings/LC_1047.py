class Solution:
    def removeDuplicates(self, s: str) -> str:
        """Remove all adjacent duplicate characters from s until no more remain.
        Uses a stack (list) to build the result in O(n) time and O(n) space.
        """
        stack = []
        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)
