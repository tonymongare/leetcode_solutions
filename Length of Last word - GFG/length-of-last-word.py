#User function Template for python3

class Solution:

    def findLength(self, s):
        # code here
        length = 0
        
        new_str = s.strip()
        
        for i in range(len(new_str) -1, -1, -1):
            if new_str[i] == " ":
                return length
            else:
                length += 1
        return length

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):

        s = input()

        solObj = Solution()

        ans = solObj.findLength(s)

        print(ans)
# } Driver Code Ends