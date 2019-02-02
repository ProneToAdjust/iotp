# import necessary packages
import sys

# get and type cast second argument to int
on_off_arg = sys.argv[1]

# if argument is not 0 and not 1, write value to brightness_variable.txt file
if(int(on_off_arg) != 0) and (int(on_off_arg) != 1):
    f = open("brightness_variable.txt","w+")
    f.write(on_off_arg)
    f.close()

# if argument is either 0 or 1 write variable to on_off_variable.txt file
elif(int(on_off_arg) == 0) or (int(on_off_arg) == 1):
    f = open("on_off_variable.txt","w+")
    f.write(on_off_arg)
    f.close()
