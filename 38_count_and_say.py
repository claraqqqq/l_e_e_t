# Count and Say
#
# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.
# Note: The sequence of integers will be represented as a string.

class Solution:
    # @return a string
    def countAndSay(self, n):
        seq = '1'
        for dummy_idx in range(n-1):
            prev_num = None
            new_seq = ''
            cnt = 0
            for cur_num in seq:
                if prev_num != None and prev_num != cur_num:
                    new_seq += str(cnt) + prev_num
                    cnt = 1
                else:
                    cnt += 1
                prev_num = cur_num
            new_seq += str(cnt) + prev_num
            seq = new_seq
        return seq