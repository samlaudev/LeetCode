class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        
        // 检查nums元素个数是否小于3 
        if(nums.size() < 3) {
            return result;
        }
        // 排序
        sort(nums.begin(), nums.end());
        // 循环左右逼近，注意跳过重复元素
        auto last = nums.end();
        auto first = nums.begin();
        for(auto start = first; start < last - 2; start++) {
            // 夹在start与end之间的哨兵
            auto sentry = start + 1; 
            // 跳过重复元素
            if (start > first && *start == *(start - 1))
                continue;
            auto end = last - 1;        
        
            while(sentry < end) {
                int target = *start + *sentry + *end;
                
                if (target < 0) {
                    sentry++;
                    // 如果当前元素与上个元素相等，跳过
                    while(*sentry == *(sentry -1) && sentry < end) 
                        sentry++;
                }else if (target > 0) {
                    end--;
                    // 如果当前元素与上个元素相等，跳过
                    while(*end == *(end + 1) && sentry < end)
                        end--;
                }else {
                    result.push_back({*start, *sentry, *end});
                    sentry++;
                    end--;
                    while (*sentry == *(sentry -1) && *end == *(end + 1) && sentry < end)
                        sentry++;
                }
            }
        }
        
        return result;
    }
};