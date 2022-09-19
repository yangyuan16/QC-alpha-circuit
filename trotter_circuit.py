#
# 1) The evolution operator is decomposed into trotter slices,
#    and then the circuit is evolved by trotter decomposition evolution
#    Note: trotter slice is also decomposed as a series of Quantum Gates!
# 2) Obtain the the quantum gate decomposition form of  trotter evolution operator slice
#    corresponding to different magnetic fields is obtained
#==========================================================================
#
import numpy as np
import scipy
from scipy.linalg import expm
from qiskit.quantum_info import Operator
from qiskit import  QuantumCircuit, QuantumRegister, ClassicalRegister
import matplotlib.pyplot as plt
import library.Hamiltonian as libH
#
if __name__ == '__main__':
    dt = 0.1
    hx = np.arange(0, 1, 0.1)
    Hxx, Hyy, Hzz, Hmx, Hmz = libH.heisenberg_2body()
    Is_plot_circuit = True
    U = []
    for it in range(len(hx)):
        H = Hxx + Hyy + Hzz - hx[it] * Hmx
        U0 = expm(-1j * dt * H)
        U.append(expm(-1j * dt * H))
        Q = QuantumRegister(2)
        C = ClassicalRegister(2)
        circuit = QuantumCircuit(Q, C)
        U_gate = Operator(U0)
        circuit.unitary(U_gate, [0, 1])
        circuit.measure([0, 1], [0, 1])
        if Is_plot_circuit is True:
            circuit.draw(output='mpl')
            plt.title('hx=%g' % hx[it])
            plt.show()
            circuit.decompose().draw(output='mpl')
            plt.title('hx=%g_dt=%g' % (hx[it], dt))
            plt.show()
