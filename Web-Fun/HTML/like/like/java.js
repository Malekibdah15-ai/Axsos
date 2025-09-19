class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for(let i = 0; i < nums.length; i++){
            for(let j = 0; j < nums.length; j++){
                if(nums[i] + nums[j] == target);
                return [i,j];
            }
        }
    }
};