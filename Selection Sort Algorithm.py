# Programmer: Rizon Takabe
# Class: CS 240
# Date: 4/15/23
# Assignment: Selection Sort
# This algorithm saves the index of the smallest integer in an unsorted array and adds it to a new array
# and pops it from the unsorted array until were left with an empty old array and a sorted new array
def main():
    myArray = [5,6,9,10,2,1,7,8,12,3,200,69,63,155,66,34,24,101,107,999,909]
    numbers_file = read_file("numbers-1.txt")
    print(selection_sort(numbers_file)[7586])
    print(selection_sort(myArray))    

# takes in an array and iterates over entire thing while keeping track of smallest int and returns its index
def find_smallest_num(array):
    smallest_num = array[0]
    smallest_num_index = 0
    for i in range(1, len(array)):
        if array[i] < smallest_num:
            smallest_num = array[i]
            smallest_num_index = i
    return smallest_num_index

# removes the smallest number in unsorted array and adds it to new array
def selection_sort(array):
    new_array = []

    for i in range(len(array)):
        smallest_num = find_smallest_num(array)
        new_array.append(array.pop(smallest_num))
    return new_array

# convert the numbers.txt file to an array
def read_file(file_name):
    file_array = []
    with open(file_name, 'r') as file:
        for line in file:
            file_array.append(int(line))
    return file_array

main()