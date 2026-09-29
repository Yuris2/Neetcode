import random
class RandomizedSet:
    def __init__(self):
        #Val = Index
        self.dic = {}
        self.arr = []
        self.elem = 0


    
    def insert(self,val:int)->bool:
        res = False

        if val not in self.dic:
            self.arr.append(val)
            self.dic[val] = self.elem
            self.elem += 1

        return res
    
    def remove(self,val:int)->bool:
        res = False

        if val in self.dic:
            targetIndex = self.dic[val]
            lastElem = self.arr[-1]

            self.arr[targetIndex] = lastElem
            self.dic[lastElem] = targetIndex

            del self.dic[val]
            self.arr.pop()
            self.elem -= 1

        #Dictionary
        return res
        #List = []
    
    def getRandom(self)->int:
        #Get Random
        return random.choice(self.arr)
        #List = []



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()