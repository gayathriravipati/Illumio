# Illumio_Assessment
Task: 

Write a program that reads a file and finds matches against a predefined set of words(predefined.txt).  


Input Files:

predefined.txt	- Contains a list of unique predefined words, one word in each line, which are alphanumeric
randomwords.txt	-  Contains multiple lines, each line have multiple words


Here are the assumptions:

1. Count and display the frequency of each word from `predefined.txt` in `randomwords.txt`, showing every word's count even if it's zero.
2. Sort the output first by frequency in descending order; if frequencies are tied, sort alphabetically.
3. Treat words with trailing punctuation (like '?', '!') as their base forms (e.g., "here?" as "here", but "it's" and "its" as distinct).


Time Complexity:
generate_map_from_file: O(n + m * k) => O(n + k) {m=1 as words in each line is only one}
read_and_count_words: O(n + m * k)
sorting: O(u log u)

n - number of lines
m - average number of words in each line
k -  average length of each word
u - size of the map i.e., number of predefined words 

Space Complexity: O(u) - size of the map

Command to execute: python3 getCount.py

Constraints given:  20 MB file and 10000 lines
Both the functions in the code, opens the file using with open(file_path, 'r') as file:. This ensures that the file is properly closed after reading, even if an exception occurs. 
The file is read line by line using for line in file:, which is memory efficient as it does not load the entire file into memory. This approach is suitable for large files. 

Also, the use of dictionaries for counting and regex for word extraction ensures the optimised solution.