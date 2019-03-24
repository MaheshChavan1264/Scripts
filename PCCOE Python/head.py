import sys

def head(file, n):
    with open(file) as f:
        for i in range(n):
            print(f.readline().strip())
            
if __name__ == "__main__":
    head(sys.argv[1], int(sys.argv[2]))