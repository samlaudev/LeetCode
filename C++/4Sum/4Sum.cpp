class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        // 初始化数据结构
        vector<vector<int>> result;
        unordered_multimap<int, pair<int, int>> hashMap;
        
        // 检查nums长度小于4
        if (nums.size() < 4) {
            return result;
        }
        // 排序
        sort(nums.begin(), nums.end());
        // 使用哈希表存储两个数的和
        for (int i = 0; i < nums.size() - 1; i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                hashMap.insert(make_pair(nums[i] + nums[j], make_pair(i, j)));
            }
        }
        // 遍历哈希表查找两个数的和与target之差的值
        for(auto i = hashMap.begin(); i != hashMap.end(); i++) {
            auto searchNum = target - i->first;
            auto range = hashMap.equal_range(searchNum);
            
            for(auto j = range.first; j != range.second; j++) {
                int indexA = i->second.first;
                int indexB = i->second.second;
                int indexC = j->second.first;
                int indexD = j->second.second;
                
                // 判断四个下标是否不同
                if(indexA != indexC && indexA != indexD && indexB != indexC && indexB != indexD) {
                    vector<int> vec = {nums[indexA], nums[indexB], nums[indexC], nums[indexD]};
                    sort(vec.begin(), vec.end());
                    result.push_back(vec);
                }
            }
        }
        // 移除重复数组
        sort(result.begin(), result.end());
        result.erase(unique(result.begin(), result.end()), result.end());
        
        return result;
    }
};