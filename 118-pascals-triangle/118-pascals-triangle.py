class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        output = [[1]]
        
        while numRows > 1:
            numRows -= 1
            prevR = [0] + output[-1] + [0]
            output.append([
                prevR[i] + prevR[i + 1]
                for i in range(len(prevR) - 1)
            ])
            
        return output
            
            