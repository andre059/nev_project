#file = open('test.txt', 'rt')  # read, text

#content = file.read(5)
#print(content)

#for line in file:
    #print(line)


#file.close()

with open('test.txt', 'rt') as file:
    for line in file:
        print(line)

