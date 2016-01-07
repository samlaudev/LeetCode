class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        auto total = nums1.size() + nums2.size();
        // 判断元素总数是否为偶数
        if (total % 2 == 0) {
            // 如果是偶数，找出中间两个数相加，然后除以2.0
            return (find_kth(nums1, nums2, total / 2) + find_kth(nums1, nums2, total / 2 + 1)) / 2.0;
        } else {
            // 如果是奇数，找出中间数即可
            return find_kth(nums1, nums2, total / 2 + 1);
        } 
    }

private:
    int find_kth(vector<int>& nums1, vector<int>& nums2, int k) {
        
        // 总是假设nums1的元素长度小于nums2
        if (nums1.size() > nums2.size())  return find_kth(nums2, nums1, k);
        // 递归退出条件
        if (nums1.size() == 0)  return nums2[k-1];
        if (k == 1) return min(nums1[0], nums2[0]);
        
        // 分为两部分，递归解决
        int index1 = min(k / 2, (int)nums1.size());
        int index2 = k - index1;
        
        if (nums1[index1 - 1] < nums2[index2 - 1]) {
            vector<int> vec(nums1.begin() + index1, nums1.end());
            return find_kth(vec, nums2, index2);
        }else if (nums1[index1 - 1] > nums2[index2 - 1]) {
            vector<int> vec(nums2.begin() + index2, nums2.end());
            return find_kth(nums1, vec, index1);
        }else {
            return nums1[index1 - 1];
        }
    }
};