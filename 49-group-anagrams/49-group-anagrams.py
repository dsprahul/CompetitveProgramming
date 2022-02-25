class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        import string
        import functools
        
        clusters = []
        if strs.count("") > 0:
            clusters.append([""] * strs.count(""))
        
        strs = [st for st in strs if st != ""]
        
        first_26_primes = [
            2,	3,	5,	7,	11,	13,	17,	19,	23,	29,
            31,	37,	41,	43,	47,	53,	59,	61,	67,	71,
            73,	79,	83,	89,	97,	101
        ]
        char_to_num = {
            c: first_26_primes[i] for i, c in enumerate(string.ascii_lowercase)
        }
        
        strs_num = [functools.reduce(lambda x, y: x*y, map(lambda x: char_to_num[x], numstr)) for numstr in strs]
        
        for cluster_pow in set(strs_num):
            clusters.append(
                [strs[idx] for idx in range(len(strs)) if strs_num[idx] == cluster_pow]
            )
                                     
        return clusters