def longestStr(str1,str2):
	if str1 == "" and str2 == "":
		return str1
	if str1 == "":
		return str2
	if str2 == "":
		return str1
	return longestStr(str1[1:],str2[1:])
def longestStrLen(str1,str2):
	if str1 == "" and str2 == "":
		return 0
	if str1 == "":
		return 1 + longestStrLen(str1,str2[1:])
	if str2 == "":
		return 1 + longestStrLen(str1[1:],str2)
	return 1 + longestStrLen(str1[1:],str2[1:])

print(longestStr('yeet','yeeter'))
print(longestStr('yeeter','yeet'))
print(longestStr("yuh","yea"))
print(longestStrLen('yeet','yeeter'))
print(longestStrLen('yeeter','yeet'))
print(longestStrLen("yuh","yea"))