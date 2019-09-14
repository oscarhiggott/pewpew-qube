import pew

images = [pew.Pix.from_iter((
    (0, 3, 3, 3, 3, 3, 3, 0),
    (3, 2, 0, 1, 1, 0, 0, 3),
    (3, 0, 2, 0, 0, 1, 0, 3),
    (3, 1, 0, 2, 0, 0, 1, 3),
    (3, 3, 0, 0, 2, 0, 3, 3),
    (3, 0, 3, 3, 3, 3, 0, 3),
    (3, 0, 0, 0, 0, 0, 2, 3),
    (0, 3, 3, 3, 3, 3, 3, 0)
)),

pew.Pix.from_iter((
    (0, 3, 3, 3, 3, 3, 3, 0),
    (3, 0, 0, 2, 1, 0, 0, 3),
    (3, 0, 1, 2, 0, 1, 0, 3),
    (3, 1, 0, 0, 2, 0, 1, 3),
    (3, 3, 0, 0, 2, 0, 3, 3),
    (3, 0, 3, 3, 3, 3, 0, 3),
    (3, 0, 0, 0, 0, 2, 0, 3),
    (0, 3, 3, 3, 3, 3, 3, 0)
)),

pew.Pix.from_iter((
    (0, 3, 3, 3, 3, 3, 3, 0),
    (3, 0, 0, 1, 2, 0, 0, 3),
    (3, 0, 1, 0, 2, 1, 0, 3),
    (3, 1, 0, 2, 0, 0, 1, 3),
    (3, 3, 0, 2, 0, 0, 3, 3),
    (3, 0, 3, 3, 3, 3, 0, 3),
    (3, 0, 2, 0, 0, 0, 0, 3),
    (0, 3, 3, 3, 3, 3, 3, 0)
)),

pew.Pix.from_iter((
    (0, 3, 3, 3, 3, 3, 3, 0),
    (3, 0, 0, 1, 1, 0, 2, 3),
    (3, 0, 1, 0, 0, 2, 0, 3),
    (3, 1, 0, 0, 2, 0, 1, 3),
    (3, 3, 0, 2, 0, 0, 3, 3),
    (3, 0, 3, 3, 3, 3, 0, 3),
    (3, 2, 0, 0, 0, 0, 0, 3),
    (0, 3, 3, 3, 3, 3, 3, 0)
))]


loop = True
screen = images[0]
i = 0
pew.init()
while loop:
    pew.show(screen)
    keys      = 0 
    if keys != 0:
        if keys & pew.K_DOWN:
            value = pew.K_DOWN
            loop = False
        elif keys & pew.K_LEFT:
            value = pew.K_LEFT
            loop = False
        elif keys & pew.K_RIGHT:
            value = pew.K_RIGHT
            loop = False
        elif keys & pew.K_UP:
            value = pew.K_UP
            loop = False
    
    i += 0.05
    if i == 0:
        screen = images[0]
    elif i == 1:
        screen = images[1]
    elif i == 2:
        screen = images[2]
    elif i == 3:
        screen = images[3]
    elif i == 4:
        screen = images[2]
    elif i == 5:
        screen = images[1]
    elif i == 6:
        i = 0
    
    pew.tick(0.02)
while pew.keys:
    pew.tick(0.02)
    
if value == pew.K_UP:
    from loop      import main_loop
    from rotations import instruction_set_XYZ
    
    main_loop(instruction_set_XYZ())
elif value == pew.K_LEFT:
    pass
elif value == pew.K_DOWN:
    pass
elif value == pew.K_RIGHT:
    pass


























