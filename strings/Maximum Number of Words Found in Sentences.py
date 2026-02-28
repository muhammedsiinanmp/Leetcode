"""
LeetCode 2114 - Maximum Number of Words Found in Sentences
Category: String
Difficulty: Easy

Approach:
Count spaces in each sentence (words = spaces + 1).
Track maximum.

Time Complexity: O(n * m)
Space Complexity: O(1)
"""

from typing import List

def mostWordsFound(self, sentences: List[str]) -> int:
    # Normal
    # res = []
    # for each in sentences:
    #    res.append(len(each.split(" ")))
    # return max(res)

    # Pythonic
    # return max(i.count(" ") +1 for i in sentences) 

    # DS
    max_words = 0
    for sentence in sentences:
        max_count = 1
        for word in sentence:
            if word == " ":
                max_count += 1
        max_words = max(max_words,max_count)
    return max_words

if __name__ == "__main__":
    sample = ["alice and bob love leetcode", "i think so too"]
    print(mostWordsFound(sample))