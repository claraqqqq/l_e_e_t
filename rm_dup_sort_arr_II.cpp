class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        
        if (nums.size() <= 2){
            return nums.size();
        }
        
        int pos = 0;
        int cnt = 1;
        
        for (int i=1; i<nums.size(); i++){
            if (nums[i] == nums[pos]){
                cnt ++;
                if (cnt == 2){
                    nums[++pos] = nums[i];
                }
            }
            else{
                cnt = 1;
                nums[++pos] = nums[i];
            }
        }
        
        return pos+1;
    }
};
