


#Importing the module Random to use Random methods
import random

#Importing the module timeit to Measure the time needed to execute this code
import time
print()

size_Str=input("Enter size: ")
k_str=input("Enter the the order of the kth smallest element: ")
threshold_str =input("Enter the threshold for the Hybrid merge sorting: ")

size=int(size_Str)
k=int(k_str)
threshold=int(threshold_str)
print()
#Creating empty arrays of size "size"
arr =[None]*(size)
arr1=[None]*(size)
arr2=[None]*(size)
arr3=[None]*(size)
arr4=[None]*(size)
arr5=[None]*(size)


#Initalizing the empty array with random integers numbers from 0 to 50000
for i in range(len(arr)):
    arr[i]=random.randint(0,99999)

#making more arrays with same elements for testing
for i in range(len(arr)):
    arr1[i]=arr[i]
    arr2[i]=arr[i]
    arr3[i]=arr[i]
    arr4[i]=arr[i]
    arr5[i]=arr[i]


#Merge Algorithm
def mergeSort(arr):
    # If this condition is not satisfied then the Recurrence function will reach its base
    if(len(arr)>1):

        # creating 2 temporary arrays and dividing arr to both
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        #Sorting the 2 halves by recursion

        mergeSort(L)
        mergeSort(R)
        # i is the index of the 1st array
        # j is the index of the 2nd array
        # k is the index of the merged array
        i = 0
        j = 0
        k = 0
        n1 = len(L)
        n2 = len(R)

        # compares the 1st non-used elements in each array with each other
        # Where the smallest one gets to enter the array
        # loop ends when one of the 1st/2nd arrays end

        while (i < n1 and j < n2):
            if (L[i] < R[j]):
                arr[k] = L[i]
                k += 1
                i += 1
            else:
                arr[k] = R[j]
                k += 1
                j += 1

        # Empties whatever array is left into the merged one

        while (i < n1):
            arr[k] = L[i]
            k += 1
            i += 1

        while (j < n2):
            arr[k] = R[j]
            k += 1
            j += 1

#QuickSort Algorithm
def Random_QuickSort(A, p, r):
    if p < r:
        q = Random_Partition(A, p, r)
        Random_QuickSort(A, p, q - 1)
        Random_QuickSort(A, q + 1, r)
# finds a random index and replace it with the last element in the array and continue
# as a normal last pivot quick sort
def Random_Partition(A, p, r):
    i = random.randint(p, r)
    A[i], A[r] = A[r], A[i]
    return Partition(A, p, r)
# finding the right position in the array for the pivot
def Partition(A, p, r):
    pivot = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    # return the right index of the pivot
    return i + 1

#Insertion Algorithm
def insertionSort(arr):
    for i in range(len(arr)):
        key=arr[i]
        j=i
        while(j>0 and arr[j-1]>key):
            arr[j]=arr[j-1]
            j=j-1
        arr[j]=key

#SelectionSort
def selectionSort(arr):
    #We used i<n-1 as a condition to make i reach the 2nd last term instead of the last since the last one will be already sorted and need no further comparisons
    for i in range(len(arr)-1):
        #Assuming the first element in the unsorted array is the minimum
        min=i
        #making j check the rest of the unsorted array except the one i pointing to
        for j in range(i+1,len(arr)):
            if(arr[min]>arr[j]):
                #Sets the new minimum if found
                min=j
        #Checks if the first element is indeed the minimum or not if not swaps else the loop of i continues
        if min!=i:
            arr[min],arr[i]=arr[i],arr[min]

#Hybrid
def hybrid(arr, threshold):
    if (len(arr) > 1):
        if len(arr) <= threshold:
            selectionSort(arr)
            return
        else:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            # Sorting the 2 halves by recursion

            hybrid(L, threshold)
            hybrid(R, threshold)
            # i is the index of the 1st array
            # j is the index of the 2nd array
            # k is the index of the merged array
            i = 0
            j = 0
            k = 0
            n1 = len(L)
            n2 = len(R)

            # compares the 1st non-used elements in each array with each other
            # Where the smallest one gets to enter the array
            # loop ends when one of the 1st/2nd arrays end

            while (i < n1 and j < n2):
                if (L[i] < R[j]):
                    arr[k] = L[i]
                    k += 1
                    i += 1
                else:
                    arr[k] = R[j]
                    k += 1
                    j += 1

            # Empties whatever array is left into the merged one

            while (i < n1):
                arr[k] = L[i]
                k += 1
                i += 1

            while (j < n2):
                arr[k] = R[j]
                k += 1
                j += 1

#Find Kth
def find_Kth_smallest_Element(A,p,r,k):
    if p<r :
        q = Partition(A,p,r)
        if k<q:
            find_Kth_smallest_Element(A,p,q-1,k)
        elif k>q:
             find_Kth_smallest_Element(A,q+1,r,k)
        else:
            # this mean that the pivot is the elemnt that i am looking for
            return A[q]
    # this means that i have sorted the array and i can access the element that i am looking for
    return A[k]


#Runtime of Merge Sort
start_time=time.time()
mergeSort(arr)
end_time=time.time()
run_time=end_time-start_time
run_time=run_time*1000
print("Runtime of Pure Merge Sort "+ str(run_time) +" ms")


#Runtime of Random Pivot QuickSort
start_time=time.time()
Random_QuickSort(arr1,0,len(arr1)-1)
end_time=time.time()
run_time=end_time-start_time
run_time=run_time*1000
print("Runtime of Random pivot Quick Sort "+ str(run_time) +" ms")

#Runtime of Hybrid Merge+Selection Sort
start_time=time.time()
hybrid(arr4,threshold)
end_time=time.time()
run_time=end_time-start_time
run_time=run_time*1000
print("Runtime of Hybrid Sort "+ str(run_time) +" ms")

#Runtime of Insertion Sort
start_time=time.time()
insertionSort(arr2)
end_time=time.time()
run_time=end_time-start_time
run_time=run_time*1000
print("Runtime of Insertion Sort "+ str(run_time) +" ms")


#Runtime of Selection Sort
start_time=time.time()
selectionSort(arr3)
end_time=time.time()
run_time=end_time-start_time
run_time=run_time*1000
print("Runtime of Selection Sort "+ str(run_time) +" ms")

count=[-1]
def checkOrdered(arr):
    count[0]=count[0]+1
    for i in range(len(arr)-1):
        if(arr[i]>arr[i+1]):
            print("The array arr"+str(count[0])+" is not Sorted correctly")
            return
    print("The array arr"+str(count[0])+" is Sorted")

#Checking if the sorting algorithms are done correctly
print()
checkOrdered(arr)
checkOrdered(arr1)
checkOrdered(arr2)
checkOrdered(arr3)
checkOrdered(arr4)
print()

kth=find_Kth_smallest_Element(arr5,0,len(arr5)-1,k-1)

if(k%10==1):
    print("The "+str(k)+"st smallest element is "+str(kth))
    print("For checking:")
    print("The " + str(k) + "st smallest element in arr1 (array sorted by Quick sort) is " + str(arr1[k-1]))
elif(k%10==2):
    print("The " + str(k) + "nd smallest element is " + str(kth))
    print("For checking:")
    print("The " + str(k) + "nd smallest element in arr1 (array sorted by Quick sort) is " + str(arr1[k - 1]))
elif(k%10==3):
    print("The " + str(k) + "rd smallest element is " + str(kth))
    print("For checking:")
    print("The " + str(k) + "rd smallest element in arr1 (array sorted by Quick sort) is " + str(arr1[k - 1]))
else:
    print("The " + str(k) + "th smallest element is " + str(kth))
    print("For checking:")
    print("The " + str(k) + "th smallest element in arr1 (array sorted by Quick sort) is " + str(arr1[k - 1]))
