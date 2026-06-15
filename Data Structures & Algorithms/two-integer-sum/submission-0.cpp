class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> toAddIndex;
        vector<int> toReturn(2);
        for (int i = 0; i < nums.size(); i++) {
            if (toAddIndex.count(target - nums[i])) {
                toReturn[0] = toAddIndex[target - nums[i]];
                toReturn[1] = i;
                return toReturn;
            }
            toAddIndex[nums[i]] = i;
        }

        return toReturn;
    }
};
