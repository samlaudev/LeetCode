class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;
        map<int, int> hashTable;
        
        for(int i = 0; i < nums.size(); i++) {
            // 计算出另个需要查找的整数，并在哈希表中查找
            int searchNum = target - nums[i];
            if(hashTable.count(searchNum)) {
                result.push_back(hashTable[searchNum] + 1);
                result.push_back(i + 1);
                
                return result;
            }
            // 存放当前数及应对的下标，以便下次在哈希表中查找
            hashTable[nums[i]] = i;
        }
        
        return result;
    }
};