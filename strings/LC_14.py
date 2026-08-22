class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        """Return the longest common prefix string amongst an array of strings.

        Approach: horizontal scanning — take first string as prefix and iteratively
        shorten it while it is not a prefix of subsequent strings. This results in
        O(S) time where S is the sum of all characters in the array.
        """
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            # reduce prefix length until s startswith prefix
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
