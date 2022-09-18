#%%
# 1) show how to construct 5 qubits alpha circuit
# 2) show the result of measuring 1 qubit on 5-qubits alpha circuit
# 3) show the result of measuring 2 qubits on 5-qubits alpha circuit
#
from qiskit import QuantumCircuit,QuantumRegister,ClassicalRegister
from qiskit import execute, BasicAer
from qiskit.circuit import Parameter
import matplotlib.pylab as plt
import numpy as np
import library.circuit as libcir
#
theta = Parameter('theta')  # Define a global parameter theta, which is the control parameter of alpha_circuit
def alpha_circuit_construct(nq, nc, mq, mc, initial_state):
    n = nq  # qubits 数目
    nc = nc # c_bit 数目  nc 的数目必须按照严格线路设计时测量比特的数目写，否则会出现bug
    qc = QuantumCircuit(n,nc)
    mq = mq
    mc = mc
    #=================================
    # 固定不同的初态
    initial_state = initial_state
    for it in range(n):
        if initial_state[it] == 1:
            qc.x(it)
        else:
            qc.id(it)
    #===============================
    for it in range(n):
        qc.h(it)
    for i in range(n-1):
        qc.cx(i, i+1)
        qc.cx(i+1,i)
    qc.barrier()
    qc.rz(theta, range(n))
    qc.barrier()
    #
    for it in range(n):
        qc.h(it)
    qc.measure(mq,mc)
    return qc
#
def run_circuit(qc, theta_range, shots):
    # circuits = [qc.bind_parameters({theta: theta_val}) for theta_val in theta_range]
    job = execute(qc, backend=BasicAer.get_backend('qasm_simulator'),
                  parameter_binds=[{theta: theta_val} for theta_val in theta_range], shots=shots)
    counts = job.result().get_counts()
    return counts
#
def measure_1qubit(counts):
    count_0, count_1 = libcir.circjob_count_1q(counts)
    count_0_r = [count_0[it] / shots for it in range(len(count_0))]
    count_1_r = [count_1[it] / shots for it in range(len(count_1))]
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    # 画一个
    ax.plot(theta_range, count_0_r, '.-', label='0')
    ax.plot(theta_range, count_1_r, '.-', label='1')
    ax.set_xlabel('theta', fontsize=14)
    ax.set_ylabel('Counts', fontsize=14)
    ax.legend(fontsize=14)
    plt.show()
    return
#
def measure_2qubit(counts):
    count_00, count_10, count_01, count_11 = libcir.circjob_count_2q(counts)
    count_00_r = [count_00[it]/shots for it in range(len(count_00))]
    count_10_r = [count_10[it]/shots for it in range(len(count_10))]
    count_01_r = [count_01[it]/shots for it in range(len(count_01))]
    count_11_r = [count_11[it]/shots for it in range(len(count_11))]
    #
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    # 画一个
    ax.plot(theta_range, count_00_r, '.-', label='00', lw=1.5, color='blue', marker='o', markersize=3,
            markeredgewidth=1, markerfacecolor='blue')
    ax.plot(theta_range, count_10_r, '.-', label='01', lw=1.5, color='orange', marker='o', markersize=3,
            markeredgewidth=1, markerfacecolor='orange')  # 注意 IBM 的比特位默认从右往左读，所以这里需要调换一下
    ax.plot(theta_range, count_01_r, '.-', label='10', lw=1.5, color='green', marker='o', markersize=3,
            markeredgewidth=1, markerfacecolor='green')  # 注意 IBM 的比特位默认从右往左读，所以这里需要调换一下
    ax.plot(theta_range, count_11_r, '.-', label='11', lw=1.5, color='red', marker='o', markersize=3,
            markeredgewidth=1, markerfacecolor='red')
    ax.set_xlabel('theta', fontsize=14)
    ax.set_ylabel('Counts', fontsize=14)
    ax.legend(fontsize=14)
    plt.show()
    return
#========================================================
if __name__ == '__main__':
    # draw the 5-qubit circuit
    nq = 5  # number of qubits
    nc = 5  # number of classical bits
    mq = [0,1,2,3,4]
    mc = [0,1,2,3,4]
    initial_state = [0,0,0,0,0]
    qc = alpha_circuit_construct(nq=nq,nc=nc,mq=mq,mc=mc,initial_state=initial_state)
    qc.draw('mpl')
    plt.show()
    #
    # results of measuring 1 qubit
    nc = 1    # we need to reset nc = 1
    mc = [0]  # we need to reset mc = [0]
    mq = [0]  # we need to reset mq = [0]
    theta_range = np.linspace(0, 3, 100)
    shots = 1024
    qc_m1 = alpha_circuit_construct(nq=nq, nc=nc, mq=mq, mc=mc, initial_state=initial_state) # get circuit
    qc_m1.draw('mpl')
    plt.show()
    counts = run_circuit(qc=qc_m1, theta_range=theta_range, shots=shots)
    print(counts)
    measure_1qubit(counts=counts) # Plot the results of the case that measuring one qubit
    #
    # results of measuring 2 qubit
    nc = 2 # we need to reset nc = 2
    mc = [0, 1] # we need to reset mc = [0, 1]
    mq = [0, 1] # we need to reset mq = [0, 1]
    theta_range = np.linspace(0, 3, 100)
    shots = 1024
    qc_m2 = alpha_circuit_construct(nq=nq, nc=nc, mq=mq, mc=mc, initial_state=initial_state) # get circuit
    qc_m2.draw('mpl')
    plt.show()
    counts = run_circuit(qc=qc_m2, theta_range=theta_range, shots=shots)
    print(counts)
    measure_2qubit(counts=counts) # Plot the results of the case that measuring two qubits







