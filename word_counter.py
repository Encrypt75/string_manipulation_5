#ask user for a sentence or common phrase
words = input("Enter a sentence or phrase: ")

#this block convert str into list using .split()
str_spliter = words.split()

#this part uses len() to count how many words are in a list
print(len(str_spliter))