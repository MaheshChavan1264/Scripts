import sys

def square(x):
    return x*x

if __name__=="__main__":
    x = float(sys.argv[1])
    print(square(x))