from aether import QuantumCircuit, simulate


def propagate_statevector(vec,qc):
    """
    Take an initial statevector 'vec', initialize
    a circuit with this statevector, execute the
    quantum circuit 'qc' on it and return the new
    statevector.
    """
    qc_i = QuantumCircuit(2,0)
    qc_i.initialize(vec)

    return simulate(qc_i + qc, get='statevector')
