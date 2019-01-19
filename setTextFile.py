import sys

# get and type cast second argument to int
first_arg = sys.argv[1]

f= open("var.txt","w+")
f.write(first_arg)
f.close()
