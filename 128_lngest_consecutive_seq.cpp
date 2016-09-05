// Longest Consecutive Sequence

/*
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
*/

/* Unordered Map
Unordered maps are associative containers that store elements formed by the combination of a key value and a mapped value, and which allows for fast retrieval of individual elements based on their keys.
*/

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {

        unordered_map<int, bool> rcrd;

        for (auto item: nums){
            rcrd[item] = false;
        }

        int longest_len = 0;

        for (auto item: nums){

            if (rcrd[item] == true){
        	      continue;
            }

        	  int len = 1;
        	  rcrd[item] = true;

        	  for (int item_y=item+1; rcrd.find(item_y)!=rcrd.end(); item_y++){
        		    rcrd[item_y] = true;
        		    len++;
        	  }

        	  for (int item_y=item-1; rcrd.find(item_y)!=rcrd.end(); item_y--){
        		    rcrd[item_y] = true;
        	    	len++;
          	}

        	  longest_len = max(longest_len, len);
        }

        return longest_len;
    }
};
