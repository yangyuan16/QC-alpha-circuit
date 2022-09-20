# 5 qubits exact evolution of Heisenberg model
# 1) show the results of measuring n qubits, where n > 3 .
# 2) write the data to files in '.pr' format, which is useful for further analysis
#
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
def measure_nqubit(t_series, hx_series, Nbody, bound_cond,v0, N_m,Is_save,savepath,Is_plot):
    t = t_series
    hx = hx_series
    # ======================================================================
    for it1 in range(len(t)):
        prop = []
        for it2 in range(len(hx)):
            H = evolution_H(Nbody=Nbody,bound_cond=bound_cond, hx=hx[it2])
            U = expm(-1j * t[it1] * H)
            v1 = np.dot(U, v0)
            propbility = [v1[it].real ** 2 + v1[it].imag ** 2 for it in range(len(v1))]
            prop.append(propbility)
        if Is_save is True:
            mkdir(savepath)
            saveexp = 'H_heisenberg_hx(%g,%g,%g)_Nq%d_Nc%d_t%g' % (
            hx[0], hx[-1], len(hx), Nbody, N_m, t[it1]) + 'exact'
            save(savepath, saveexp + '.pr', (prop, hx), ('prop', 'hx'))
        if Is_plot is True:
            fig = plt.figure()
            ax = fig.add_subplot(111)
            # 画一个
            for itk in range(2 ** Nbody):
                ax.plot(hx, np.array(prop)[:, itk], '.-', label='%g' % itk, lw=1.5, marker='o', )
            ax.set_xlabel('hx', fontsize=14)
            ax.set_ylabel('Counts', fontsize=14)
            ax.legend(fontsize=14)
            plt.title('t=%g' % (t[it1]), size=20)
            # ax.title('t=%g'%t[it1])
            print('t=%g' % (t[it1]))
            plt.show()
    return
#=====================================================
if __name__ == '__main__':
    Nbody = 4  #
    N_m = 4  # number of measuring qubits
    initial_state = [0,0,0,0]
    bound_cond = 'open' # boundary condition
    v0 = get_initial_vector(initial_state, n=Nbody)
    #
    t = np.arange(0, 10, 0.1)  # set time series
    hx = np.arange(0,1,0.1)
    #
    Is_save = True
    Is_plot = True
    savepath = '.\\data\\H_heisenberg_hx\\exact_evolution\\Nbody%g'%N_m
    measure_nqubit(t_series=t,hx_series=hx,Nbody=Nbody,bound_cond=bound_cond,
                   v0=v0,N_m = N_m, Is_save=Is_save,savepath=savepath, Is_plot=True)
    #