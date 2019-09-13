import pew


OFFSETS = ((0, 0), (4, 0), (0, 4), (4, 4))


def update(values, previous):
    output = pew.Pix()
    for (x_off, y_off), (shift, rot) in zip(OFFSETS, values):
        for y in range(4):
            for x in range(4):
                a, b = x, y
                for i in range(rot):
                    a, b = 3 - b, a
                b = (b + shift) % 4
                output.pixel(a + x_off, b + y_off,
                             previous.pixel(x + x_off, y + y_off))
    return output


def wait_for_key():
    keys = 0
    while not keys:
        keys = pew.keys()
        pew.tick(0.1)
    while pew.keys():
        pew.tick(0.1)
    return keys


pew.init()
screen = pew.Pix()
screen.pixel(0, 0, 3)
screen.pixel(4, 4, 3)
screen.pixel(0, 4, 3)
screen.pixel(4, 0, 3)

while True:
    pew.show(screen)
    keys = wait_for_key()
    if keys & pew.K_O:
        values = [[1, 0], [0, 0], [0, 0], [0, 0]]
    if keys & pew.K_X:
        values = [[0, 1], [0, 0], [0, 0], [0, 0]]
    screen = update(values, screen)
