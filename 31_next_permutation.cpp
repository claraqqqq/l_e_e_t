/*
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
*/

/*
typedef: A type alias is a different name by which a type can be identified. In C++, any valid type can be aliased so that it can be referred to with a different identifier.
typedef existing_type new_type_name ;
typedef char C;


*/
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        //if(nums.size()<2) return;

        int partition = -1;
        for(int idx=0; idx<nums.size()-1; idx++){
			       if(nums[idx]<nums[idx+1]){
				           partition = idx;
			      }
		    }

		    if(partition == -1){
			       sort(nums.begin(), nums.end());
			      return;
		    }

		    int label;
		    for(int idx=partition+1; idx<nums.size(); idx++){
			       if(nums[idx]>nums[partition]){
				           label = idx;
			       }
		    }

		    int tmp = nums[label];
		    nums[label] = nums[partition];
		    nums[partition] = tmp;

		    reverse(nums.begin()+partition+1, nums.end());
    }
};
