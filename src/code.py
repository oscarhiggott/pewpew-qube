import random
import time
import pew


if __name__ == "__main__":
    qiskit_images = (
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
        )
    )
    i = 0
    value = 0
    pew.init()
    while not value:
        keys = pew.keys()
        if keys & pew.K_UP:
            value = 1
        elif keys & pew.K_RIGHT:
            value = 2
        elif keys & pew.K_DOWN:
            value = 3
        elif keys & pew.K_LEFT:
            value = 4

        animation = (0,0,1,1,2,2,3,3,2,2,1,1)
        i = (i + 1) % len(animation)
        screen = qiskit_images[animation[i]]
        pew.show(pew.Pix.from_iter(screen))
        pew.tick(0.1)

    while pew.keys():
        pew.tick(0.1)

    random.seed(int(time.monotonic()*1000))
    del qiskit_images
    from loop import main_loop
    if value == 1:
        from rotations import instruction_set_XYZ
        main_loop(instruction_set_XYZ())
    else:
        from instruction_sets import InstructionSet
        from displays import IBMQ
        main_loop(InstructionSet(level=value-2, goal=IBMQ))
