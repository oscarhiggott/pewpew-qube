import pew
from aether import QuantumCircuit
from math import pi, atan2
from propagate_statevector import propagate_statevector
from random import randint

pew.init()
screen = pew.Pix()

def make_circuit(gate):
    qc = QuantumCircuit(2)
    
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

def rot90(block):
    return list(zip(*reversed(block)))

def make_block(c_num):
    amp, phi = (abs(c_num), atan2(c_num.imag, c_num.real))
    
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
        block = rot90(block)
    elif 3< phi < 3.2:
        block = rot90(block)
        block = rot90(block)
    elif -1.5 > phi > -1.7:
        block = rot90(block)
        block = rot90(block)
        block = rot90(block)
    
    return block

def make_image(state):
    blocks = []
    for num in state:
        blocks.append(make_block(num[0] + num[1]*1j))
    
    image = []
    
    for i in range(2):
        for j in range(4):
            image.append(blocks[2*i][j] + blocks[2*i+1][j])
    
    return tuple(tuple(x) for x in image)

def random_state():
    
    qc = QuantumCircuit(2)
    
    for i in range(5):
    
        gate = ['xx','xy','xz','yx','yz','yy','zx','zy','zz'][randint(0,9)]
    
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
    
    state = [[1.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0]]
    return propagate_statevector(state, qc)
    
    
    
    
    
    
    
    
    
    
    
    
    
    