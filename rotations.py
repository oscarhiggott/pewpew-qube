import pew
from aether import QuantumCircuit, execute
from math import pi

pew.init()
screen = pew.Pix()

qc = QuantumCircuit(2)

gate = 'xx'

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

