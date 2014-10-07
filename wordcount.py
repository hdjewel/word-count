


import sys 
#get our data file name from the command line (*args)
script, file_name = sys.argv

#open file
with open(file_name) as poem_line:  
    word_count_dict = {}
    for line in poem_line:
        aline = line.rstrip().split(' ')
    print aline
#strip nonalpha characters from item

#populate dictionary

#print contents of dictionary to user
