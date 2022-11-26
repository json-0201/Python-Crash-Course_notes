# whitespace - nonprinting character [space, tabs, end-of-line symbols]
# tab - \t
# newline - \n

print('python')
print('\tpython')


print('languages:\npython\nC\nJava')


print('languages:\n\tpython\n\tC\n\tJava')

# stripping whitespace left/right/both - '.strip()', '.lstrip()', '.rstrip()'

language = 'python      '

if language == 'python':
    print ('no whitespace detected')
else:
    print('whitespace detected')

##############################

# assigning variable with permanent change - var = var.method()
language = language.rstrip()

if language == 'python':
    print ('no whitespace detected')
else:
    print('whitespace detected')
