def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r- m
  
    # Temp Arrays
    L = [0] * (n1)
    R = [0] * (n2)
  
    # Copying data to temp arrays L[] and R[]
    for i in range(0 , n1):
        L[i] = arr[l + i]
  
    for j in range(0 , n2):
        R[j] = arr[m + 1 + j]
  
    # Merging the temp arrays back into arr
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
  
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
  
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
  
# l is for left index and r is right index of the
def mergeSort(arr,l,r):
    if l < r:
  
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = (l+(r-1))//2
  
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
  
  
arr = [21,7,4,6,1,15]
n = len(arr)
print ("Given array is")
for i in range(n):
    print ("%d" %arr[i])
  
mergeSort(arr,0,n-1)
print ("\n\nSorted array is")
for i in range(n):
    print ("%d" %arr[i])


#  Output:
#  Given array is
#  21
#  7
#  4
#  6
#  1
#  15


#  Sorted array is
#  1
#  4
#  6
#  7
#  15
#  21
