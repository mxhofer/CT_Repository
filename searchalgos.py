def insertionSort (A, direction = "up"):
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
