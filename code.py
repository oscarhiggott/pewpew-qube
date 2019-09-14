import random
import time
import pew


if __name__ == "__main__":

    qiskit_images = [
        (
            (0, 3, 3, 3, 3, 3, 3, 0),
            (3, 2, 0, 1, 1, 0, 0, 3),
            (3, 0, 2, 0, 0, 1, 0, 3),
            (3, 1, 0, 2, 0, 0, 1, 3),
            (3, 3, 0, 0, 2, 0, 3, 3),
            (3, 0, 3, 3, 3, 3, 0, 3),
            (3, 0, 0, 0, 0, 0, 2, 3),
            (0, 3, 3, 3, 3, 3, 3, 0)
        ),
        (
            (0, 3, 3, 3, 3, 3, 3, 0),
            (3, 0, 0, 2, 1, 0, 0, 3),
            (3, 0, 1, 2, 0, 1, 0, 3),
            (3, 1, 0, 0, 2, 0, 1, 3),
            (3, 3, 0, 0, 2, 0, 3, 3),
            (3, 0, 3, 3, 3, 3, 0, 3),
            (3, 0, 0, 0, 0, 2, 0, 3),
            (0, 3, 3, 3, 3, 3, 3, 0)
        ),
        (
            (0, 3, 3, 3, 3, 3, 3, 0),
            (3, 0, 0, 1, 2, 0, 0, 3),
            (3, 0, 1, 0, 2, 1, 0, 3),
            (3, 1, 0, 2, 0, 0, 1, 3),
            (3, 3, 0, 2, 0, 0, 3, 3),
            (3, 0, 3, 3, 3, 3, 0, 3),
            (3, 0, 2, 0, 0, 0, 0, 3),
            (0, 3, 3, 3, 3, 3, 3, 0)
        ),
        (
            (0, 3, 3, 3, 3, 3, 3, 0),
            (3, 0, 0, 1, 1, 0, 2, 3),
            (3, 0, 1, 0, 0, 2, 0, 3),
            (3, 1, 0, 0, 2, 0, 1, 3),
            (3, 3, 0, 2, 0, 0, 3, 3),
            (3, 0, 3, 3, 3, 3, 0, 3),
            (3, 2, 0, 0, 0, 0, 0, 3),
            (0, 3, 3, 3, 3, 3, 3, 0)
        )]

    loop = True
    i = 0
    pew.init()
    while loop:
        keys = pew.keys()
        keys &= ~(pew.K_X | pew.K_O)
        if keys != 0:
            if keys & pew.K_UP:
                value = 0
            elif keys & pew.K_RIGHT:
                value = 1
            elif keys & pew.K_DOWN:
                value = 2
            elif keys & pew.K_LEFT:
                value = 3
            break

        animation = (0,1,2,3,2,1)
        i = (i + 1) % 6
        screen = qiskit_images[animation[i]]
        pew.show(pew.Pix.from_iter(screen))
        pew.tick(0.1)

    random.seed(int(time.monotonic()*1000))
    from loop import main_loop
    if value == 0:
        from rotations import instruction_set_XYZ
        main_loop(instruction_set_XYZ())
    else:
        from instruction_sets import InstructionSet
        from goal_displays import IBMQ
        if value == 1:
            main_loop(InstructionSet(level=0, goal=IBMQ))
        elif value == 2:
            main_loop(InstructionSet(level=1, goal=IBMQ))
        elif value == 3:
            main_loop(InstructionSet(level=2, goal=IBMQ))
