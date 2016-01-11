class Solution {
public:
    int maxArea(vector<int>& height) {
        int result = 0;
        // 长度检查
        if (height.size() < 2) {
            return 0;
        }
        // 左右夹逼
        int start = 0;
        int end = height.size() - 1;
        while (start < end) {
            // 计算出当前容器大小后，跟之前的容器比较，取较大那个
            result = max(result, min(height[start], height[end]) * (end - start));
            // 移动下标
            if (height[start] <= height[end]) {
                start++;
            }else {
                end--;
            }
        }
        
        return result;
    }
};