import sys     # we need this library to deal with operating system

filename = sys.argv[1]

infile = open(filename)

for line in infile:
    print(line) # the file has "\n" at the end of each line already

infile.close()