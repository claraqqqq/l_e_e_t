class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        map<int, int> mm;
        vector<int> res;
        for (int i=0; i<nums.size(); i++){
            
            if (mm.find(target-nums[i]) != mm.end()){
                res.push_back(mm[target-nums[i]]+1);
                res.push_back(i+1);
                break;
            }
            else{
                mm[nums[i]] = i;
            }
        }
        return res;
        
    }
};
