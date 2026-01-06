class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_map={}
        final={}
        for str in strs:
            chars=[a for a in str]
            char_map[str]=chars
            chars=tuple(sorted(chars))
            if chars in final:
                final[chars].append(str)
            else:
                final[chars]=[str]
        return list(final.values())

        