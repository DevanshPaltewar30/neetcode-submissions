class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result={}
        for i in strs:
            count=[0]*26

            for ch in i:
                count[ord(ch)-ord("a")]+=1
            # we can't use list as key in dictionary
            # so we have to covert it into the tuple
            key=tuple(count)
            if key not in result:
                result[key]=[]
            result[key].append(i)
        return list((result.values()))



