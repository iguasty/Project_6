# Project_6
 Sorting

**Design**

In this project, I was able to utilize some of my previous code from Project 5. A 2*5 array of boxes populated with random numbers is generated at the start of the program. The user presses the sort button which begins the swap sort program, moving the highest value to the end of the array by swapping values with the lower values. After the highest value is set, it goes to the next highest value all the way down to the lowest value so that the array is sorted low to high. Each box is highlighted yellow as it checks if its lower or higher than the next box. A box is highlighted pink if its going to swap with the right value and cyan if its going to swap with the left. The box turns green if the value is sorted.

**Testing**

A pytest was added to test if the values in the boxes were being swapped correctly. It creates 2 test labels and swaps them using the swap_val function and then checks to see if they were actually swapped.