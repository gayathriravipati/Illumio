import re

#Reads the words from the given file, creates a dictionary{frequency_map} where each key is a lowercase version of a word from the file, and each value is a list containing the original word and a count initialized to 0.
def generate_map_from_file(file_path):
    frequency_map = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    converted_word = ''.join([char.lower() if char.isupper() else char for char in word])
                    if converted_word not in frequency_map:
                        frequency_map[converted_word] = [word, 0]
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return frequency_map

#Iterates through each line and also each word in line, converts any uppercase char to lowercase and if there is a matching word found in the dictionary then increment its respective count
def read_and_count_words(file_path, frequency_map):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                words = re.findall(r"\b[\w'-:]+\b", line)  #To handle punctuation in between the words
                for word in words:
                    converted_word = ''.join([char.lower() if char.isupper() else char for char in word])
                    if converted_word in frequency_map:
                        frequency_map[converted_word][1] += 1
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

predefined_file_path = 'predefined.txt'
randomwords_file_path = 'randomwords.txt'
frequency_map = generate_map_from_file(predefined_file_path)

#print("Word Map:", frequency_map)

read_and_count_words(randomwords_file_path, frequency_map)

#Sorting the values in the frequency_map based on the count to print the results in decreasing order
sorted_words = sorted(
    [(value[0], value[1]) for value in frequency_map.values()],
    key=lambda x: (-x[1], x[0])
)

# Print the results
for word, count in sorted_words:
    print(f"{word}: {count}")
