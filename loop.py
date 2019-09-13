import pew
from aether import QuantumCircuit, simulate

'''
Q
'''
#class instruction_set_H_CX:
#    def __init__(self):
#        pass
#    
#    def key_pressed(self, key, screen):
#        print (key)
#        return screen
#
#    def initialization():
#        pass

final_screen = pew.Pix.from_iter((
    (1,0,0,0,0,0,0,1),
    (0,2,0,0,0,0,2,0),
    (0,0,3,0,0,3,0,0),
    (0,0,0,3,3,0,0,0),
    (0,0,0,3,3,0,0,0),
    (0,0,3,0,0,3,0,0),
    (0,2,0,0,0,0,2,0),
    (1,0,0,0,0,0,0,1),
))

    

def main_loop(ins):
    """
    main loop of the program. Takes an instruction
    set and calls it iteratively to process the
    pushed buttons and update the display.
    Button 'O' exits the loop
    """
    # initialize PewPew console
    pew.init()
    screen = pew.Pix()
    
    # flags used throughout the loop
    bool_loop = True
    keys      = 0 
    old_keys  = 0
    
    while bool_loop:
        # get the pressed keys
        keys = pew.keys()
    
        if keys != 0 and keys != old_keys:
            # update the history
            old_keys = keys
    
            # dispatch the pushed buttons
            if keys & pew.K_X:
                value = pew.K_X
            elif keys & pew.K_DOWN:
                value = pew.K_DOWN
            elif keys & pew.K_LEFT:
                value = pew.K_LEFT
            elif keys & pew.K_RIGHT:
                value = pew.K_RIGHT
            elif keys & pew.K_UP:
                value = pew.K_UP
            elif keys & pew.K_O:
                value = pew.K_O
                bool_loop = False
    
            # call instruction set here
            screen = ins.key_pressed(value, screen)
    
        elif keys == 0:
            # this is necessary to be able to push 
            # a button twice in a row
            old_keys = keys
    
        # update the screen and wait for 100ms
        pew.show(screen) 
        pew.tick(0.1)
        
    # the program has been terminated. 
    # display the final state
    pew.show(final_screen)
