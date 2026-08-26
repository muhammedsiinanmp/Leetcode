LC-66: Plus One

Approach:
- Iterate digits from the least significant end, adding carry (initially 1).
- Update the digit with s % 10 and compute carry = s // 10.
- If carry remains after processing all digits, prepend it to the list.

Time complexity: O(n)
Space complexity: O(1) extra (result may be longer by 1 digit)
