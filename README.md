# Illumio_Assessment
Task: 

Write a program that reads a file and finds matches against a predefined set of words(predefined.txt) based on the given constraints.  


Input Files:

predefined.txt	- Contains a list of unique predefined words, one word in each line, which are alphanumeric
randomwords.txt	-  Contains multiple lines, each line having multiple words


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

Constraints: The file size can be around 20 MB and may contain up to 10,000 lines.

Both functions in the code open the file using with open(file_path, 'r') as file: This ensures that the file is properly closed after reading, even if an exception occurs. The file is read line by line using "for line in file:", which is memory efficient because it does not load the entire file into memory at once. This approach is well-suited for handling large files.
Also, the use of dictionaries for counting and regex for word extraction ensures the optimized solution.

How to run the program: python3 getCount.py

What is tested?
The program is tested using specific input files that include predefined words and random text. The tests cover a range of word types, including:

- All lowercase letters (e.g., "spectacular")
- All uppercase letters (e.g., "AHJKJS")
- Mixed uppercase and lowercase letters (e.g., "semiCircular")
- Numerical-only words (e.g., "29339")
- Alphanumeric combinations (e.g., "nvm2929")
- Words with apostrophes (e.g., "It's")




