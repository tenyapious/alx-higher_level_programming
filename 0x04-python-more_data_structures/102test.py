#!/usr/bin/python3

a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}

s = 'C'

for i in list(a_dictionary):
    if a_dictionary[i] == s:
        del a_dictionary[i]

print(a_dictionary)
