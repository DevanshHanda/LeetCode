class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        i=0
        m=len(students)
        s=sandwiches[::-1].copy()
        f=True
        l1=[]
        while f:
            if i==0:
                if l1==students:
                    break
                else:
                    l1=students.copy()
            if students[i]==-1:
                i=(i+1)%m
                continue
            if students[i]==s[-1]:
                s.pop()
                students[i] = -1
            i=(i+1)%m
        return m-students.count(-1)


