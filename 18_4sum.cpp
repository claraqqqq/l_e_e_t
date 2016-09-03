/*
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
*/

/*
std::unique: Removes all but the first element from every consecutive group of equivalent elements in the range [first,last).
std::vector::erase: Removes from the vector either a single element (position) or a range of elements ([first,last)).
*/
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        
        vector<vector<int>> res;
        
        if(nums.size() < 4) return res;
        
        sort(nums.begin(), nums.end());
        
        unordered_map<int, vector<pair<int, int>>> map_2sum;
        for(size_t idx=0; idx<nums.size(); idx++){
			for(size_t idy=idx+1; idy<nums.size(); idy++){
				map_2sum[nums[idx]+nums[idy]].push_back(pair<int,int>(idx,idy));
			}
		}
		
		for(size_t idz=0; idz<nums.size(); idz++){
			for(size_t idw=idz+1; idw<nums.size(); idw++){
				const int residual = target - nums[idz] - nums[idw];
				if (map_2sum.find(residual) != map_2sum.end()){
					const auto& vec = map_2sum[residual];
					for(size_t idt=0; idt<vec.size(); idt++){
						if (vec[idt].first > idw){
							res.push_back({nums[idz], nums[idw], nums[vec[idt].first], nums[vec[idt].second]});
						}
					}
				}
			}
		}
		sort(res.begin(), res.end());
		res.erase(unique(res.begin(), res.end()), res.end());
		return res;
    }
};

