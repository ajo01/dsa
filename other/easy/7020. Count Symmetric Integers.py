class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        
        for num in range(low, high+1):
            list = [int(i) for i in str(num)]
            if len(list) % 2 == 0:
                n = int(len(list)/2)
                first_sum = sum(list[:n])
                second_sum = sum(list[n:])
                if first_sum == second_sum:
                    count +=1
                
                
            
        return count
            
            
        