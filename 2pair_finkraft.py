



def findPair(l, target):
    numMap = {}
    for num in l:
        diff = target-num
        if diff!=0 and diff in numMap:
            return (num,diff)
        numMap[num]=1
    
    return ()

l = [4,5,34,6,7]
target = 13
print(findPair(l,target))


