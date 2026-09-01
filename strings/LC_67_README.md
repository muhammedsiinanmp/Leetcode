LC-67: Add Binary

Approach:
- Process both binary strings from right-to-left, adding bit-by-bit and tracking carry.
- Append computed bits to a result list and reverse at the end to build the final binary string.
- This is O(max(len(a), len(b))) time and O(max(len(a), len(b))) space for the result.
