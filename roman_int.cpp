class Solution {
    
private:
    int val[255];
    void init() {
        val['I'] = 1; val['V'] = 5; val['X'] = 10; 
        val['L'] = 50; val['C'] = 100; val['D'] = 500; 
        val['M'] = 1000; 
    }
    
public:
    int romanToInt(string s) {
        init();
        int res = 0;
        for (int i=0; i<s.size();i++) {
            if (i>0 && val[s[i-1]]<val[s[i]]) {
                res -= 2*val[s[i-1]];
            }
            res += val[s[i]];
        }
    return res;
    }
};
