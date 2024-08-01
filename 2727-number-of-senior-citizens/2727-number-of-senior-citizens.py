class Solution:
    def countSeniors(self, details: List[str]) -> int:
        age = details[0][11:13]
        c=0

        for age in details:
            if int(age[11:13]) >60:
                c+=1
        return c