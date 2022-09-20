# Obtain the evolution results of sigma_z_string i.e. sigma_z^n with n > 3
# 1) sigma_z_string by exact_evolution with fixed hx
# 2) sigma_z_string by alpha_circuit with fixed hx
# 3) sigma_z_string by trotter_circuit with fixed hx
#
import numpy as np
import library.BasicFunctions as bf
import matplotlib.pylab as plt
from library.BasicFunctions import save_pr as save
from library.BasicFunctions import mkdir
#
def exact_evolution_results_to_sigma_string(t_range, h1, h2, nh, Nbody, hx_fix,
                                            loadpath, savepath,Is_save, Is_plot):
    hx_1 = h1
    hx_2 = h2
    nhx = nh
    sigmaz_string = []
    for it in range(len(t_range)):
        t = round(t_range[it], 1)
        loadexp = 'H_heisenberg_hx(%g,%g,%g)_Nq%d_Nc%d_t%g' % (hx_1, hx_2, nhx, Nbody, Nbody, t) + 'exact' + '.pr'
        print(loadpath + loadexp)
        data = bf.load_pr(loadpath + loadexp)
        counts_sum = data['prop']
        hx_range = data['hx']
        index = list(hx_range).index(hx_fix)
        prop = counts_sum[index]
        z_string = 0
        for itk in range(len(prop)):
            A = format(itk, 'b').zfill(Nbody)
            z_string += prop[itk] * ((-1) ** A.count('1'))
        sigmaz_string.append(z_string)
    if Is_save is True:
        mkdir(savepath)
        saveexp = 'H_heisenberg_zstring_t(%g,%g,%g)_Nq%d_Nc%d_hx%g' % (
        t_range[0], t_range[-1], len(t_range), Nbody, Nbody, hx_fix) + 'exact'
        save(savepath, saveexp + '.pr', (sigmaz_string, t_range), ('sigmaz_string', 't_range'))
    if Is_plot is True:
        fig = plt.figure(figsize=(10, 4))
        ax1 = fig.add_subplot(111)
        # 画一个
        if Nbody == 4:
            label_name = r'$\sigma^{zzzz}$'
        elif Nbody == 5:
            label_name = r'$\sigma^{zzzzz}$'
        else:
            raise Exception('wrong input of Nbody')
        ax1.plot(t_range, sigmaz_string, '.-', label=label_name, lw=1.5, color='green', marker='o',
                 markersize=3,
                 markeredgewidth=1, markerfacecolor='green')

        ax1.set_xlabel('t', fontsize=14)
        ax1.set_ylabel('Counts', fontsize=14)
        ax1.legend(fontsize=14)
        plt.title('hx=%g_N%g' % (hx_fix, Nbody), size=20)
        plt.show()
    return
#
def trotter_circuit_results_to_sigma_string(t_range, h1, h2, nh, Nbody, hx_fix,
                                            dt, shots, loadpath, savepath,
                                            Is_save=True,Is_plot=True, ):
    hx_1 = h1
    hx_2 = h2
    nhx = nh
    sigmaz_string = []
    for it in range(len(t_range)):
        t = round(t_range[it], 1)
        loadexp = 'H_heisenberg_hx(%g,%g,%g)_Nq%d_Nc%d_t%g_dt%g_shots%g' % (
        hx_1, hx_2, nhx, Nbody, Nbody, t, dt, shots) + 'trotter' + '.pr'
        print(loadpath + loadexp)
        data = bf.load_pr(loadpath + loadexp)
        counts_sum = data['counts']
        hx_range = data['hx']
        index = list(hx_range).index(hx_fix)
        prop = counts_sum[index]
        z_string = 0
        for itk in range(len(prop)):
            A = format(itk, 'b').zfill(Nbody)
            z_string += prop[A] * ((-1) ** A.count('1'))
        sigmaz_string.append(z_string / shots)
    if Is_save is True:
        mkdir(savepath)
        saveexp = 'H_heisenberg_zstring_t(%g,%g,%g)_Nq%d_Nc%d_hx%g_dt%g_shots%g' % (
            t_range[0], t_range[-1], len(t_range), Nbody, Nbody, hx_fix, dt, shots) + 'trotter'
        save(savepath, saveexp + '.pr', (sigmaz_string, t_range), ('sigmaz_string', 't_range'))
    if Is_plot is True:
        fig = plt.figure(figsize=(10, 4))
        ax1 = fig.add_subplot(111)
        # 画一个
        if Nbody == 4:
            label_name = r'$\sigma^{zzzz}$'
        elif Nbody == 5:
            label_name = r'$\sigma^{zzzzz}$'
        else:
            raise Exception('wrong input of Nbody')
        ax1.plot(t_range, sigmaz_string, '.-', label=label_name, lw=1.5, color='green', marker='o', markersize=3,
                 markeredgewidth=1, markerfacecolor='green')
        ax1.set_xlabel('t', fontsize=14)
        ax1.set_ylabel('Counts', fontsize=14)
        ax1.legend(fontsize=14)
        plt.title('hx=%g_Nbody%g' % (hx_fix, Nbody), size=20)
        plt.show()
    return
#
def alpha_circuit_results_to_sigma_string(theta_max_range, n_theta_inter,Nqubits, Nbody, hx_fix,
                                          loadpath, savepath, Is_save, Is_plot, ):
    sigmaz_string = []
    for it in range(len(theta_max_range)):
        theta_max = round(theta_max_range[it], 1)
        loadexp = 'H_heisenberg_theta(%g,%g,%g)_Nq%d_Nc%d_shots%g' % (
        0, theta_max, n_theta_inter, Nqubits, Nbody, shots) + 'advance' + '.pr'
        print(loadpath + loadexp)
        data = bf.load_pr(loadpath + loadexp)
        counts_sum = data['counts']
        theta_range = data['theta']
        index = round(len(theta_range) * hx_fix)
        prop = counts_sum[index]
        z_string = 0
        for itk in range(len(prop)):
            A = format(itk, 'b').zfill(Nbody)
            z_string += prop[A] * ((-1) ** A.count('1'))
        sigmaz_string.append(z_string / shots)

    if Is_save is True:
        mkdir(savepath)
        saveexp = 'H_heisenberg_zstring_thetamax(%g,%g,%g)_Nq%d_Nc%d_hx%g_shots%g' % (
            theta_max_range[0], theta_max_range[-1], len(theta_max_range), Nbody, Nbody, hx_fix, shots) + 'advance'
        save(savepath, saveexp + '.pr', (sigmaz_string, theta_max_range), ('sigmaz_string', 'theta_max_range'))

    if Is_plot is True:
        fig = plt.figure(figsize=(10, 4))
        ax1 = fig.add_subplot(111)
        # 画一个
        ax1.plot(theta_max_range, sigmaz_string, '.-', label=r'sigmaz_string', lw=1.5, color='green', marker='o',
                 markersize=3,
                 markeredgewidth=1, markerfacecolor='green')
        ax1.set_xlabel('theta_max', fontsize=14)
        ax1.set_ylabel('Counts', fontsize=14)
        ax1.legend(fontsize=14)
        plt.title('hx=%g_Nbody%g' % (hx_fix, Nbody), size=20)
        plt.show()
    return
#
if __name__ == '__main__':
    scheme = 'alpha' # 'exact', 'alpha', 'trotter'
    if scheme is 'exact':
        # Obtain sigma_z sigma_zz sigma_zzz from the exact evolution
        Nbody = 5
        hx_1 = 0
        hx_2 = 0.9
        nhx = 10
        t_range = np.arange(0, 8, 0.1)
        hx_fix = 0.5
        loadpath = '.\\data\\H_heisenberg_hx\\exact_evolution\\Nbody%g\\' % Nbody
        savepath = '.\\data\\H_heisenberg_hx\\exact_evolution_fix_hx\\Nbody%g\\' % Nbody
        exact_evolution_results_to_sigma_string(t_range=t_range, h1=hx_1, h2=hx_2, nh=nhx,
                                                Nbody=Nbody, hx_fix=hx_fix,
                                                loadpath=loadpath, savepath=savepath,
                                                Is_save = True,Is_plot=True,)
    if scheme is 'trotter':
        #Obtain sigma_z sigma_zz sigma_zzz from the evolution on trotter circuit
        Nbody = 5
        hx_1 = 0
        hx_2 = 0.9
        nhx = 10
        t_range = np.arange(0, 8, 0.1)
        hx_fix = 0.5
        dt = 0.1
        shots = 1024
        loadpath_t = '.\\data\\H_heisenberg_hx\\trotter_qasm_simulator\\Nbody%g\\' % Nbody
        savepath_t = '.\\data\\H_heisenberg_hx\\trotter_qasm_simulator_fix_hx\\Nbody%g\\' % Nbody
        trotter_circuit_results_to_sigma_string(t_range=t_range, h1=hx_1, h2=hx_2, nh=nhx, Nbody=Nbody,
                                                hx_fix=hx_fix, dt=dt, shots=shots, loadpath=loadpath_t,
                                                savepath=savepath_t,Is_save=True, Is_plot=True)
    if scheme is 'alpha':
        # obtain sigma_z sigma_zz sigma_zzz from the evolution on alpha circuit
        Nqubits = 5
        Nbody = 5
        shots = 1024
        theta_max_range = np.arange(0.1, 8, 0.1)  # theta max 就是我要旋转到一个角度
        n_theta_inter = 50  # 从 0 到 theta_max 之间取 10 个值。
        hx_fix = 0.5
        loadpath_a = '.\\data\\H_heisenberg_hx\\advance_qasm_simulator\\Nbody%g\\' % Nbody
        savepath_a = '.\\data\\H_heisenberg_hx\\advance_qasm_simulator_fix_hx\\Nbody%g\\' % Nbody
        alpha_circuit_results_to_sigma_string(theta_max_range, n_theta_inter, Nqubits, Nbody, hx_fix,
                                              loadpath=loadpath_a, savepath=savepath_a,
                                              Is_save=True, Is_plot=True)


