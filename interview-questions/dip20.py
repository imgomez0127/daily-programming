from collections import OrderedDict
class Solution(object):
    
    def interview_question(self,sequence):
        d = OrderedDict()
        while sequence != 0:
            num = sequence % 10
            d[num] = d.get(num,0) + 1    
            sequence = sequence // 10
        output_num = 0
        for num in d.keys():
            output_num = 10 * output_num + d[num] 
            output_num = 10 * output_num + num
        return output_num
s = Solution()
ans1 = s.interview_question(1)
ans2 = s.interview_question(ans1)
ans3 = s.interview_question(ans2)
ans4 = s.interview_question(ans3)
print(ans1)
print(ans2)
print(ans3)
print(ans4)

