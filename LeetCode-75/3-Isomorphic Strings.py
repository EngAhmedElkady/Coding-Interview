class Solution:
    
   
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):return 0
        ans=""
        dic={}
        lst=[False]*200
        for i in range(len(s)):
            x=dic.get(s[i],'_')
            if x=='_':
                if lst[ord(t[i])-ord('a')]==False:
                    dic[s[i]]=t[i]
                    x=t[i]
                    lst[ord(t[i])-ord('a')]=True
            ans+=x
        if ans == t:return 1
        else : return 0
            
        
if __name__=="__main__":
    ans=Solution()
    result=ans.isIsomorphic("bbbaaaba","aaabbbba")
    print(result)