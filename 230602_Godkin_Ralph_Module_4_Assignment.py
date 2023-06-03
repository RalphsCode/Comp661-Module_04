# PART A

# f = open('file.txt', 'w')
# txt_string = 'This is a test file\nHello Student\nTesting 1,2,3 - testing !\nPython rocks !'
# f.write(txt_string)
# f.close()


# QUESTION 1

# with open('file.txt', 'r') as f:   
#     counter = 0 
#     for line in f.readlines():
#         counter += 1
#     print(f'\nThere are {counter} lines of text in file.txt.\n')


# QUESTION 2

# with open('file.txt', 'r') as f: 
#     words = f.read()

# words_without_commas = words.replace(",", " ")
# word_list = words_without_commas.split()
# five_count = 0
# for words in word_list:
#     if (len(words)) == 5:
#         five_count += 1

# print(f'\nThere are {five_count} five-letter word(s) in the file.\n')


# QUESTION 3

# import os

# path = os.getcwd()
# files = os.listdir(path)
# for file in files:
#     print(file)


# QUESTION 4

# import os

# file_to_find = input('Please enter a filename with extension (eg: file.txt) ')
# cwd = os.getcwd()
# if os.path.isfile(os.path.join(cwd, file_to_find)):
#         print(f'\nThe file: "{file_to_find}" was found in the current directory.\nHere are the contents of the file: \n')
#         with open('file.txt', 'r') as f: 
#             print(f.read())
# else:
#     print(f'\nERROR: The file: "{file_to_find}" was NOT found in the current directory.\n')


# QUESTION 5

# with open('accounts.txt', 'a') as f: 
#     content = '100 Mary 34.58 200 Alison 345.67 300 Marc 3.00 400 Zoltar -32.16 500 Kathleen 24.32'
#     f.write(content)


# QUESTION 6


import os

with open('accounts.txt', 'r') as f: 
    content = f.read()                                                      # READ ORIGINAL FILE
    print(f'\nInitial Accounts File ("accounts.txt"):\n{content}')

word_content = content.split()                                              # PUT THE TXT FILE CONTENTS INTO A LIST
location = word_content.index('Zoltar')
word_content[location] = 'Robert'                                           # REPLACE ZOLTAR WITH ROBERT
print(f'\nUpdated Accounts File:\n{word_content}')

os.remove('accounts.txt')                                                   # DELETE ORIGINAL FILE

with open('myaccounts.txt', 'a') as f: 
    content_string = ' '.join(word_content)
    content_without_apostrophie = content_string.replace("'", "")
    f.write(content_without_apostrophie)                                    # POPULATE THE NEW FILE

with open('myaccounts.txt', 'r') as f: 
     print(f'\nNew File ("myaccounts.txt") Content: \n{f.read()}\n')        # DISPLAY NEW FILE