class Item(object):  # represent items to be packed using a class

    def __init__(self,name,volume,value):
        self.name = name
        self.volume = volume
        self.value = value

    def __repr__(self):
        return "<{}: vol={} value={}>".format(self.name,self.volume, self.value)


def solveKnapsackProblem(items,maxCapacity):  
    ''' returns an optimal list of items to pack,
    and the total value of these items '''
    if maxCapacity <= 0 or items == []:  # base case
        return [],0

    else:
        bestValue = 0
        bestNextItem = None

        for i in range(len(items)):

            if items[i].volume <= maxCapacity:
                restOfItems = items[:i] + items[i+1:]
                print(restOfItems)
                restSolutionList, restValue = solveKnapsackProblem(restOfItems, maxCapacity - items[i].volume)

                if items[i].value + restValue > bestValue:
                    bestNextItem = items[i]
                    bestValue = bestNextItem.value + restValue
                    bestSolutionList = [bestNextItem] + restSolutionList

        if bestNextItem == None:  # all the items are too big
            return [],0
        else:
            return bestSolutionList, bestValue

# >>>testItems = [Item("item 1", 2, 4), Item("item 2", 3, 5), Item("item3", 7, 6)]
# >>>solveKnapsackProblem(testItems, maxCapacity=9)

################################################################
def solveKnapsackGREEDY(items, maxCapacity):
    ''' returns a near-best solution based on packing in order of value density '''
    
    remainingCapacity = maxCapacity
    solutionList, solutionValue = [], 0

    for item in sorted(items, key=lambda x: x.value/x.volume, reverse=True):
        if item.volume <= remainingCapacity:
            solutionList.append(item)
            solutionValue += item.value
            remainingCapacity -= item.volume
    return solutionList, solutionValue

# >>>testItems = [Item("item 1", 2, 4), Item("item 2", 3, 5), Item("item3", 7, 6)]
# >>>solveKnapsackGREEDY(testItems, maxCapacity=9)
