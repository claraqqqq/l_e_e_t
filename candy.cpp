class Solution {
public:
    int candy(vector<int>& ratings) {
        
        vector<int> candyCnt(ratings.size());
        candyCnt[0] = 1;
        for(int i =1; i < ratings.size(); i++){
            if(ratings[i] > ratings[i-1]){
                candyCnt[i] = candyCnt[i-1] + 1;
            }
            else{
                candyCnt[i] = 1;
            }
            
        }
        
        int totalCandy = candyCnt[ratings.size()-1];
        for(int i=ratings.size()-2; i>=0; i--){
            if(ratings[i] > ratings[i+1] && candyCnt[i] <= candyCnt[i+1]){
                candyCnt[i] = candyCnt[i+1] + 1;
            }
            totalCandy += candyCnt[i];
        }
        
        return totalCandy;
    }
};
