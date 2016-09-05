// Median of Two Sorted Arrays

/*
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
*/

// vector::begin: Returns an iterator pointing to the first element in the vector.
// const_iterator: If want to iterative over a const vector, have to use a const_iterator.

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        const int m = nums1.size();
        const int n = nums2.size();

        int total_num = m + n;

        if (total_num & 0x1)
            return find_median(nums1.begin(), m, nums2.begin(), n, total_num/2+1);
        else{
            int tmp1 = find_median(nums1.begin(), m, nums2.begin(), n, total_num/2);
            int tmp2 = find_median(nums1.begin(), m, nums2.begin(), n, total_num/2+1);
            return (tmp1+tmp2) / 2.0;
        }
    }

private:
	  static int find_median(std::vector<int>::const_iterator nums1, int m, std::vector<int>::const_iterator nums2, int n, int median_th){

		if (m > n)
		    return find_median(nums2, n, nums1, m, median_th);
		if (m == 0)
		    return *(nums2 + median_th - 1);
		if (median_th == 1)
		    return min(*nums1, *nums2);

		int m1 = min(median_th/2, m);
		int n1 = median_th - m1;

		if (*(nums1+m1-1) < *(nums2+n1-1))
		    return find_median(nums1+m1, m-m1, nums2, n, median_th-m1);
		else if (*(nums1+m1-1) > *(nums2+n1-1))
		    return find_median(nums1, m, nums2+n1, n-n1, median_th-n1);
		else
		    return nums1[m1-1];
    }
};
