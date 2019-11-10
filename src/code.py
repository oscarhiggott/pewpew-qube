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
    i = 0      # frame counter
    value = 0  # holds the selected level (0 = none)
    pew.init() # initialize the PewPew console

    while not value:
        # check for pressed keys
        keys = pew.keys()
        if keys & pew.K_UP:
            value = 1
        elif keys & pew.K_RIGHT:
            value = 2
        elif keys & pew.K_DOWN:
            value = 3
        elif keys & pew.K_LEFT:
            value = 4
        
        # display the next frame of the animation
        animation = (0,0,1,1,2,2,3,3,2,2,1,1)
        i = (i + 1) % len(animation)
        screen = qiskit_images[animation[i]]
        pew.show(pew.Pix.from_iter(screen))

        # wait 0.1 seconds
        pew.tick(0.1)

    # freeze the screen while a button is pressed
    while pew.keys():
        pew.tick(0.1)

    # initialize the random-number generator
    random.seed(int(time.monotonic()*1000))

    # unload unnecessary objects to save RAM
    del qiskit_images

    # load the new main loop
    from loop import main_loop

    # execute the new main loop passing to it the selected level
    if value == 1:
        from rotations import instruction_set_XYZ
        main_loop(instruction_set_XYZ())
    else:
        from instruction_sets import InstructionSet
        from displays import IBMQ
        main_loop(InstructionSet(level=value-2, goal=IBMQ))
