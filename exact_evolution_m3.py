# 5 qubits exact evolution of Heisenberg model
# 1) show the results of measuring 3 qubits.
# 2) write the data to files in '.pr' format, which is useful for further analysis
#

import numpy as np
import scipy
from scipy.linalg import expm
import library.Hamiltonian as libH
import matplotlib.pyplot as plt
from library.BasicFunctions import save_pr as save
from library.BasicFunctions import mkdir
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
def measure_3qubit(t_series, hx_series, Nbody, bound_cond,v0, Is_save,savepath):
    t = t_series
    hx = hx_series
    #
    for it1 in range(len(t)):
        prop000 = []
        prop001 = []
        prop010 = []
        prop011 = []
        prop100 = []
        prop101 = []
        prop110 = []
        prop111 = []
        for it2 in range(len(hx)):
            H = evolution_H(Nbody=Nbody,bound_cond=bound_cond, hx=hx[it2])
            U = expm(-1j * t[it1] * H)
            v1 = np.dot(U, v0)
            propbility = [v1[it].real ** 2 + v1[it].imag ** 2 for it in range(len(v1))]
            p000 = np.sum(propbility[0:round(len(v1) / 8)])
            p001 = np.sum(propbility[round(len(v1) / 8):round(len(v1) / 4)])
            p010 = np.sum(propbility[round(len(v1) / 4):round(len(v1) * 3 / 8)])
            p011 = np.sum(propbility[round(len(v1) * 3 / 8):round(len(v1) / 2)])
            p100 = np.sum(propbility[round(len(v1) / 2):round(len(v1) * 5 / 8)])
            p101 = np.sum(propbility[round(len(v1) * 5 / 8):round(len(v1) * 6 / 8)])
            p110 = np.sum(propbility[round(len(v1) * 6 / 8):round(len(v1) * 7 / 8)])
            p111 = np.sum(propbility[round(len(v1) * 7 / 8):])

            prop000.append(p000)
            prop001.append(p001)
            prop010.append(p010)
            prop011.append(p011)
            prop100.append(p100)
            prop101.append(p101)
            prop110.append(p110)
            prop111.append(p111)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        # 画一个
        ax.plot(hx, prop000, '.-', label='000', lw=1.5, color='blue', marker='o', markersize=10,
                markeredgewidth=1, markerfacecolor='blue')
        ax.plot(hx, prop001, '.-', label='001', lw=1.5, color='orange', marker='o', markersize=8,
                markeredgewidth=1, markerfacecolor='orange')
        ax.plot(hx, prop010, '.-', label='010', lw=1.5, color='green', marker='o', markersize=6,
                markeredgewidth=1, markerfacecolor='green')
        ax.plot(hx, prop011, '.-', label='011', lw=1.5, color='red', marker='o', markersize=5,
                markeredgewidth=1, markerfacecolor='red')
        ax.plot(hx, prop100, '.-', label='100', lw=1.5, color='black', marker='s', markersize=4,
                markeredgewidth=1, markerfacecolor='black')
        ax.plot(hx, prop101, '.-', label='101', lw=1.5, color='brown', marker='s', markersize=3,
                markeredgewidth=1, markerfacecolor='brown')
        ax.plot(hx, prop110, '.-', label='110', lw=1.5, color='cyan', marker='s', markersize=2,
                markeredgewidth=1, markerfacecolor='cyan')
        ax.plot(hx, prop111, '.-', label='111', lw=1.5, color='magenta', marker='s', markersize=1,
                markeredgewidth=1, markerfacecolor='magenta')
        ax.set_xlabel('hx', fontsize=14)
        ax.set_ylabel('Counts', fontsize=14)
        ax.legend(fontsize=14)
        plt.title('t=%g' % (t[it1]), size=20)
        # ax.title('t=%g'%t[it1])
        print('t=%g' % (t[it1]))
        plt.show()

        counts_sum = {}
        counts_sum['000'] = prop000; counts_sum['100'] = prop100
        counts_sum['001'] = prop001; counts_sum['101'] = prop101
        counts_sum['010'] = prop010; counts_sum['110'] = prop110
        counts_sum['011'] = prop011; counts_sum['111'] = prop111
        if Is_save is True:
            mkdir(savepath)
            saveexp = 'H_heisenberg_hx(%g,%g,%g)_Nq%d_Nc%d_t%g' % (
                hx[0], hx[-1], len(hx), Nbody, 3, t[it1]) + 'exact'
            save(savepath, saveexp + '.pr', (counts_sum, hx), ('counts', 'hx'))
    return
#

if __name__ == '__main__':
    Nbody = 5
    initial_state = [0,0,0,0,0]
    bound_cond = 'open' # boundary condition
    v0 = get_initial_vector(initial_state, n=Nbody)
    #
    t = np.arange(1, 10, 1)  # set time series
    hx = np.linspace(0, 1, 100) # set hx series
    #
    Is_save = True
    savepath = '.\\data\\H_heisenberg_hx\\exact_evolution\\Nbody%g'%3
    measure_3qubit(t_series=t,hx_series=hx,Nbody=Nbody,bound_cond=bound_cond,
                   v0=v0,Is_save=Is_save,savepath=savepath)
    #

