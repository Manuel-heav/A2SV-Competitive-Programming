class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fiveCounter = 0
        tenCounter = 0
        for bill in bills:
            if bill == 5:
                fiveCounter += 1
            elif bill == 10: 
                if fiveCounter > 0:
                    fiveCounter -= 1
                    tenCounter += 1
                else: 
                    return False
            elif bill == 20:
                if tenCounter > 0 and fiveCounter > 0:
                    fiveCounter -= 1
                    tenCounter -= 1
                elif fiveCounter >= 3:
                    fiveCounter -= 3
                else:
                    return False
        return True


                
        
        