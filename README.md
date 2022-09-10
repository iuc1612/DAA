# DAA
## Rising Towers 
In this problem, the user has two choices: either have random numbers in the matrix or to insert values in the matrix themselves.
For random numbers, I imported random and numpy packages of Python. used them to appened random numbers to the matrix.
For the user input, I took one temporary array and one index variable. The user input will be stored in the temp array. 
When -1 is inserted in the array, the contents of the array are appended to the matrix as a column. 
The array is then cleared and the index is incremented. 

For the logic of checking for rising towers:  the 0th element of the 0th column/tower is compared to the next element of the tower. If the next element is greater than the previous element,the tower is a rising tower. 
This is implemented in a nested for loop over all the elements of all the towers.
