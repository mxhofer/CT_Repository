def insertionSort (A, direction = "up"):  # first-try version
    print(A)
    for j in range(1,len(A)):
        key = A[j]
        i = j-1
        if direction == "up":
            while i>=0 and A[i]>key:
                A[i+1],A[i] = A[i],A[i+1]
                print("--- ", A)
                i = i-1
        else:
            while i>=0 and A[i]<key:
                A[i+1],A[i] = A[i],A[i+1]
                print("--- ", A)
                i = i-1
    return A
    
def insertionSort (A):  # improved version
    for j in range(1,len(A)):
        key = A[j]
        i = j-1
        while i>=0 and A[i]>key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
    return A

def insertionSort (A) :  # improved version with print() statements to understand better
    print ("list to be sorted = ", A)
    for j in range (1, len (A)) :
        key = A[j]
        print ("  key = {} (at index {})".format (key, j))
        i = j - 1
        while i >= 0 and A[i] > key :
            A[i + 1] = A[i]
            print ("    moving number {} at index {} one place to right giving: {}".format (A[i], i, A))
            i = i - 1
        A[i + 1] = key
        print ("    finally changing number that was at index {} with the key value {} giving: {}".format (i + 1, key, A))
    print ("sorted list = ", A)
    return A

#bubble sort algorithm
#you compare two adjacent numbers and swap them if not ascending
#this is a polynomial time algorithm, because it got a square in it due to the two loops. Quite inefficient.
def bubbleSort(A):
    for b in range(len(A)-1):
        for i in range(len(A)-1-b):
            swap = False
            if A[i] > A[i+1]:
                A[i+1],A[i] = A[i],A[i+1]
                swap = True
        if not(swap):
            break
    return A

def search(findItem,list):
    for counter,item in enumerate(list): #enumarte creates format of [counter, item]
        if item==findItem:
            return counter
    else:
        return "n not in list"

#easier method using Python's built in .index method
def easysearch(nlist, n):
    if n in nlist:
        return nlist.index(n)
    else: return "change n"
