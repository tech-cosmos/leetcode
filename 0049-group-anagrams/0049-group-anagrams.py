class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final={}
        for str in strs:
            chars=tuple(sorted(str))
            if chars in final:
                final[chars].append(str)
            else:
                final[chars]=[str]
        return list(final.values())

        