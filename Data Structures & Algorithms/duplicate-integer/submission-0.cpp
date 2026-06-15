class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int, bool> dupeMap;
        for (int num: nums) {
            if (dupeMap.find(num) != dupeMap.end()) {
                return true;
            }
            dupeMap[num] = true;
        }
        return false;
    }
};