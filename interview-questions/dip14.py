def distance(s1, s2):
    if s1 == "":
        return len(s2)
    if s2 == "":
        return len(s1)
    if s1[0] == s2[0]:
        return distance(s1[1:],s2[1:])
    insertion = distance(s1[1:],s2) + 1
    deletion = distance(s1,s2[1:]) + 1
    replacement = distance(s1[1:],s2[1:]) + 1
    return min(insertion,deletion,replacement)
         
print(distance('biting', 'sitting'))
print(distance("hello", "hello"))
print(distance("helllo","hello"))
# 2
