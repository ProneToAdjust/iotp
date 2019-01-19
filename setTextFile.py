import sys

# get and type cast second argument to int
first_arg = sys.argv[1]

if(int(first_arg) != 0) and (int(first_arg) != 1):
    f = open("brightness_variable.txt","w+")
    f.write(first_arg)
    f.close()
elif(int(first_arg) == 0) or (int(first_arg) == 1):
    f = open("on_off_variable.txt","w+")
    f.write(first_arg)
    f.close()
