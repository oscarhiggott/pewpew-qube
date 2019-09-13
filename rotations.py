import pew
from aether import QuantumCircuit, execute
from math import pi
from propagate_statevector import propagate_statevector

pew.init()
screen = pew.Pix()

qc = QuantumCircuit(2)

gate = 'xx'

def make_circuit(gate):
    if gate[0] == 'x':
        qc.h(0)
    elif gate[0] == 'y':
        qc.rx(pi/2,0)
    
    if gate[1] == 'x':
        qc.h(1)
    elif gate[1] == 'y':
        qc.rx(pi/2,1)
    
    qc.cx(0,1)
    qc.h(1)
    qc.rx(pi)
    qc.h(1)
    qc.cx(0,1)
    
    if gate[0] == 'x':
        qc.h(0)
    elif gate[0] == 'y':
        qc.rx(-pi/2,0)
    
    if gate[1] == 'x':
        qc.h(1)
    elif gate[1] == 'y':
        qc.rx(-pi/2,1)
    
    return qc

def make_block(c_num):
    amp, phi = (abs(x), math.atan2(x.imag, x.real))
    
    if amp < 0.01:
        phi = 0
    
    if amp < 0.25:
        block = [[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]]
    elif amp < 0.6:
        block = [[0,0,0,0],[0,1,0,1],[0,1,0,1],[0,0,0,0]]
    elif amp < 0.9:
        block = [[0,0,0,1],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
    else:
        block = [[0,0,0,1],[0,0,0,1],[0,0,0,1],[0,0,0,1]]
    
    if 1.4 < phi < 1.7:
        block = np.rot90(block)
    elif 3< phi < 3.2:
        block = np.rot90(block)
        block = np.rot90(block)
    elif -1.5 > phi > -1.7:
        block = np.rot90(block)
        block = np.rot90(block)
        block = np.rot90(block)
    
    return block

def make_image(state):

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    