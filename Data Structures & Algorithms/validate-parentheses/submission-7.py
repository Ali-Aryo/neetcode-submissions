class Solution:
    def isValid(self, s: str) -> bool:
        sets = {')':'(' ,  '}':'{' , ']':'['}
        stack = []
        for i in range(len(s)):
            if s[i] in "{[(":
                stack.append(s[i])
            if s[i] in "}])":
                if not bool(stack): #true if empty
                    return False
                if stack.pop() != sets[s[i]]:
                    return False 
        if not bool(stack): #true if empty
            return True
        return False

