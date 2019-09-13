import random
from aether import QuantumCircuit, simulate
import pew

from goal_displays import IBMQ
from permute_screen import update, state_to_permindices
from propagate_statevector import propagate_statevector


GATES = {
    pew.K_UP: ('x', 0),
    pew.K_DOWN: ('x', 1),
    pew.K_LEFT: ('h', 0),
    pew.K_RIGHT: ('h', 1),
    pew.K_X: ('cx', 1)
}


class InstructionSet:
    def __init__(self, length=2):
        self.goal_screen = IBMQ
        self.length = length
        self.state = self.get_random_initial_state()

    def get_random_initial_state(self):
        qc = QuantumCircuit(2, 0)
        qc.data = [random.choice(list(GATES.values())) for _ in range(self.length)]
        return simulate(qc, get='statevector')

    def get_current_screen(self):
        return update(state_to_permindices(self.state),
                      pew.Pix.from_iter(self.goal_screen))

    def key_pressed(self, key):
        key &= ~0x20
        if key == 0:
            return
        qc = QuantumCircuit(2, 0)
        qc.data.append(GATES[key])
        self.state = propagate_statevector(self.state, qc)
