import pew


"""
THIS IS THE GENERAL STRUCTURE OF AN INSTRUCTION SET
class instruction_set_H_CX:
   def __init__(self):
       self.state = <initial_state>

   def key_pressed(self, key):
       # Update self.state here
       
   def get_current_screen(self):
       # Calculate screen using current self.state
       return screen
"""

start_screen_1 = pew.Pix.from_iter((
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,3,3,0,0,0),
    (0,0,0,3,3,0,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
))

start_screen_2 = pew.Pix.from_iter((
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,3,3,3,3,0,0),
    (0,0,3,2,2,3,0,0),
    (0,0,3,2,2,3,0,0),
    (0,0,3,3,3,3,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
))

start_screen_3 = pew.Pix.from_iter((
    (0,0,0,0,0,0,0,0),
    (0,3,3,3,3,3,3,0),
    (0,3,2,2,2,2,3,0),
    (0,3,2,1,1,2,3,0),
    (0,3,2,1,1,2,3,0),
    (0,3,2,2,2,2,3,0),
    (0,3,3,3,3,3,3,0),
    (0,0,0,0,0,0,0,0),
))

start_screen_4 = pew.Pix.from_iter((
    (3,3,3,3,3,3,3,3),
    (3,2,2,2,2,2,2,3),
    (3,2,1,1,1,1,2,3),
    (3,2,1,0,0,1,2,3),
    (3,2,1,0,0,1,2,3),
    (3,2,1,1,1,1,2,3),
    (3,2,2,2,2,2,2,3),
    (3,3,3,3,3,3,3,3),
))

final_screen_1 = pew.Pix.from_iter((
    (1,0,0,0,0,0,0,1),
    (0,2,0,0,0,0,2,0),
    (0,0,3,0,0,3,0,0),
    (0,0,0,3,3,0,0,0),
    (0,0,0,3,3,0,0,0),
    (0,0,3,0,0,3,0,0),
    (0,2,0,0,0,0,2,0),
    (1,0,0,0,0,0,0,1),
))
final_screen_2 = pew.Pix.from_iter((
    (0,0,0,0,0,0,0,0),
    (0,1,0,0,0,0,1,0),
    (0,0,2,0,0,2,0,0),
    (0,0,0,3,3,0,0,0),
    (0,0,0,3,3,0,0,0),
    (0,0,2,0,0,2,0,0),
    (0,1,0,0,0,0,1,0),
    (0,0,0,0,0,0,0,0),
))
final_screen_3 = pew.Pix.from_iter((
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,1,0,0,1,0,0),
    (0,0,0,2,2,0,0,0),
    (0,0,0,2,2,0,0,0),
    (0,0,1,0,0,1,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
))
final_screen_4 = pew.Pix.from_iter((
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,1,1,0,0,0),
    (0,0,0,1,1,0,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
))
final_screen_5 = pew.Pix.from_iter((
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
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

    # Load start screens
    pew.show(start_screen_1)
    pew.tick(0.2)
    pew.show(start_screen_2)
    pew.tick(0.2)
    pew.show(start_screen_3)
    pew.tick(0.2)
    pew.show(start_screen_4)
    pew.tick(0.2)
    pew.show(final_screen_5)
    pew.tick(0.5)
    # pew.show(ins.goal_screen)
    # pew.tick(1)
    
    # initialization stage
    pew.show(ins.get_current_screen())

    # flags used throughout the loop
    bool_loop = True
    old_keys = 0
    
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
                break
            else:
                value = 0

            ins.key_pressed(value)
    
        elif keys == 0:
            # this is necessary to be able to push 
            # a button twice in a row
            old_keys = keys
    
        # update the screen and wait for 100ms
        pew.show(ins.get_current_screen())
        pew.tick(0.05)
        
    # the program has been terminated. 
    # display the final sequence
    pew.show(final_screen_1)
    pew.tick(0.2)
    pew.show(final_screen_2)
    pew.tick(0.2)
    pew.show(final_screen_3)
    pew.tick(0.2)
    pew.show(final_screen_4)
    pew.tick(0.2)
    pew.show(final_screen_5)
    pew.tick(0.2)
