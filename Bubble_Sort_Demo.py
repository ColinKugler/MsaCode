import random

def bubble_sort(data_list):
    number_of_items = len(data_list)
    print(number_of_items)
#Loop through the list to visit each item
    for i in range(number_of_items):
        for j in range(number_of_items - 1):
            if(data_list[j] < data_list[j+1]):
                temp = data_list[j]
                data_list[j] = data_list[j+1]
                data_list[j+1] = temp
    return data_list
#Loop through list to compare items to adjacent items in list
#Compare adjacent items in list
#If right element is less than left element, swap positions.

def easier_sort(data_list):
    number_of_items = len(data_list)
    print(number_of_items)
#Loop through the list to visit each item
    for i in range(number_of_items):
        for j in range(number_of_index - 1):
            if(data_list[j+1] < data_list[j]):
                pass

def main():
    #Create a list of integers
    my_list= [5, 2 ,9, 1, 14, 7]
    integer_list = random.sample(range(0,1000), 100)
    print(integer_list)
    sorted_list = bubble_sort(integer_list)
    print(sorted_list)

main()