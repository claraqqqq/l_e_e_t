class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int tail = nums.size() - 1;
        int i = 0;
        while(i <= tail){
            if(nums[i] == val){
                nums[i] = nums[tail--];
                continue;
            }
            i++;
        }
        return tail+1;
    }
};
