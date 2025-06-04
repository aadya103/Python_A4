# Assignment 4 
This repository contains solutions for two tasks from Module 5: Files, Exceptions, and Errors in Python. The program is written in two Python files, Task 1 and Task 2.

## Task 1: Read a File and Handle Errors  
The program attempts to open and read the contents of a file named sample.txt. It reads and prints each line from the file. If the file does not exist, the program handles the error gracefully by printing an appropriate error message instead of crashing.

### Sample Output (If file exists)  
```sh
Reading file content:
Line 1: This is a sample text file.  
Line 2: It contains multiple lines.  
```  

### Sample Output (If file does not exist)  
```sh
Error: The file 'sample.txt' was not found.
```

## Task 2: Write and Append Data to a File  
The program prompts the user to enter some text, writes it to a file named output.txt, then takes additional input and appends it to the same file. After writing and appending, it reads and prints the final contents of the file.

### Sample Input/Output  
```sh
Enter text to write to the file: Hello, Python! 
Data successfully written to output.txt.

Enter additional text to append: Learning file handling in Python.
Data successfully appended.
Final content of output.txt:  

Hello, Python!  
Learning file handling in Python. 
```
