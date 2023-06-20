"""
Function to perform quick sort
Input: Array
Output: Sorted list 
"""

def main():
    #create a list
    arr = [40, 80, 10, 90, 30, 50, 70]
    quicksort(arr)

def quicksort(arr):
    #Create a stack to simulate recursive calls
    stack = []
    #Place list partitions on the stack
    stack.append((0, len(arr) - 1))
    #Inside while loop; loop runs until the stack of partitions is empty.
    while stack:
        #Get the next partition to process
        low, high = stack.pop()
        pivot_index = partition(arr, low, high)
        #If there are items on the left side of the pivot, put them on the stack
        if pivot_index - 1 > low:
            stack.append((low, pivot_index - 1))
        #If there are items on the right of the oivot, put them on the stack.
        if pivot_index + 1 < low:
            stack.append((pivot_index + 1, high))


"""
Function to perform quick sort
Input: (list) arr, (int) low, (int) high
Output: (int)partition index
"""

def partition(arr, low, high):
    pivot = arr[high]
    #Choose the rightmost item as the pivot.
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    #loop hrough the partition to place all symbols <= pivot to the left, and >= to the right. If the current item is less than or equal to the pivot, 
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1

main()