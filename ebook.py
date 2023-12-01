# Clean the data from an higlights and notes text document from Kindle

# Ask the user for the file name:
#fname = input('Please enter the file name: ')

# Open the file iterate over each line an print selected lines
source = open('test.txt', 'r')
destination = open('out.txt', 'w')

for line in source:
    line = line
    if 'D:' in line:
        continue
    elif '==' in line:
        continue
    elif '- Your Highlight' in line:
        continue
    destination.write(line)




