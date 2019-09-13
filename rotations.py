import pew
from aether import QuantumCircuit
from math import pi, atan2, sqrt
from propagate_statevector import propagate_statevector
from random import randint

pi4 = 0.785398
pi2 = 1.570796
#pi  = 3.141593

def make_circuit(gate):
    qc = QuantumCircuit(2)
    
    if gate[0] == 'x':
        qc.h(0)
    elif gate[0] == 'y':
        qc.rx(pi2,0)
    
    if gate[1] == 'x':
        qc.h(1)
    elif gate[1] == 'y':
        qc.rx(pi2,1)
    
    qc.cx(0,1)
    qc.h(1)
    qc.rx(pi2,1) # for XX and YY and ZZ: pi/2.
    qc.h(1)
    qc.cx(0,1)
    
    if gate[0] == 'x':
        qc.h(0)
    elif gate[0] == 'y':
        qc.rx(-pi2,0)
    
    if gate[1] == 'x':
        qc.h(1)
    elif gate[1] == 'y':
        qc.rx(-pi2,1)
    
    return qc


def rot90(block):
    res = []
    for i in range(len(block)):
        transposed = []
        for col in block:
            transposed.append(col[i])
        transposed.reverse()
        res.append(transposed)
    return res


def make_block(c_num):
    amp = sqrt(c_num[0]*c_num[0] + c_num[1]*c_num[1])
    phi = atan2(c_num[1], c_num[0])
    
    if amp < 0.01:
       phi = 0
    
    scenario  = 0
    phases    = [0.0, pi4, -pi4, 2.0*pi4, -2.0*pi4, 3.0*pi4, -3.0*pi4, 4.0*pi4, -4.0*pi4]
    scenarios = [1,  -1,   -2,   4,        2,      -4,       -3,       3,        3      ]
    for i in range(9):
        if (phi - phases[i])*(phi - phases[i]) < 0.001:
            scenario = scenarios[i]
            continue
#    print ("phi",phi, "scenario", scenario)
    
    if amp < 0.25:
        block = [[0,0,0,0],[0,2,2,0],[0,2,2,0],[0,0,0,0]]
    elif amp < 0.6:
        if scenario > 0:
            block = [[0,0,2,0],[0,0,0,2],[0,0,0,2],[0,0,2,0]]
        else:
            block = [[0,0,0,0],[0,2,2,0],[0,0,2,0],[0,0,0,0]]
    elif amp < 0.9:
        if scenario > 0:
            block = [[0,0,0,2],[0,0,2,0],[0,0,2,0],[0,0,0,2]]
        else:
            block = [[0,0,2,0],[0,0,2,2],[0,0,0,0],[0,0,0,0]]
    else:
        if scenario > 0:
            block = [[0,0,0,2],[0,0,0,2],[0,0,0,2],[0,0,0,2]]
        else:
            block = [[0,0,2,2],[0,0,0,2],[0,0,0,0],[0,0,0,0]]
    
    if scenario != 1 and scenario != -1:
        for r in range(abs(scenario) - 1):
            block = rot90(block)
#    if amp < 0.25:
#        block = [[0,0,0,0],[0,2,2,0],[0,2,2,0],[0,0,0,0]]
#    elif amp < 0.6:
#        block = [[0,0,2,0],[0,0,0,2],[0,0,0,2],[0,0,2,0]]
#    elif amp < 0.9:
#        block = [[0,0,0,2],[0,0,2,0],[0,0,2,0],[0,0,0,2]]
#    else:
#        block = [[0,0,0,2],[0,0,0,2],[0,0,0,2],[0,0,0,2]]
#    
#    if 1.4 < phi < 1.7:
#        block = rot90(block)
#        block = rot90(block)
#        block = rot90(block)
#    elif 3. < phi < 3.2 or -3. > phi > -3.2:
#        block = rot90(block)
#        block = rot90(block)
#    elif -1.5 > phi > -1.7:
#        block = rot90(block)
    
    return block


def make_image(state):
    blocks = []
    for num in state:
        blocks.append(make_block(num))
    
    image = pew.Pix()
    
    for i in range(2):
        for j in range(4):
            tmp = blocks[2*i][j] + blocks[2*i+1][j]
            for x in range(8):
                image.pixel(x,4*i+j,tmp[x])
    
    return image 


def random_state():
    qc = QuantumCircuit(2)
    state = [[1.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0]]
    
    for i in range(5):
        gate = ['xx','xy','xz','yx','yz','yy','zx','zy','zz'][randint(0,8)]
        qc = make_circuit(gate)
        state = propagate_statevector(state, qc)
    print("random state", state)
    return state


class instruction_set_XYZ:
    def __init__(self):
        self.key_hist = []
        self.state = [[1.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0]]


    def key_pressed(self, key, screen):
        if key == pew.K_UP:
            self.key_hist = []
        elif key == pew.K_LEFT or key == pew.K_DOWN or key == pew.K_RIGHT:
            self.key_hist.append(key)
            if len(self.key_hist) == 2:
                if self.key_hist[0] == pew.K_LEFT:
                    gate = 'x'
                elif self.key_hist[0] == pew.K_DOWN:
                    gate = 'y'
                else:
                    gate = 'z'
                
                if self.key_hist[1] == pew.K_LEFT:
                    gate = gate + 'x'
                elif self.key_hist[1] == pew.K_DOWN:
                    gate = gate + 'y'
                else:
                    gate = gate + 'z'

                self.state = propagate_statevector(self.state, make_circuit(gate))
                print ("new state", self.state)
                screen = make_image(self.state)
                self.key_hist = []
        elif key == pew.K_X:
            self.__init__()
            screen = self.initialization(screen)

        return screen


    def initialization(self,screen):
        self.state = random_state()
        screen = make_image(self.state)

        return screen
    
    
    
    
    
    
    
    
    
    
    
    
    
