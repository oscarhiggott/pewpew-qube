from loop import main_loop
from instruction_sets import InstructionSet


if __name__ == "__main__":
    ins = InstructionSet(level=2)

    main_loop(ins)
