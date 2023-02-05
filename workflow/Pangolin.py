import os
import sys

print("first argument is the input file, second argument is output file")
temp=sys.argv
print(sys.argv)
execstr=""
if len(temp)>1:
    execstr = execstr+"pangolin " + temp[1]
    if len(temp)>2:
        execstr=execstr + " --outfile " + temp[2]
print(execstr)
result=os.system(execstr)
print(result)
