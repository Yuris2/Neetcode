class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #Create an array of ordered pairs
        array = [(x,y) for x,y in zip(position, speed)]
        #Sort the array by decreasing p
        array.sort(key=lambda t:t[0], reverse = True)

        stack = []

        for p, s in array:
            #Calculate the time it takes to reach the target
            time = (target - p) / s
            stack.append(time)
            #if the stack has more than one fleet
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                #If the car behind it is faster, forms a fleet
                    #remove faster time
                stack.pop()
            #add to stack
        
        return len(stack)


        