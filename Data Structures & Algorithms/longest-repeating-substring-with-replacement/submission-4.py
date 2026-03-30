class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res=0
        mp={}
        l=0
        f=0
        for r in range(len(s)):
            mp[s[r]]=1+mp.get(s[r],0)
            f=max(f,mp[s[r]])
            while(r-l+1) - f>k:
                mp[s[l]]-=1
                l+=1
            res=max(res,r-l+1)


        return res

    