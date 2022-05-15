class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        if n == 0:
            return 
        
        p = m + n - 1
        d = m - 1
        s = n - 1
        while True:
            
            print(s, d, p)
            
            if nums2[s] >= nums1[d]:
                nums1[p] = nums2[s]
                s -= 1
            else:
                nums1[p] = nums1[d]
                d -= 1                
                
            p -= 1
            
            if s < 0:
                nums1[:p+1] = nums1[:d+1]
                break
            elif d < 0:
                nums1[:p+1] = nums2[:s+1]
                break
            
        