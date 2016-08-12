// Search in Rotated Sorted Array II

// Follow up for "Search in Rotated Sorted Array":
// What if duplicates are allowed?
// Would this affect the run-time complexity? How and why?
// Write a function to determine if a given target is in the array.

class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int idx_first = 0, idx_last = nums.size();
        
        while (idx_first != idx_last){
			
			int idx_mid = idx_first + (idx_last - idx_first) / 2;
			
			if (nums[idx_mid] == target) return true;
			
			if (nums[idx_first] < nums[idx_mid]){
				if (nums[idx_first] <= target && target < nums[idx_mid])
					idx_last = idx_mid;
				else
					idx_first = idx_mid + 1;
			}
			
			else if (nums[idx_first] > nums[idx_mid]) {
				if (nums[idx_mid] < target && target <= nums[idx_last-1])
					idx_first = idx_mid + 1;
				else
					idx_last = idx_mid;				
			}
			
			else
				idx_first++;
		}
		
		return false;
    }
};
