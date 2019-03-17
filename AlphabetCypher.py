key = {
'A': 'abcdefghijklmnopqrstuvwxyz',
'B': 'bcdefghijklmnopqrstuvwxyza',
'C': 'cdefghijklmnopqrstuvwxyzab',
'D': 'defghijklmnopqrstuvwxyzabc',
'E': 'efghijklmnopqrstuvwxyzabcd',
'F': 'fghijklmnopqrstuvwxyzabcde',
'G': 'ghijklmnopqrstuvwxyzabcdef',
'H': 'hijklmnopqrstuvwxyzabcdefg',
'I': 'ijklmnopqrstuvwxyzabcdefgh',
'J': 'jklmnopqrstuvwxyzabcdefghi',
'K': 'klmnopqrstuvwxyzabcdefghij',
'L': 'lmnopqrstuvwxyzabcdefghijk',
'M': 'mnopqrstuvwxyzabcdefghijkl',
'N': 'nopqrstuvwxyzabcdefghijklm',
'O': 'opqrstuvwxyzabcdefghijklmn',
'P': 'pqrstuvwxyzabcdefghijklmno',
'Q': 'qrstuvwxyzabcdefghijklmnop',
'R': 'rstuvwxyzabcdefghijklmnopq',
'S': 'stuvwxyzabcdefghijklmnopqr',
'T': 'tuvwxyzabcdefghijklmnopqrs',
'U': 'uvwxyzabcdefghijklmnopqrst',
'V': 'vwxyzabcdefghijklmnopqrstu',
'W': 'wxyzabcdefghijklmnopqrstuv',
'X': 'xyzabcdefghijklmnopqrstuvw',
'Y': 'yzabcdefghijklmnopqrstuvwx',
'Z': 'zabcdefghijklmnopqrstuvwxy'
}
def findReplacement(messageChar,cypherChar):
	alphaIndex = 0
	while key['A'][alphaIndex] != messageChar:
		alphaIndex += 1
	return key[cypherChar.upper()][alphaIndex]
def cypher(codeWord, message):
 
	initialStr = ""
	encodedStr = ""
	for i in range(len(message)):
		initialStr += codeWord[i%len(codeWord)]
	for i in range(len(message)):
		encodedStr += findReplacement(message[i],initialStr[i])
	return encodedStr
if __name__ == '__main__':
	print(cypher('bond','theredfoxtrotsquietlyatmidnight'))
	print("lumicjcnoxjhkomxpkwyqogywq" == cypher('snitch','thepackagehasbeendelivered'))
	print([1,2]==[1,2])
	print([1,2] is [1,2])