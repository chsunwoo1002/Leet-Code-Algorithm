// 2. Two Sum
// https://leetcode.com/problems/two-sum/

#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> hmap;
        for(int i = 0; i < nums.size(); i++){
            hmap.insert({ nums[i], i});
        }
        for(int i = 0; i < nums.size(); i++){
            if(hmap.count(target-nums[i]) > 0 && hmap.at(target-nums[i]) != i)
                return vector<int> { i, hmap.at(target-nums[i])};
        }
        return vector<int>{};
    }
};
