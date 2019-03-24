import sys
def cat(filename):
    with open(filename) as file:
        print(file.read())
if __name__=="__main__":
    cat(sys.argv[1])
    