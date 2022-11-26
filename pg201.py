# 10-6, 10-7 Addition (Calculator)
print('Enter two numbers and I will add them.\nEnter \'q\' to exit.')

while True:
    num_1 = input('first number:\nanswer: ')
    if num_1 == 'q':
        break
    num_2 = input('second number:\nanswer: ')
    if num_2 == 'q':
        break
    
    try:
        sum = int(num_1) + int(num_2)
    except ValueError:
        print('Your input value needs to be a number.')
    else:
        print(f'\tresult: {sum}\n')

# 10-8. Cats and Dogs
file1 = r'C:\Users\Jimmy Son\Desktop\Python Crash Course\codes\path_chapter10\text1.txt'
file2 = r'C:\Users\Jimmy Son\Desktop\Python Crash Course\codes\path_chapter10\text2.txt'

files = [file1, file2]
print('')

for file in files:
    try:
        with open(file, 'r') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f'The file {file} is missing.')
    else:
        print(contents)

# 10-9. Silent Cats and Dogs
for file in files:
    try:
        with open(file, 'r') as f:
            contents = f.read()
    except FileNotFoundError:
        #print(f'The file {file} is missing.')
        pass
    else:
        print(contents)

# 10-10. Common Words
file3 = 'hippodrome_sktaing_book.txt'

try:
    with open(file3, encoding = 'utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f'The file {file3} does not exist.')
else:
    word = 'joy'
    word_count = contents.lower().count(word)   # lower() catches all appearances, regardless of th
    print(f'The word {word} appears {word_count} times in {file3}.')
    