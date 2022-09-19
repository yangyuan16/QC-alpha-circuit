# realize the trotter scheme by quantum gates
# results of measuring n qubits (n > 3) based on trotter scheme
#==============================================================
#
import numpy as np
import scipy
from scipy.linalg import expm
from qiskit.quantum_info import Operator
from qiskit import  QuantumCircuit, QuantumRegister, ClassicalRegister
import matplotlib.pyplot as plt
import library.Hamiltonian as libH
from qiskit import execute, BasicAer
from library.BasicFunctions import save_pr as save
from library.BasicFunctions import mkdir
import library.circuit as libcir
#
#
def get_U_series(dt,hx_series,Hxx,Hyy,Hzz,Hmx):
    U = []
    hx = hx_series
    for it in range(len(hx)):
        H = Hxx + Hyy + Hzz - hx[it] * Hmx
        U0 = expm(-1j * dt * H)
        U.append(U0)
    return U
#
def construct_trotter_circuit(hx_series, Nbody, t, dt, U_series,Is_plot_circuit):
    hx = hx_series
    U = U_series
    steps = round(t / dt)
    circuit_trotter = []
    for it in range(len(hx)): # 对磁场进行循环
        n = Nbody  # qubits 数目
        nc = Nbody # c_bit 数目  nc 的数目必须按照严格线路设计时测量比特的数目写，否则会出现bug
        qc = QuantumCircuit(n,nc)
        #=================================
        # 固定不同的初态
        for it1 in range(n):
            if initial_state[it1] == 1:
                qc.x(it1)
            else:
                qc.id(it1)
        #===================================
        for it2 in range(np.int64(steps)):
            for it3 in range(n-1):
                U_gate = Operator(U[it])
                qc.unitary(U_gate, [it3, it3+1])
            qc.barrier()
        qc.measure(q_measure, c_measure)
        circuit_trotter.append(qc)
        if Is_plot_circuit is True:
            qc.draw('mpl')
            plt.title('hx=%g_t=%g_dt=%g'%(hx[it],t,dt))
            plt.show()
    return circuit_trotter
#
def measure_nqubit(t_series, hx_series, Nbody, dt, U_series,shots,Is_plot_circuit, Is_plot_result,Is_save,savepath):
    hx = hx_series
    for itk in range(len(t_series)):
        t = round(t_series[itk], 1)
        circuit_collect = construct_trotter_circuit(hx_series=hx_series,Nbody=Nbody,
                                                    t=t, dt=dt, U_series=U_series,
                                                    Is_plot_circuit=Is_plot_circuit)
        counts_sum = []
        for it4 in range(len(circuit_collect)):
            job = execute(circuit_collect[it4],
                          backend=BasicAer.get_backend('qasm_simulator'),
                          shots=shots)
            counts = job.result().get_counts()
            counts_new = libcir.circjob_count_nq(counts, nbody=Nbody)
            counts_sum.append(counts_new)
        #
        if Is_save is True:
            mkdir(savepath)
            saveexp = 'H_heisenberg_hx(%g,%g,%g)_Nq%d_Nc%d_t%g_dt%g_shots%g' % (
            hx[0], hx[-1], len(hx), Nbody, Nbody, t, dt, shots) + 'trotter'
            save(savepath, saveexp + '.pr', (counts_sum, hx), ('counts', 'hx'))
        #
        if Is_plot_result is True:
            fig = plt.figure(figsize=(8, 6))
            ax = fig.add_subplot(111)
            counts_matrix = libcir.circjob_count_maxtrix(counts_sum=counts_sum)
            for it in range(2 ** Nbody):
                ax.plot(hx, np.array(counts_matrix)[:, it], '.-', label='%g' % it, marker='o', markersize=10,
                        markeredgewidth=1, )
            ax.set_xlabel('hx', fontsize=14)
            ax.set_ylabel('Counts', fontsize=14)
            ax.legend(fontsize=14)
            plt.title('t=%g_dt=%g' % (t, dt))
            plt.show()
    return
#

if __name__ == '__main__':
    dt = 0.1
    hx_series = np.arange(0, 1, 0.1)
    t_series = np.arange(0, 9, 0.1)
    Hxx, Hyy, Hzz, Hmx, Hmz = libH.heisenberg_2body()
    #
    Nbody = 5
    initial_state = [0, 0, 0, 0, 0]  # 选取初始态
    q_measure = [0, 1, 2, 3, 4]  # [q0, q1, q2, q3]
    c_measure = [0, 1, 2, 3, 4]  # [c0, c1, c2, c3]
    Is_plot_circuit = False
    Is_plot_result = False
    #
    shots=1024
    Is_save = True
    savepath = '.\\data\\H_heisenberg_hx\\trotter_qasm_simulator\\Nbody%g'%Nbody
    #
    U_collect = get_U_series(dt=dt, hx_series=hx_series, Hxx=Hxx,
                         Hyy=Hyy,Hzz=Hzz,Hmx=Hmx)
    #
    measure_nqubit(t_series=t_series, hx_series=hx_series, Nbody=Nbody,
                   dt=dt, U_series=U_collect, shots=shots,
                   Is_plot_circuit=Is_plot_circuit, Is_plot_result=Is_plot_result,
                   Is_save=Is_save,savepath=savepath)



