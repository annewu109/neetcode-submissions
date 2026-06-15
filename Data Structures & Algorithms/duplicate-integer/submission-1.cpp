class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> dupeSet;
        for (int num: nums) {
            if (dupeSet.count(num) == 1) {
                return true;
            }
            dupeSet.insert(num);
        }
        return false;
    }
};