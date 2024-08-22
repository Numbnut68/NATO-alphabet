student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato = {
    row.letter : row.code for (index, row) in nato_df.iterrows()
}
# print(nato)


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    u_input = input("Enter a word to convert to the Phonetic Alphabet\n").upper()
    try:
        phonetic_words = [nato[letter] for letter in u_input if not letter == " "]
    except KeyError:
        print("Only letters in the alphabet please")
        generate_phonetic()
    else:
        print(phonetic_words)


generate_phonetic()
