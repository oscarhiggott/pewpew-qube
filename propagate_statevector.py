import pew
from aether import QuantumCircuit, simulate

'''
Q
'''

def propagate_statevector(vec,qc):
    """
    take an initial statevector 'vec', initialize
    a circuit with this statevector, execute the
    quantum circuit 'qc' on it and return the new
    statevector
    """
    qc_i = QuantumCircuit(2,2)
    qc_i.initialize(vec)

    return simulate(qc_i + qc, get='statevector')
### to check the propagate_statevector function, 
### execute the following block:
#statevector = [[0.0,0.0],[1.0,0.0],[0.0,0.0],[0.0,0.0]]
#
#print ("initial state:")
#print (statevector)
#
#qc = QuantumCircuit(2,2)
#qc.x(0)
#
#state = propagate_statevector(statevector, qc)
#print ("final state:")
#print (state)

