#**********************
# Modules & Packages
#********************

# Module = Python code file = Has Functions, Classes, Variables = Runnable code.
# Reuse the existing modules more efficiently

import os  # os is a module
os.listdir() # listing all the files in the current directory.
dir(os) # gives all the classes, functions, modules, sub modules -> gives list of files inside it.

os?  # gives the help about os
os ?? # gives much more detail help
help(os)
help() -> quit # for comeout of the help mode use quit command.

os.__file__ # gives the os.py location in your machine

sqrt(4) # gives an error 
math.sqrt(4) # gives an error 

import math # math is a module -> If you want to access any mathematical functions, we need to import math module. Otherwise it will give errors.
math.sqrt(4) # give 2 now.
sqrt(4) # gives error again bcs

from math import * # This will solve all the problems of accessing math functions. After this statement, you can directly access any math function.
from math import sqrt # This also we can use, it accepts only sqrt functions.
sqrt(4) # gives 2 now.

dir(math) # gives all the mathematical functions.



































