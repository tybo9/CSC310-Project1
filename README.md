Assignment 1


When to Submit
Due: 11:59pm, 9/9/2020

What to Submit
	Put your Python functions in a single .py file. Please ensure your codes are executable without errors. Clearly document it. 

How to Submit
	Submit all your code using the Canvas. 

1. Write a Python function that takes a positive integer N and returns the factorial of N, i.e., N! 
The factorial of N, denoted N!, is the product of the integers from 1 to N. (1 Point)

Examples: 
5!=5*4*3*2*1, 
4!=4*3*2*1
0!=1

2. Write a short Python function that takes a sequence of integer values and determines if there is a distinct pair of numbers in the sequence whose product is odd. (1 Point)

Examples: 
	Inputs: 2 4 5
	Outputs: false

	Inputs: 1 3 4
	Outputs: true

3. Write a python function that takes an integer (e.g., 342, -123) and returns its reverse digit (i.e., 243, -321).  (2 Point)

Examples:  

Input: 234
Output: 432

Input:-241
Output:-142

Notes: This function should be able to deal with both positive and negative integers. 




4.  Write a Python function that takes a string s, representing a sentence,
and returns a copy of the string with all comma removed.  (1 Point)

Examples: 
	Inputs: “Sit down, please”
	Output: “Sit down please”

	Input: “Hello Python, I don’t really know you well”
	Output: “Hello Python I don’t really know you well”

5. Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', write a Python function determine if the input string is valid. (2 Point)

An input string is valid if:
1.	Open brackets must be closed by the same type of brackets.
2.	Open brackets must be closed in the correct order.

You don’t need to worry about time complexity nor storage complexity.   

Examples: 
Input: s=”()”
Output: true
Input: s=”({})”
Output: true

Input : s=”(}”
Output: false

Input : s=”([{})]”
Output: false


 6. Write a Python function that merges two sorted lists and return a new sorted list. Both the input lists and output lists should be sorted. You might use the Python list as the data structure. (3 Point)

Examples: 
Input:  1<3<4, 1<2<6<8
Output: 1<1<2<3<4<6<8
