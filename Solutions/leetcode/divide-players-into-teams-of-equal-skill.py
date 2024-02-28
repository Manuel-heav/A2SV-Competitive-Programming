class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        chemistry = []
        l = 0
        r = len(skill) - 1
        count = 0
        N = (sum(skill) * 2) / len(skill)
        while l < r:
            if skill[l] + skill[r] == N:
                chemistry.append(skill[l] * skill[r])
                count += 1
                l+=1
                r-=1
            elif skill[l] + skill[r] > N:
                r-=1
            elif skill[l] + skill[r] < N:
                l+=1
        
        if count != len(skill) / 2:
            return -1
        else:
            return sum(chemistry)
            

        