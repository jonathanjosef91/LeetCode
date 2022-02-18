class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        NUM_OF_CHARS = 256
        hist = [0] * NUM_OF_CHARS
        l = 0
        r = 0
        max = 0

        while r < len(s):
            hist_i = ord(s[r])
            hist[hist_i] += 1
            while hist[hist_i] > 1:
                hist[ord(s[l])] -= 1
                l += 1
            if r - l + 1 > max:
                max = r - l + 1
            r += 1

        return max