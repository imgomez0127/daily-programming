from queue import LifoQueue
class Solution(object):
    
    def interview_question(self,sequence):
        stack = LifoQueue()
        cur_num_count = None
        while sequence != 0:
            num = sequence % 10
            if cur_num_count == None :
                cur_num_count = [num,1]
            elif num != cur_num_count[0]:
                stack.put(cur_num_count)
                cur_num_count = [num,1]
            else:
                cur_num_count[1] += 1 
            sequence = sequence // 10
        stack.put(cur_num_count)
        output_num = 0
        while(not stack.empty()):
            num = stack.get()
            output_num = 10 * output_num + num[1] 
            output_num = 10 * output_num + num[0]
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

