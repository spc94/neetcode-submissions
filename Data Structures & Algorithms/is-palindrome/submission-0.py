class Solution:
    # with smaller string there is not so much to worry about making it super efficient
    # larger strings 
    def isPalindrome(self, s: str) -> bool:
        # new string = s without non-alpha numeric
        # size of new string
        # from end to mid and start to mid -> compare each char
        # if not equal then return false
        # return true
        clean_string = ""
        for char in s:
            if char.isalnum():
                clean_string += char.lower()
        clean_string_size = len(clean_string)-1
        print("new string size")
        print(clean_string_size)
        mid = clean_string_size//2 # integer division
        print("mid")
        print(mid)
        k = 0
        print("new string: ", clean_string)
        for i in range(clean_string_size,mid,-1):
            if clean_string[k] == clean_string[i]:
                print("comparison: ", clean_string[k] , " == ", clean_string[i])
                k +=1
            else: 
                return False
        return True





        