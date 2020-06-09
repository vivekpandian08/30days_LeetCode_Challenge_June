class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people,key = lambda a:(-a[0],a[1]))
        newlst = []
        for i in people:
             newlst.insert(i[1],i)
        return newlst