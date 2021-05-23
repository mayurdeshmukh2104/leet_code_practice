class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        { = 123, } = 125, ( = 40, ) = 41, [ = 91, ] = 93
        """
        list_parenthesis = list()
        for i in s:
            list_parenthesis.append(ord(i))
            for j in list_parenthesis:
                if j == 123 and ord(i) == 125:
                    list_parenthesis.remove(ord(i))
                    list_parenthesis.remove(j)
                elif j == 40 and ord(i) == 41:
                    list_parenthesis.remove(ord(i))
                    list_parenthesis.remove(j)
                elif j == 91 and ord(i) == 93:
                    list_parenthesis.remove(ord(i))
                    list_parenthesis.remove(j)
        #print(list_parenthesis)
        if not list_parenthesis:
            return True
        else:
            return False
        
    
solObj = Solution()
bool_val = solObj.isValid('([)]')
print(bool_val)