#%%
# 1) show the result of measuring 3 qubits on 5-qubits alpha circuit
# 2) write the data to files in '.pr' format, which is useful for further analysis
#
from qiskit import QuantumCircuit,QuantumRegister,ClassicalRegister
from qiskit import execute, BasicAer
from qiskit.circuit import Parameter
import matplotlib.pylab as plt
import numpy as np
import library.circuit as libcir
from library.BasicFunctions import save_pr as save
from library.BasicFunctions import mkdir
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
def measure_3qubit(counts):
    count_000, count_100, count_010, count_110, count_001,count_101,count_011,count_111 = libcir.circjob_count_3q(counts)
    count_000_r = [count_000[it]/shots for it in range(len(count_000))]
    count_010_r = [count_010[it]/shots for it in range(len(count_010))]
    count_001_r = [count_001[it]/shots for it in range(len(count_001))]
    count_011_r = [count_011[it]/shots for it in range(len(count_011))]

    count_100_r = [count_100[it]/shots for it in range(len(count_100))]
    count_110_r = [count_110[it]/shots for it in range(len(count_110))]
    count_101_r = [count_101[it]/shots for it in range(len(count_101))]
    count_111_r = [count_111[it]/shots for it in range(len(count_111))]

    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111)
    # 画一个
    ax.plot(theta_range, count_000_r, '.-', label='000',color='blue',marker='o', markersize=10,
            markeredgewidth=1, markerfacecolor='blue') # 注意 IBM 的比特位默认从右往左读，所以这里需要调换一下
    ax.plot(theta_range, count_100_r, '.-', label='001',color='orange',marker='o', markersize=8,
            markeredgewidth=1, markerfacecolor='orange')
    ax.plot(theta_range, count_010_r, '.-', label='010',color='green',marker='o', markersize=6,
            markeredgewidth=1, markerfacecolor='green')
    ax.plot(theta_range, count_110_r, '.-', label='011',color='red',marker='o', markersize=5,
            markeredgewidth=1, markerfacecolor='red')

    ax.plot(theta_range, count_001_r, '.-', label='100',color='black',marker='s', markersize=4,
            markeredgewidth=1, markerfacecolor='black')
    ax.plot(theta_range, count_101_r, '.-', label='101',color='brown',marker='s', markersize=3,
            markeredgewidth=1, markerfacecolor='brown')
    ax.plot(theta_range, count_011_r, '.-', label='110',color='cyan',marker='s', markersize=2,
            markeredgewidth=1, markerfacecolor='cyan')
    ax.plot(theta_range, count_111_r, '.-', label='111',color='magenta',marker='s', markersize=1,
            markeredgewidth=1, markerfacecolor='magenta')

    ax.set_xlabel('theta', fontsize=14)
    ax.set_ylabel('Counts', fontsize=14)
    ax.legend(fontsize=14)
    plt.show()
    counts_sum = {}
    counts_sum['000'] = count_000_r; counts_sum['100'] = count_100_r
    counts_sum['001'] = count_001_r; counts_sum['101'] = count_101_r
    counts_sum['010'] = count_010_r; counts_sum['110'] = count_110_r
    counts_sum['011'] = count_011_r; counts_sum['111'] = count_111_r
    return counts_sum
#=========================================================================================
if __name__ == '__main__':
    # results of measuring 3 qubit
    nq = 5  # number of qubits
    nc = 3  # number of classical bits
    mq = [0,1,2,]
    mc = [0,1,2,]
    initial_state = [0,0,0,0,0]
    #
    theta_max_range = np.arange(0.1, 9, 0.1)
    n_theta_inter = 50
    Is_save = True
    savepath = '.\\data\\H_heisenberg_hx\\advance_qasm_simulator\\Nbody%g\\'%nc
    for ik in range(len(theta_max_range)):
        theta_max = round(theta_max_range[ik], 1)
        theta_range = np.arange(0, theta_max, theta_max / n_theta_inter)
        shots = 1024
        #
        qc_m3 = alpha_circuit_construct(nq=nq, nc=nc, mq=mq, mc=mc, initial_state=initial_state)  # get circuit
        counts = run_circuit(qc=qc_m3, theta_range=theta_range, shots=shots)
        counts_sum = measure_3qubit(counts=counts)
        if Is_save is True:
            mkdir(savepath)
            saveexp = 'H_heisenberg_theta(%g,%g,%g)_Nq%d_Nc%d_shots%g' % (
            theta_range[0], theta_max, len(theta_range), nq, nc, shots) + 'advance'
            save(savepath, saveexp + '.pr', (counts_sum, theta_range), ('counts', 'theta'))