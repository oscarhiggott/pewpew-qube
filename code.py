from loop import main_loop
from instruction_sets import InstructionSet
from goal_displays import QISKIT, IBMQ


if __name__ == "__main__":
    ins = InstructionSet(level=0, goal=IBMQ)

    main_loop(ins)
