# 5 qubits exact evolution of Heisenberg model
# show the results of measuring 1 qubit and 2 qubits.
#
import numpy as np
import scipy
from scipy.linalg import expm
import library.Hamiltonian as libH
import matplotlib.pyplot as plt

#
def get_initial_vector(initial_state,n):
    Nbody = n
    v0 = np.zeros(2 ** Nbody)
    index = 0
    for it in range(len(initial_state)):
        index += initial_state[it] * 2 ** (len(initial_state) - it - 1)
    print('index:', index)
    v0[index] = 1
    return v0
#
def get_Nbody_Hamiltonian(n, bound_cond = 'open'):
    Nbody = n
    if Nbody == 2:
        Hxx, Hyy, Hzz, Hmx, Hmz = libH.heisenberg_2body()
    elif Nbody == 3:
        Hxx, Hyy, Hzz, Hmx, Hmz = libH.heisenberg_3body(bound_cond=bound_cond)
    elif Nbody == 4:
        Hxx, Hyy, Hzz, Hmx, Hmz = libH.heisenberg_4body(bound_cond=bound_cond)
    elif Nbody == 5:
        Hxx, Hyy, Hzz, Hmx, Hmz = libH.heisenberg_5body(bound_cond=bound_cond)
    elif Nbody == 6:
        Hxx, Hyy, Hzz, Hmx, Hmz = libH.heisenberg_6body(bound_cond=bound_cond)
    else:
        raise Exception('n can not larger than 6')
    return Hxx, Hyy, Hzz, Hmx, Hmz
#
def evolution_H(Nbody,bound_cond,hx):
    Hxx, Hyy, Hzz, Hmx, Hmz = get_Nbody_Hamiltonian(n=Nbody, bound_cond=bound_cond)
    H = Hxx + Hyy + Hzz - hx * Hmx
    return H
#
def measure_1qubit(t_series, hx_series, Nbody, bound_cond,v0,):
    t = t_series
    hx = hx_series
    # ====================
    for it1 in range(len(t)):
        prop0 = []
        prop1 = []
        for it2 in range(len(hx)):
            H = evolution_H(Nbody=Nbody,bound_cond=bound_cond, hx=hx[it2])
            U = expm(-1j * t[it1] * H)
            v1 = np.dot(U, v0)
            propbility = [v1[it].real ** 2 + v1[it].imag ** 2 for it in range(len(v1))]
            p0 = np.sum(propbility[0:round(len(v1) / 2)])
            p1 = np.sum(propbility[round(len(v1) / 2):])
            prop0.append(p0)
            prop1.append(p1)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        # 画一个
        ax.plot(hx, prop0, '.-', label='0')
        ax.plot(hx, prop1, '.-', label='1')
        ax.set_xlabel('hx', fontsize=14)
        ax.set_ylabel('Counts', fontsize=14)
        ax.legend(fontsize=14)
        plt.title('t=%g' % (t[it1]), size=20)
        # ax.title('t=%g'%t[it1])
        print('t=%g' % (t[it1]))
        plt.show()
    return
#
def measure_2qubit(t_series, hx_series, Nbody, bound_cond,v0):
    t = t_series
    hx = hx_series
    for it1 in range(len(t)):
        prop00 = []
        prop01 = []
        prop10 = []
        prop11 = []
        for it2 in range(len(hx)):
            H = evolution_H(Nbody=Nbody,bound_cond=bound_cond, hx=hx[it2])
            U = expm(-1j * t[it1] * H)
            v1 = np.dot(U, v0)
            propbility = [v1[it].real ** 2 + v1[it].imag ** 2 for it in range(len(v1))]
            p00 = np.sum(propbility[0:round(len(v1) / 4)])
            p01 = np.sum(propbility[round(len(v1) / 4):round(len(v1) / 2)])
            p10 = np.sum(propbility[round(len(v1) / 2):round(len(v1) * 3 / 4)])
            p11 = np.sum(propbility[round(len(v1) * 3 / 4):])
            prop00.append(p00)
            prop01.append(p01)
            prop10.append(p10)
            prop11.append(p11)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        # 画一个
        ax.plot(hx, prop00, '.-', label='00', lw=1.5, color='blue', marker='o', markersize=6,
                markeredgewidth=1, markerfacecolor='blue')
        ax.plot(hx, prop01, '.-', label='01', lw=1.5, color='orange', marker='o', markersize=3,
                markeredgewidth=1, markerfacecolor='orange')
        ax.plot(hx, prop10, '.-', label='10', lw=1.5, color='green', marker='o', markersize=3,
                markeredgewidth=1, markerfacecolor='green')
        ax.plot(hx, prop11, '.-', label='11', lw=1.5, color='red', marker='o', markersize=3,
                markeredgewidth=1, markerfacecolor='red')
        ax.set_xlabel('hx', fontsize=14)
        ax.set_ylabel('Counts', fontsize=14)
        ax.legend(fontsize=14)
        plt.title('t=%g' % (t[it1]), size=20)
        # ax.title('t=%g'%t[it1])
        print('t=%g' % (t[it1]))
        plt.show()
    return
#
if __name__ == '__main__':
    Nbody = 5
    initial_state = [0,0,0,0,0]
    bound_cond = 'open' # boundary condition
    v0 = get_initial_vector(initial_state, n=Nbody)
    t = np.arange(1, 10, 1)  # set time series
    hx = np.linspace(0, 1, 100) # set hx series
    # results of measuring 1 qubit
    measure_1qubit(t_series=t, hx_series=hx, Nbody=Nbody,
                   bound_cond=bound_cond, v0=v0)
    # results of measuring 2 qubits
    measure_2qubit(t_series=t, hx_series=hx, Nbody=Nbody,
                   bound_cond=bound_cond, v0=v0)