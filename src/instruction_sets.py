import random
from aether import QuantumCircuit, simulate
import pew

from displays import IBMQ
from permute_screen import update, state_to_permindices
from propagate_statevector import propagate_statevector


ALL_GATES = {
    pew.K_UP: ('x', 0),
    pew.K_DOWN: ('x', 1),
    pew.K_LEFT: ('h', 0),
    pew.K_RIGHT: ('h', 1),
    pew.K_X: ('cx', 1)
}

X_CNOT_GATES = {
    pew.K_UP: ('x', 0),
    pew.K_DOWN: ('x', 1),
    pew.K_X: ('cx', 1)
}

H_CNOT_GATES = {
    pew.K_LEFT: ('h', 0),
    pew.K_RIGHT: ('h', 1),
    pew.K_X: ('cx', 1)
}

LEVELS = {
    0: {
        'gates': X_CNOT_GATES,
        'length': 3
    },
    1: {
        'gates': H_CNOT_GATES,
        'length': 11
    },
    2: {
        'gates': ALL_GATES,
        'length': 11
    }
}


class InstructionSet:
    def __init__(self, level=0, goal=IBMQ):
        self.goal_screen = update(((1,0),(0,0),(0,0),(0,0)),
                           pew.Pix.from_iter(goal))
        self.length = LEVELS[level]['length']
        self.gates = LEVELS[level]['gates']
        self.state = self.get_random_initial_state()

    def get_random_initial_state(self):
        qc = QuantumCircuit(2, 0)
        qc.data = [random.choice(list(self.gates.values())) for _ in range(self.length)]
        return simulate(qc, get='statevector')

    def get_current_screen(self):
        return update(state_to_permindices(self.state),
                      self.goal_screen)

    def key_pressed(self, key):
        key &= ~0x20
        if key not in self.gates:
            return
        qc = QuantumCircuit(2, 0)
        qc.data.append(self.gates[key])
        self.state = propagate_statevector(self.state, qc)
