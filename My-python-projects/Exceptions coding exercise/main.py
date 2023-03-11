###---IndexError handling---###
# fruits = ["Apple", "Pear", "Orange"]
#
# #TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError as ind_error:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")
#
# make_pie(4)

###---KeyError hanlding---###
# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]
# total_likes = 0
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError as key_error:
#         pass
#
# print(total_likes)

###---NATO alphabet exception handling---###
import pandas
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}
# print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def convert_to_NATO():
    user_input = input("word to spell phonetically:").upper()
    try:
        output = [nato_dict[letter] for letter in user_input]
    except KeyError as key_error:
        print("Only letter in the alphabet please")
        convert_to_NATO()
    else:
        print(output)
        convert_to_NATO()


convert_to_NATO()
