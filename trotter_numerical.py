# evolution of 5 qubits Heisenberg model by trotter numerical simulators
# 1) write the data to files in '.pr' format, which is useful for further analysis
#
import numpy as np
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
def trotter_slice(dt, hx, Nbody):
    if Nbody ==5:
        Hxx, Hyy, Hzz, Hmz, Hmx = libH.heisenberg_5body_trotter_block()
    else:
        raise Exception ('wrong input of Nbody')
    H_01 = Hxx['01'] + Hyy['01'] + Hzz['01'] - hx * Hmx['01']
    H_12 = Hxx['12'] + Hyy['12'] + Hzz['12'] - hx * Hmx['12']
    H_23 = Hxx['23'] + Hyy['23'] + Hzz['23'] - hx * Hmx['23']
    H_34 = Hxx['34'] + Hyy['34'] + Hzz['34'] - hx * Hmx['34']
    H_04 = Hxx['04'] + Hyy['04'] + Hzz['04'] - hx * Hmx['04']

    U_01 = expm(-1j  * dt * H_01)
    U_12 = expm(-1j  * dt * H_12)
    U_23 = expm(-1j  * dt * H_23)
    U_34 = expm(-1j  * dt * H_34)
    U_04 = expm(-1j  * dt * H_04)
    U = np.dot(U_01,np.dot(U_12,np.dot(U_23,np.dot(U_34,U_04))))
    return U
#
def trotter_evolution(t_series,dt,hx,Nbody,v0,Is_save,savepath,Is_plot):
    t = t_series
    prop = []
    prop000 = []
    prop001 = []
    prop010 = []
    prop011 = []
    prop100 = []
    prop101 = []
    prop110 = []
    prop111 = []
    for it1 in range(len(t)):
        num_slice = t[it1] / dt
        U = trotter_slice(dt=dt,hx=hx,Nbody=Nbody)
        v_ini = v0
        for it2 in range(round(num_slice)):
            v_ini = np.dot(U,v_ini)
        v1 = v_ini
        propbility = [v1[it].real ** 2 + v1[it].imag ** 2 for it in range(len(v1))]
        prop.append(propbility)
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
    counts_sum = {}
    counts_sum['000'] = prop000; counts_sum['100'] = prop100
    counts_sum['001'] = prop001; counts_sum['101'] = prop101
    counts_sum['010'] = prop010; counts_sum['110'] = prop110
    counts_sum['011'] = prop011; counts_sum['111'] = prop111
    if Is_save is True:
        mkdir(savepath)
        saveexp = 'Trotter_numerical_hx%g_Nbody%g_t(%g,%g,%g)' % (
            hx, Nbody,t[0],t[-1],len(t))
        save(savepath, saveexp + '.pr', (prop, counts_sum, hx), ('prop', 'counts', 'hx'))
    if Is_plot is True:
        fig = plt.figure()
        ax = fig.add_subplot(111)
        # 画一个
        for itk in range(2 ** Nbody):
            ax.plot(t, np.array(prop)[:, itk], '.-', label='%g' % itk, lw=1.5, marker='o', )
        ax.set_xlabel('t', fontsize=14)
        ax.set_ylabel('Counts', fontsize=14)
        ax.legend(fontsize=14)
        plt.title('hx=%g' % (hx), size=20)
        # ax.title('t=%g'%t[it1])
        plt.show()
    return
#
if __name__ == '__main__':
    print()
    Nbody = 5
    initial_state = [0,0,0,0,0]
    v0 = get_initial_vector(initial_state=initial_state, n=Nbody)
    t_series = np.arange(0, 8, 0.2)  # set time series
    dt = 0.02
    hx = 0.5
    savepath = '.\\data\\H_heisenberg_hx\\trotter_numerical\\Nbody%g\\'%Nbody
    Is_save = True
    Is_plot = True
    trotter_evolution(t_series=t_series, dt=dt, hx=hx, Nbody=Nbody,v0=v0,
                      Is_save=Is_save, savepath=savepath, Is_plot=Is_plot)
