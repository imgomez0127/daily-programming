from operator import itemgetter
from collections import Counter
class Solution(object):
  def topKFrequent(self, words, k):
    counter = Counter(words)
    return [word 
            for word,frequency in 
            sorted(
                sorted(
                    counter.most_common(k),
                    key=lambda x : x[0]
                ),
                key=lambda x : x[1],
                reverse=True
            )]
words = ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"]
k = 2
print(Solution().topKFrequent(words, k))
# ['pro', 'daily']
