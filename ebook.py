# Clean the data from an higlights and notes text document from Kindle

# Ask the user for the file name:
#fname = input('Please enter the file name: ')

# Open the file iterate over each line an print selected lines
fhand = open('test.txt')
count = 0
for line in fhand:
    line = line.rstrip()
    if not 'D:' in line:
        continue
    print(line)




