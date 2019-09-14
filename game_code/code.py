from loop import main_loop
from rotations import instruction_set_XYZ

#TODO:
# * get different seed for each random number generator
# * merge all instruction sets

ins = instruction_set_XYZ()

main_loop(ins)
