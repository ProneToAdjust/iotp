import sys

# get and type cast second argument to int
on_off_arg = sys.argv[1]

if(int(on_off_arg) != 0) and (int(on_off_arg) != 1):
    f = open("brightness_variable.txt","w+")
    f.write(on_off_arg)
    f.close()
elif(int(on_off_arg) == 0) or (int(on_off_arg) == 1):
    f = open("on_off_variable.txt","w+")
    f.write(on_off_arg)
    f.close()
