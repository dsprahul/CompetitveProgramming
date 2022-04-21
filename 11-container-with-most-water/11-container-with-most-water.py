class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        calc_this_container_area = lambda w1, w2, h1, h2: abs(w1 - w2) * min(h1, h2)
        
        
        max_container_area = -float("inf")
        n = len(height)
        w1 = 0
        w2 = n - 1
        
        while w1 <= w2:
            
            this_container_area = calc_this_container_area(w1, w2, height[w1], height[w2])
            max_container_area = max(max_container_area, this_container_area)
            
            if height[w1] < height[w2]:
                w1 += 1
            else:
                w2 -= 1
                
        return max_container_area
                
        