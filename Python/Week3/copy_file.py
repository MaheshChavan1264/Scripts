import sys

infilename=sys.argv[1]
outfilename=sys.argv[2]

infile=open(infilename)
outfile=open(outfil\
\
ename,"w")
for line in infile:
    outfile.write(line)
infile.close()
outfile.close()