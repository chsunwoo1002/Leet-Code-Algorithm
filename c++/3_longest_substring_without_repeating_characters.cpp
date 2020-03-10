// 3. Longest Substring Without Repeating Characters
// https://leetcode.com/problems/longest-substring-without-repeating-characters/
#include <unordered_set>

class Solution {
public:
    int maxInt(int a, int b) {
        if(a > b)
            return a;
        else
            return b;
    }
    int lengthOfLongestSubstring(string s) {
        int left = 0;
        int right = 0;
        int max = 0;
        std::unordered_set<char> set;
        while(right < s.length()) {
            std::unordered_set<char>::const_iterator got = set.find (s.at(right));
            if(got == set.end()) {
                set.insert(s.at(right));
                right++;
                max = maxInt(max, set.size());
            }
            else {
               set.erase(s.at(left));
                left++;
            }
        }
        return max;
    }
};
