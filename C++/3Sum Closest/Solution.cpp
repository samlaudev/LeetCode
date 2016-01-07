class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        // 初始化变量
        int result = 0;
        int minGap = INT_MAX;
        // 排序
        sort(nums.begin(), nums.end());
        // 循环左右夹逼
        auto last = nums.end();
        for(auto start = nums.begin(); start < last - 2; start++) {
            auto end = last - 1;
            // 夹在start与end之间的移动哨兵
            auto sentry = start + 1;
            while (sentry < end) {
                int sum = *start + *sentry + *end;
                int gap = abs(sum - target);
                
                if (gap < minGap) {
                    result = sum;
                    minGap = gap;
                }
                // 移动sentry或end左右夹逼
                if (sum < target) {
                    sentry++;
                }else {
                    end--;
                }
            }
        }
        
        return result;
    }
};