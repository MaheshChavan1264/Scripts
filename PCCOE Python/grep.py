import sys
def grep(filename,string):
    with open(filename) as file:
        f=file.read()
        for i in file:
            if string in i :
                print(i)
if __name__=="__main__":
    grep(sys.argv[1],sys.argv[2])