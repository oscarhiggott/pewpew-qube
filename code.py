from loop import main_loop
# from instruction_sets import InstructionSet
# from goal_displays import QISKIT, IBMQ
from rotations import instruction_set_XYZ


if __name__ == "__main__":
    ins = instruction_set_XYZ()

    main_loop(ins)
