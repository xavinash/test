str1 = input("please input the string:")

def removeDuplicates(s):
	flag = 1
	while flag:
		original_l = len(s)
		i = 0
		while i < len(s)-1:
			if i>=0 and s[i]==s[i+1]==s[i+2] and chr(ord(s[i])-1)!="`":
				s=s[:i]+chr(ord(s[i])-1)+s[i+3:]
				print(s)
				i-=2
			i+=1
		if original_l == len(s):
			return s
removeDuplicates(str1)