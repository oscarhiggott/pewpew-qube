RUBIK = (
    (0, 0, 0, 0, 3, 3, 3, 3),
    (0, 0, 0, 0, 3, 3, 3, 3),
    (0, 0, 0, 0, 3, 3, 3, 3),
    (0, 0, 0, 0, 3, 3, 3, 3),
    (2, 2, 2, 2, 1, 1, 1, 1),
    (2, 2, 2, 2, 1, 1, 1, 1),
    (2, 2, 2, 2, 1, 1, 1, 1),
    (2, 2, 2, 2, 1, 1, 1, 1)
)

QISKIT = (
    (0, 0, 2, 2, 2, 2, 0, 0),
    (0, 2, 0, 0, 0, 0, 2, 0),
    (2, 0, 3, 0, 0, 0, 0, 2),
    (2, 0, 0, 2, 0, 0, 0, 2),
    (2, 0, 0, 0, 2, 0, 0, 2),
    (2, 0, 0, 0, 0, 3, 0, 2),
    (0, 2, 0, 0, 0, 0, 2, 0),
    (0, 0, 2, 2, 2, 2, 0, 0)
)

IBMQ = (
    (0, 0, 0, 3, 3, 0, 0, 0),
    (0, 0, 3, 3, 3, 3, 0, 0),
    (0, 3, 3, 0, 0, 3, 3, 0),
    (0, 3, 3, 0, 0, 3, 3, 0),
    (0, 0, 3, 3, 3, 3, 0, 0),
    (0, 0, 0, 3, 3, 0, 0, 0),
    (0, 0, 0, 3, 3, 3, 0, 0),
    (0, 0, 0, 3, 3, 3, 0, 0)
)

if __name__ == "__main__":
    import pew
    pew.init()
    pew.show(pew.Pix.from_iter(RUBIK))
    pew.tick(1.)
    pew.show(pew.Pix.from_iter(QISKIT))
    pew.tick(1.)
    pew.show(pew.Pix.from_iter(IBMQ))
    while True:
        pass