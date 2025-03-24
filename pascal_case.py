#ask user for their full name
ask_name = input("Enter full name: ")

#this is to capitalize all first letter of the words = .title()
title_cnvrtr = ask_name.title()

#print and removes the space using .replace(x, y)
print(title_cnvrtr.replace(" ", ""))