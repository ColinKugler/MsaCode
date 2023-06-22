import random

def sequentialsearch(number_list, target_value):
    for index in range (len(number_list)):
        if target_value == number_list [index]:
            return index
        
    return -1


"""
Function to run binary search on a sorted list
Input: List, target value
Output: found index
"""
def binary_search(arr, target_value):
    low_index = 0
    high_index = len(arr) - 1
    #create a loop to search for target value
    while low_index <= high_index:
        middle_index = (low_index + high_index) //2

        #check if target value is at the middle index in the list

        if arr[middle_index] == target_value:
            return middle_index
        elif arr[middle_index] < target_value:
            low_index = middle_index + 1
        else:
            high_index = middle_index - 1

    return -1


def main():
    number_list = random.sample(range(1, 101), 100)
    number_list.sort()

    #foundindex = sequentialsearch(number_list, 77)
    foundindex = binary_search(number_list, 39)
    
    if foundindex == -1:
        print("Not in list")
    else:
        print(foundindex)


main()