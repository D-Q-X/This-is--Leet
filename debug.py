class Solution:
    def isValid(self, s: str) -> bool:
        stack=list()
        if len(s)%2==1:
            return False
        dict={
            ")":"(",
            "]":"[",
            "}":"{"
        }
        for char in s:
            if char in dict :
                if stack[-1]!=dict[char]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)
        return len(stack)==0

sol=Solution()
print(sol.isValid("}("))