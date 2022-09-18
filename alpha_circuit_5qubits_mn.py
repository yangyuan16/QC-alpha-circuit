#%%
# 1) show the result of measuring n qubits (n = 4, 5, ...) on 5-qubits alpha circuit
# 2) write the data to files in '.pr' format, which is useful for further analysis
#
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
#=========================================================================================
if __name__ == '__main__':
    # results of measuring 4 qubit and 5 qubits
    nq = 5  # number of qubits
    nc = 5  # number of classical bits {set nc = 4 or nc = 5}
    mq = [0,1,2,3] # {set mq = [0,1,2,3] for nc = 4 or mq = [0,1,2,3,4] for nc = 5}
    mc = [0,1,2,3] # {set mc = [0,1,2,3] for nc = 4 or mc = [0,1,2,3,4] for nc = 5}
    initial_state = [0,0,0,0,0]
    #
    theta_max_range = np.arange(1, 9, 0.1)
    n_theta_inter = 50
    Is_save = True
    Is_plot = True
    savepath = '.\\data\\H_heisenberg_hx\\advance_qasm_simulator\\Nbody%g\\'%nc
    for ik in range(len(theta_max_range)):
        theta_max = round(theta_max_range[ik], 1)
        theta_range = np.arange(0, theta_max, theta_max / n_theta_inter)
        shots = 1024
        #
        qc = alpha_circuit_construct(nq=nq, nc=nc, mq=mq, mc=mc, initial_state=initial_state)  # get circuit
        counts = run_circuit(qc=qc, theta_range=theta_range, shots=shots)
        #
        counts_sum = []
        for itk in range(len(counts)):
            counts_new = libcir.circjob_count_nq(counts[itk], nbody=nc)
            counts_sum.append(counts_new)
        #
        if Is_save is True:
            mkdir(savepath)
            saveexp = 'H_heisenberg_theta(%g,%g,%g)_Nq%d_Nc%d_shots%g' % (
            theta_range[0], theta_max, len(theta_range), nq, nc, shots) + 'advance'
            save(savepath, saveexp + '.pr', (counts_sum, theta_range), ('counts', 'theta'))
        #
        if Is_plot is True:
            fig = plt.figure(figsize=(8, 6))
            ax = fig.add_subplot(111)
            # 画一个
            counts_matrix = libcir.circjob_count_maxtrix(counts_sum=counts_sum)
            for it in range(2 ** nc):
                ax.plot(theta_range, np.array(counts_matrix)[:, it], '.-', label='%g' % it, marker='o', markersize=10,
                        markeredgewidth=1, )
            ax.set_xlabel('theta', fontsize=14)
            ax.set_ylabel('Counts', fontsize=14)
            ax.legend(fontsize=14)
            plt.title('theta_max=%g' % theta_max)
            plt.show()