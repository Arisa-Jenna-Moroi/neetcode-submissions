class Solution:

    def encode(self, strs: List[str]) -> str:
        enc= ""
        for i in strs:
            enc += str(len(i)) + "#" + i
        return enc

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i<len(s):
            j=i
            while s[j] != '#':
                j +=1
            num = int(s[i:j])
            ans.append(s[j+1:j+1+num])
            i = j+1+num
        return ans
