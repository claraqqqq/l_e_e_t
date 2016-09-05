/*
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

For example, given array S = {-1 2 1 -4}, and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

*/

class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {

        sort(nums.begin(), nums.end());
        int res = 0;
        int min_diff = INT_MAX;

        for(auto idx=nums.begin(); idx<nums.end(); idx++) {

			      auto left = idx+1;
			      auto right = nums.end()-1;

			      while (left < right) {
				        const int sum = *idx + *left + *right;
				        const int diff = abs(sum - target);

				        if (diff < min_diff) {
					          min_diff = diff;
					          res = sum;
				        }

				        if (sum == target) return sum;
				        else if (sum < target) left++;
				        else right--;
			      }

		    }
		    return res;
    }
};
