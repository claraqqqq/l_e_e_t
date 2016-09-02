//3Sum

/*
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
*/

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        
        vector<vector<int>> res;
        
        // nums not valid
        if (nums.size() < 3) return res;

		sort(nums.begin(), nums.end());
		const int target = 0;
			
		for (auto idx = nums.begin(); idx < nums.end()-2; idx++) {	
			
			if (idx == nums.begin() || *idx > *(idx-1)) {
				auto left = idx + 1;
				auto right = nums.end() - 1;
			
				while (left < right) {
			
					if (*idx + *left + *right == target) {
						res.push_back({*idx, *left, *right});
						left++;
						right--;
						while (left < right && *left == *(left-1)) left++;
						while (left < right && *right == *(right+1)) right--;
					}
					
					else if (*idx + *left + *right < target) {
						while (left < right) {
							left++;
							if (*left > *(left-1)) break;							
						}
					}
					
					else {
						while (left < right) {
							right--;
							if (*right < *(right+1)) break;	
						}
					}
				}	
			}		
		}
		return res;
    }
};
