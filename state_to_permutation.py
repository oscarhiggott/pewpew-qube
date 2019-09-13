from math import atan

from aether import QuantumCircuit, simulate

pi = 3.141592653589793

PERM_MAP = {
    0: 0,
    -1: 1,
    -2: 2,
    2: 2,
    1: 3
}


def complex_to_polar(x, y):
    theta = None
    try:
        theta = atan(y/x)
    except ZeroDivisionError:
        if y == 0.:
            theta = 0.
        elif y > 0.:
            theta = atan(float('Inf'))
        elif y < 0.:
            theta = atan(float('-Inf'))
    return (x**2 + y**2)**0.5, theta


def statevector_to_polarvector(state):
    return [complex_to_polar(*e) for e in state]


def polar_to_permindices(r, theta):
    b = round(theta*2/pi)
    return round(r**2/0.25), PERM_MAP[b]


def polarvector_to_permindices(polarvector):
    return [polar_to_permindices(r, theta) for r, theta in polarvector]


def state_to_permindices(state):
    polarvector = statevector_to_polarvector(state)
    return polarvector_to_permindices(polarvector)


if __name__ == '__main__':
    qc = QuantumCircuit(2,2)
    qc.h(0)
    qc.h(1)
    state = simulate(qc, get='statevector')
    print(state_to_permindices(state))
