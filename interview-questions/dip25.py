from collections import defaultdict

def chainedWords(words):
    is_chainable = True
    for i in range(len(words)):
        is_chainable &= words[i][len(words[i])-1] == words[(i+1)%len(words)][0]
    return is_chainable

print(chainedWords(['apple', 'eggs', 'snack', 'karat', 'tuna']))
# True
