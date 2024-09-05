#!/usr/bin/python3
import sys
import os
# Print only the script name
print(os.path.basename(sys.argv[0]))
# Print the remaining arguments
for i in range(1, len(sys.argv)):
    print(sys.argv[i])
