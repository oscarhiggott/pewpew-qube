QISKIT = (
    (0, 3, 3, 3, 3, 3, 3, 0),
    (3, 2, 0, 1, 1, 0, 0, 3),
    (3, 0, 2, 0, 0, 0, 0, 3),
    (3, 1, 0, 2, 0, 0, 1, 3),
    (3, 3, 0, 0, 2, 0, 3, 3),
    (3, 0, 3, 3, 3, 3, 0, 3),
    (3, 0, 0, 0, 0, 0, 2, 3),
    (0, 3, 3, 3, 3, 3, 3, 0)
)

IBMQ = (
    (1, 1, 1, 3, 3, 1, 1, 1),
    (1, 1, 3, 3, 3, 3, 1, 1),
    (1, 3, 3, 0, 0, 3, 3, 1),
    (1, 3, 3, 0, 0, 3, 3, 1),
    (1, 1, 3, 3, 3, 3, 1, 1),
    (1, 1, 1, 3, 3, 1, 1, 1),
    (1, 1, 1, 3, 3, 3, 1, 1),
    (1, 1, 1, 3, 3, 3, 1, 1)
)

BLANK = (
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
)

start_screens = ((
                         (0, 0, 0, 0, 0, 0, 0, 0),
                         (0, 0, 0, 0, 0, 0, 0, 0),
                         (0, 0, 0, 0, 0, 0, 0, 0),
                         (0, 0, 0, 3, 3, 0, 0, 0),
                         (0, 0, 0, 3, 3, 0, 0, 0),
                         (0, 0, 0, 0, 0, 0, 0, 0),
                         (0, 0, 0, 0, 0, 0, 0, 0),
                         (0, 0, 0, 0, 0, 0, 0, 0)
                     ),
                     (
                         (0, 0, 0, 0, 0, 0, 0, 0),
                         (0, 0, 0, 0, 0, 0, 0, 0),
                         (0, 0, 3, 3, 3, 3, 0, 0),
                         (0, 0, 3, 2, 2, 3, 0, 0),
                         (0, 0, 3, 2, 2, 3, 0, 0),
                         (0, 0, 3, 3, 3, 3, 0, 0),
                         (0, 0, 0, 0, 0, 0, 0, 0),
                         (0, 0, 0, 0, 0, 0, 0, 0)
                     ),
                     (
                         (0, 0, 0, 0, 0, 0, 0, 0),
                         (0, 3, 3, 3, 3, 3, 3, 0),
                         (0, 3, 2, 2, 2, 2, 3, 0),
                         (0, 3, 2, 1, 1, 2, 3, 0),
                         (0, 3, 2, 1, 1, 2, 3, 0),
                         (0, 3, 2, 2, 2, 2, 3, 0),
                         (0, 3, 3, 3, 3, 3, 3, 0),
                         (0, 0, 0, 0, 0, 0, 0, 0)
                     ),
                     (
                         (3, 3, 3, 3, 3, 3, 3, 3),
                         (3, 2, 2, 2, 2, 2, 2, 3),
                         (3, 2, 1, 1, 1, 1, 2, 3),
                         (3, 2, 1, 0, 0, 1, 2, 3),
                         (3, 2, 1, 0, 0, 1, 2, 3),
                         (3, 2, 1, 1, 1, 1, 2, 3),
                         (3, 2, 2, 2, 2, 2, 2, 3),
                         (3, 3, 3, 3, 3, 3, 3, 3)
                     ))

final_screens = ((
    (1,0,0,0,0,0,0,1),
    (0,2,0,0,0,0,2,0),
    (0,0,3,0,0,3,0,0),
    (0,0,0,3,3,0,0,0),
    (0,0,0,3,3,0,0,0),
    (0,0,3,0,0,3,0,0),
    (0,2,0,0,0,0,2,0),
    (1,0,0,0,0,0,0,1),
),
                 (
    (0,0,0,0,0,0,0,0),
    (0,1,0,0,0,0,1,0),
    (0,0,2,0,0,2,0,0),
    (0,0,0,3,3,0,0,0),
    (0,0,0,3,3,0,0,0),
    (0,0,2,0,0,2,0,0),
    (0,1,0,0,0,0,1,0),
    (0,0,0,0,0,0,0,0),
),
                 (
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,1,0,0,1,0,0),
    (0,0,0,2,2,0,0,0),
    (0,0,0,2,2,0,0,0),
    (0,0,1,0,0,1,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
),
                 (
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,1,1,0,0,0),
    (0,0,0,1,1,0,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
))
