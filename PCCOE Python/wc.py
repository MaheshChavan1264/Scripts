"""
This module implements unix command wc
usage:
python wc FILENAME
"""
import sys

def linecount(filename):
    """
    returns number of lines in given file
    """
    with open(filename) as f:
        return len(f.readlines())
    
def wordcount(filename):
    """
    counts number of words in given file
    """
    with open(filename) as f:
        return len(f.read().split())
    

def charcount(filename):
    """
    returns number of charecters in given file
    """
    with open(filename) as f:
        return len(f.read())
    
if __name__ == "__main__":
    filename = sys.argv[1]
    print(linecount(filename), wordcount(filename), charcount(filename), filename)
