# Programmer: Rizon Takabe
# Class: CS 240
# Date: 4/15/23
# Assignment: Insertion Sort
# Starting at 2nd index, it compares it with the elements to its left in the sorted portion of the array
# Once it finds the correct position it shifts the others to the right
def main():
    my_array = [1, 5, 7, 3, 2, 8, 10, 9]
    my_sorted_array = insertion_sort(my_array)
    numbers_txt = read_file("numbers-1.txt")
    numbers_txt_sorted = insertion_sort(numbers_txt)

    print(numbers_txt_sorted[7586])
    print(my_sorted_array)
# i is the index currently being considered for insertion, j iterates right to left 
# over the sorted portion of array to find the correct position, temp temporarily holds the value being considered
def insertion_sort(array):

    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        while j >= 0 and array[j] > temp:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp
    return array
# copies text file to array
def read_file(file):
    array = []
    with open(file, 'r') as file:
        for line in file:
            array.append(int(line))
    return array

main()