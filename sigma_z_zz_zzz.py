# Obtain the evolution results of sigma_z, sigma_zz, and sigma_zzz
# 1) sigma_z by exact_evolution with fixed hx
# 2) sigma_z by alpha_circuit with fixed hx
# 3) sigma_z by trotter_circuit with fixed hx
#
# 4) sigma_zz by exact_evolution with fixed hx
# 5) sigma_zz by alpha_circuit with fixed hx
# 6) sigma_zz by trotter_circuit with fixed hx
#
# 7) sigma_zzz by exact_evolution with fixed hx,
# 8) sigma_zzz by alpha_circuit with fixed hx
# 9) sigma_zzz by trotter_circuit with fixed hx
#====================================================================
import numpy as np
import library.BasicFunctions as bf
import matplotlib.pylab as plt
from library.BasicFunctions import save_pr as save
from library.BasicFunctions import mkdir
#
def plot_sigma_z(t_range,counts_0, counts_1, sigma_z):
    fig = plt.figure(figsize=(10, 4))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    # 画一个
    ax1.plot(t_range, counts_0, '.-', label='0', lw=1.5, color='blue', marker='o', markersize=3,
             markeredgewidth=1, markerfacecolor='blue')
    ax1.plot(t_range, counts_1, '.-', label='1', lw=1.5, color='orange', marker='o', markersize=3,
             markeredgewidth=1, markerfacecolor='orange')
    ax2.plot(t_range, sigma_z, '.-', label=r'$\sigma^z$', lw=1.5, color='green', marker='o', markersize=3,
             markeredgewidth=1, markerfacecolor='green')
    #
    ax1.set_xlabel('t', fontsize=14)
    ax1.set_ylabel('Counts', fontsize=14)
    ax1.legend(fontsize=14)
    plt.title('hx=%g' % (hx_fix), size=20)

    ax2.set_xlabel('t', fontsize=14)
    ax2.set_ylabel(r'$\sigma^z(t)$', fontsize=14)
    ax2.legend(fontsize=14)
    plt.title('hx=%g' % (hx_fix), size=20)
    plt.show()
    return
def plot_sigma_zz(t_range, counts_00, counts_01, counts_10, counts_11, sigma_zz):
    fig = plt.figure(figsize=(10, 4))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    # 画一个
    ax1.plot(t_range, counts_00, '.-', label='00', lw=1.5, color='blue', marker='o', markersize=3,
             markeredgewidth=1, markerfacecolor='blue')
    ax1.plot(t_range, counts_01, '.-', label='01', lw=1.5, color='orange', marker='o', markersize=3,
             markeredgewidth=1, markerfacecolor='orange')
    ax1.plot(t_range, counts_10, '.-', label='10', lw=1.5, color='red', marker='o', markersize=3,
             markeredgewidth=1, markerfacecolor='red')
    ax1.plot(t_range, counts_11, '.-', label='11', lw=1.5, color='yellow', marker='o', markersize=3,
             markeredgewidth=1, markerfacecolor='yellow')
    ax2.plot(t_range, sigma_zz, '.-', label=r'$\sigma^z\sigma^z (t)$', lw=1.5, color='green', marker='o', markersize=3,
             markeredgewidth=1, markerfacecolor='green')

    ax1.set_xlabel('t', fontsize=14)
    ax1.set_ylabel('Counts', fontsize=14)
    ax1.legend(fontsize=14)
    plt.title('hx=%g' % (hx_fix), size=20)

    ax2.set_xlabel('t', fontsize=14)
    ax2.set_ylabel(r'$\sigma^z \sigma^z (t)$', fontsize=14)
    ax2.legend(fontsize=14)
    plt.title('hx=%g' % (hx_fix), size=20)
    plt.show()
    return
#
def plot_sigma_zzz(t_range, counts_000,counts_001,counts_010,counts_011,
                   counts_100,counts_101,counts_110,counts_111,sigma_zzz):
    fig = plt.figure(figsize=(10, 4))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    # 画一个
    ax1.plot(t_range, counts_000, '.-', label='000', lw=1.5, color='blue', marker='o', markersize=3,
             markeredgewidth=1, markerfacecolor='blue')
    ax1.plot(t_range, counts_001, '.-', label='001', lw=1.5, color='orange', marker='o', markersize=3,
             markeredgewidth=1, markerfacecolor='orange')

    ax1.plot(t_range, counts_010, '.-', label='010', lw=1.5, color='red', marker='o', markersize=3,
             markeredgewidth=1, markerfacecolor='red')
    ax1.plot(t_range, counts_011, '.-', label='011', lw=1.5, color='yellow', marker='o', markersize=3,
             markeredgewidth=1, markerfacecolor='yellow')

    ax1.plot(t_range, counts_100, '.-', label='100', lw=1.5, color='black', marker='o', markersize=3,
             markeredgewidth=1, markerfacecolor='red')
    ax1.plot(t_range, counts_101, '.-', label='101', lw=1.5, color='brown', marker='o', markersize=3,
             markeredgewidth=1, markerfacecolor='yellow')
    ax1.plot(t_range, counts_110, '.-', label='110', lw=1.5, color='cyan', marker='o', markersize=3,
             markeredgewidth=1, markerfacecolor='red')
    ax1.plot(t_range, counts_111, '.-', label='111', lw=1.5, color='magenta', marker='o', markersize=3,
             markeredgewidth=1, markerfacecolor='yellow')

    ax2.plot(t_range, sigma_zzz, '.-', label=r'$\sigma^z\sigma^z\sigma^z(t)$', lw=1.5, color='green', marker='o', markersize=3,
             markeredgewidth=1, markerfacecolor='green')

    ax1.set_xlabel('t', fontsize=14)
    ax1.set_ylabel('Counts', fontsize=14)
    ax1.legend(fontsize=14)
    plt.title('hx=%g' % (hx_fix), size=20)

    ax2.set_xlabel('t', fontsize=14)
    ax2.set_ylabel(r'$\sigma^z\sigma^z\sigma^z(t)$', fontsize=14)
    ax2.legend(fontsize=14)
    plt.title('hx=%g' % (hx_fix), size=20)
    plt.show()
    return
#
def exact_evolution_results_to_sigma(t_range, h1,h2,nh,Nqubits,Nbody,hx_fix, loadpath, savepath,
                                     Is_save_1q, Is_save_2q, Is_save_3q,
                                     Is_plot_1q, Is_plot_2q, Is_plot_3q):
    hx_1 = h1
    hx_2 = h2
    nhx = nh
    counts_0 = []; counts_1 = []
    counts_00 = []; counts_01 = []; counts_10 = []; counts_11 = []
    counts_000 = []; counts_001 = []; counts_010 = []; counts_011 = []
    counts_100 = []; counts_101 = []; counts_110 = []; counts_111 = []
    sigma_z = []; sigma_zz = []; sigma_zzz = []
    for it in range(len(t_range)):
        t = round(t_range[it], 1)
        loadexp = 'H_heisenberg_hx(%g,%g,%g)_Nq%d_Nc%d_t%g' % (hx_1, hx_2, nhx, Nqubits, Nbody, t) + 'exact' + '.pr'
        print(loadpath + loadexp)
        data = bf.load_pr(loadpath + loadexp)
        counts_sum = data['counts']
        hx_range = data['hx']
        index = list(hx_range).index(hx_fix)
        c0 = counts_sum['000'][index] + counts_sum['001'][index] + counts_sum['010'][index] + counts_sum['011'][index]
        c1 = counts_sum['100'][index] + counts_sum['101'][index] + counts_sum['110'][index] + counts_sum['111'][index]
        c00 = counts_sum['000'][index] + counts_sum['001'][index]
        c01 = counts_sum['010'][index] + counts_sum['011'][index]
        c10 = counts_sum['100'][index] + counts_sum['101'][index]
        c11 = counts_sum['110'][index] + counts_sum['111'][index]
        c000 = counts_sum['000'][index]; c001 = counts_sum['001'][index]
        c010 = counts_sum['010'][index]; c011 = counts_sum['011'][index]
        c100 = counts_sum['100'][index]; c101 = counts_sum['101'][index]
        c110 = counts_sum['110'][index]; c111 = counts_sum['111'][index]
        #
        counts_0.append(c0); counts_1.append(c1)
        counts_00.append(c00); counts_01.append(c01); counts_10.append(c10); counts_11.append(c11)
        counts_000.append(c000); counts_001.append(c001); counts_010.append(c010); counts_011.append(c011)
        counts_100.append(c100); counts_101.append(c101); counts_110.append(c110); counts_111.append(c111)
        sigma_z.append(c0 - c1)
        sigma_zz.append(c00 - c01 - c10 + c11)
        sigma_zzz.append(c000 - c001 - c010 + c011 - c100 + c101 + c110 - c111)
    if Is_save_1q is True:
        mkdir(savepath)
        saveexp = 'H_heisenberg_sigmaz_t(%g,%g,%g)_Nq%d_Nc%d_hx%g' % (
        t_range[0], t_range[-1], len(t_range), Nbody, Nbody, hx_fix) + 'exact'
        save(savepath, saveexp + '.pr', (counts_0, counts_1, sigma_z, t_range),
             ('counts_0', 'counts_1', 'sigma_z', 't_range'))
    if Is_save_2q is True:
        mkdir(savepath)
        saveexp = 'H_heisenberg_sigmazz_t(%g,%g,%g)_Nq%d_Nc%d_hx%g' % (
        t_range[0], t_range[-1], len(t_range), Nbody, Nbody, hx_fix) + 'exact'
        save(savepath, saveexp + '.pr', (counts_00, counts_01, counts_10, counts_11,
                                         sigma_zz, t_range),
             ('counts_00', 'counts_01', 'counts_10', 'counts_11', 'sigma_zz', 't_range'))
    if Is_save_3q is True:
        mkdir(savepath)
        saveexp = 'H_heisenberg_sigmazzz_t(%g,%g,%g)_Nq%d_Nc%d_hx%g' % (
        t_range[0], t_range[-1], len(t_range), Nbody, Nbody, hx_fix) + 'exact'
        save(savepath, saveexp + '.pr', (counts_000, counts_001, counts_010, counts_011,
                                         counts_100, counts_101, counts_110, counts_111, sigma_zzz, t_range), (
                 'counts_000', 'counts_001', 'counts_010', 'counts_011', 'counts_100', 'counts_101', 'counts_110',
                 'counts_111',
                 'sigma_zzz', 't_range'))
    if Is_plot_1q is True:
        plot_sigma_z(t_range=t_range, counts_0=counts_0, counts_1=counts_1, sigma_z=sigma_z)
    if Is_plot_2q is True:
        plot_sigma_zz(t_range=t_range, counts_00=counts_00,counts_01=counts_01,counts_10=counts_10,
                      counts_11=counts_11,sigma_zz=sigma_zz)
    if Is_plot_3q is True:
        plot_sigma_zzz(t_range=t_range,counts_000=counts_000,counts_001=counts_001,counts_010=counts_010,
                       counts_011=counts_011,counts_100=counts_100,counts_101=counts_101,counts_110=counts_110,
                       counts_111=counts_111,sigma_zzz=sigma_zzz)
    return
#
def trotter_circuit_results_to_sigma(t_range, h1,h2,nh,Nbody,hx_fix, dt, shots,
                                     loadpath, savepath,
                                     Is_save_1q, Is_save_2q, Is_save_3q,
                                     Is_plot_1q, Is_plot_2q, Is_plot_3q):
    hx_1 = h1
    hx_2 = h2
    nhx = nh
    #
    sigma_z = []; sigma_zz = []; sigma_zzz = []
    counts_0 = []; counts_1 = []
    counts_00 = []; counts_01 = []; counts_10 = []; counts_11 = []
    counts_000 = []; counts_001 = []; counts_010 = []; counts_011 = []
    counts_100 = []; counts_101 = []; counts_110 = []; counts_111 = []
    hx_fix = hx_fix
    for it in range(len(t_range)):
        t = round(t_range[it], 1)
        loadexp = 'H_heisenberg_hx(%g,%g,%g)_Nq%d_Nc%d_t%g_dt%g_shots%g' % (
        hx_1, hx_2, nhx, Nbody, Nbody, t, dt, shots) + 'trotter' + '.pr'
        print(loadpath + loadexp)
        data = bf.load_pr(loadpath + loadexp)
        counts_sum = data['counts']
        hx_range = data['hx']
        index = list(hx_range).index(hx_fix)
        c000 = counts_sum['000'][index]; c001 = counts_sum['001'][index]
        c010 = counts_sum['010'][index]; c011 = counts_sum['011'][index]
        c100 = counts_sum['100'][index]; c101 = counts_sum['101'][index]
        c110 = counts_sum['110'][index]; c111 = counts_sum['111'][index]
        c0 = counts_sum['000'][index] + counts_sum['001'][index] + counts_sum['010'][index] + counts_sum['011'][index]
        c1 = counts_sum['100'][index] + counts_sum['101'][index] + counts_sum['110'][index] + counts_sum['111'][index]
        c00 = c000 + c001; c01 = c010 + c011; c10 = c100 + c101; c11 = c110 + c111
        counts_0.append(c0); counts_1.append(c1)
        counts_00.append(c00); counts_01.append(c01); counts_10.append(c10); counts_11.append(c11)
        counts_000.append(c000); counts_001.append(c001); counts_010.append(c010); counts_011.append(c011)
        counts_100.append(c100); counts_101.append(c101); counts_110.append(c110); counts_111.append(c111)
        sigma_z.append(c0 - c1)
        sigma_zz.append(c00 - c01 - c10 + c11)
        sigma_zzz.append(c000 - c001 - c010 + c011 - c100 + c101 + c110 - c111)
    if Is_save_1q is True:
        mkdir(savepath)
        saveexp = 'H_heisenberg_sigmaz_t(%g,%g,%g)_Nq%d_Nc%d_hx%g_dt%g_shots%g' % (
        t_range[0], t_range[-1], len(t_range), Nbody, Nbody, hx_fix, dt, shots) + 'trotter'
        save(savepath, saveexp + '.pr', (counts_0, counts_1, sigma_z, t_range),
             ('counts_0', 'counts_1', 'sigma_z', 't_range'))
    if Is_save_2q is True:
        mkdir(savepath)
        saveexp = 'H_heisenberg_sigmazz_t(%g,%g,%g)_Nq%d_Nc%d_hx%g_dt%g_shots%g' % (
            t_range[0], t_range[-1], len(t_range), Nbody, Nbody, hx_fix, dt, shots) + 'trotter'
        save(savepath, saveexp + '.pr', (counts_00, counts_01, counts_10, counts_11, sigma_zz, t_range),
             ('counts_00', 'counts_01', 'counts_10', 'counts_11', 'sigma_zz', 't_range'))
    if Is_save_3q is True:
        mkdir(savepath)
        saveexp = 'H_heisenberg_sigmazzz_t(%g,%g,%g)_Nq%d_Nc%d_hx%g_dt%g_shots%g' % (
            t_range[0], t_range[-1], len(t_range), Nbody, Nbody, hx_fix, dt, shots) + 'trotter'
        save(savepath, saveexp + '.pr', (counts_000, counts_001, counts_010, counts_011, counts_100, counts_101,
                                         counts_110, counts_111, sigma_zzz, t_range),
             ('counts_000', 'counts_001', 'counts_010', 'counts_011', 'counts_100', 'counts_101', 'counts_110',
              'counts_111',
              'sigma_zzz', 't_range'))
    if Is_plot_1q is True:
        plot_sigma_z(t_range=t_range, counts_0=counts_0, counts_1=counts_1, sigma_z=sigma_z)
    if Is_plot_2q is True:
        plot_sigma_zz(t_range=t_range, counts_00=counts_00,counts_01=counts_01,counts_10=counts_10,
                      counts_11=counts_11,sigma_zz=sigma_zz)
    if Is_plot_3q is True:
        plot_sigma_zzz(t_range=t_range,counts_000=counts_000,counts_001=counts_001,counts_010=counts_010,
                       counts_011=counts_011,counts_100=counts_100,counts_101=counts_101,counts_110=counts_110,
                       counts_111=counts_111,sigma_zzz=sigma_zzz)
    return
#
def alpha_circuit_results_to_sigma(theta_max_range,n_theta_inter,Nqubits,Nbody,hx_fix, loadpath, savepath,
                                   Is_save_1q, Is_save_2q, Is_save_3q,
                                   Is_plot_1q, Is_plot_2q, Is_plot_3q):
    sigma_z = []; sigma_zz = []; sigma_zzz = []
    counts_0 = []; counts_1 = []
    counts_00 = []; counts_01 = []; counts_10 = []; counts_11 = []
    counts_000 = []; counts_001 = []; counts_010 = []; counts_011 = []
    counts_100 = []; counts_101 = []; counts_110 = []; counts_111 = []
    hx_fix = hx_fix
    for it in range(len(theta_max_range)):
        theta_max = round(theta_max_range[it], 1)
        loadexp = 'H_heisenberg_theta(%g,%g,%g)_Nq%d_Nc%d_shots%g' % (
        0, theta_max, n_theta_inter, Nqubits, Nbody, shots) + 'advance' + '.pr'
        print(loadpath + loadexp)
        data = bf.load_pr(loadpath + loadexp)
        counts_sum = data['counts']
        theta_range = data['theta']
        index = round(len(theta_range) * hx_fix)
        c000 = counts_sum['000'][index]; c001 = counts_sum['001'][index]; c010 = counts_sum['010'][index]; c011 = counts_sum['011'][index]
        c100 = counts_sum['100'][index]; c101 = counts_sum['101'][index]; c110 = counts_sum['110'][index]; c111 = counts_sum['111'][index]
        c0 = counts_sum['000'][index] + counts_sum['001'][index] + counts_sum['010'][index] + counts_sum['011'][index]
        c1 = counts_sum['100'][index] + counts_sum['101'][index] + counts_sum['110'][index] + counts_sum['111'][index]
        c00 = c000 + c001; c01 = c010 + c011; c10 = c100 + c101; c11 = c110 + c111
        counts_0.append(c0); counts_1.append(c1)
        counts_00.append(c00); counts_01.append(c01); counts_10.append(c10); counts_11.append(c11)
        counts_000.append(c000); counts_001.append(c001); counts_010.append(c010); counts_011.append(c011)
        counts_100.append(c100); counts_101.append(c101); counts_110.append(c110); counts_111.append(c111)
        sigma_z.append(c0 - c1)
        sigma_zz.append(c00 - c01 - c10 + c11)
        sigma_zzz.append(c000 - c001 - c010 + c011 - c100 + c101 + c110 - c111)

    if Is_save_1q is True:
        mkdir(savepath)
        saveexp = 'H_heisenberg_sigmaz_thetamax(%g,%g,%g)_Nq%d_Nc%d_hx%g_shots%g' % (
        theta_max_range[0], theta_max_range[-1], len(theta_max_range), Nbody, Nbody, hx_fix, shots) + 'advance'
        save(savepath, saveexp + '.pr', (counts_0, counts_1, sigma_z, theta_max_range),
             ('counts_0', 'counts_1', 'sigma_z', 'theta_max_range'))
    if Is_save_2q is True:
        mkdir(savepath)
        saveexp = 'H_heisenberg_sigmazz_thetamax(%g,%g,%g)_Nq%d_Nc%d_hx%g_shots%g' % (
            theta_max_range[0], theta_max_range[-1], len(theta_max_range), Nbody, Nbody, hx_fix, shots) + 'advance'
        save(savepath, saveexp + '.pr', (counts_00, counts_01, counts_10, counts_11, sigma_zz, theta_max_range),
             ('counts_00', 'counts_01', 'counts_10', 'counts_11', 'sigma_zz', 'theta_max_range'))
    if Is_save_3q is True:
        mkdir(savepath)
        saveexp = 'H_heisenberg_sigmazzz_thetamax(%g,%g,%g)_Nq%d_Nc%d_hx%g_shots%g' % (
            theta_max_range[0], theta_max_range[-1], len(theta_max_range), Nbody, Nbody, hx_fix, shots) + 'advance'
        save(savepath, saveexp + '.pr', (counts_000, counts_001, counts_010, counts_011,
                                         counts_100, counts_101, counts_110, counts_111, sigma_zzz, theta_max_range),
             ('counts_000', 'counts_001', 'counts_010', 'counts_011', 'counts_100', 'counts_101', 'counts_110',
              'counts_111',
              'sigma_zzz', 'theta_max_range'))
    if Is_plot_1q is True:
        plot_sigma_z(t_range=theta_max_range, counts_0=counts_0, counts_1=counts_1, sigma_z=sigma_z)
    if Is_plot_2q is True:
        plot_sigma_zz(t_range=theta_max_range, counts_00=counts_00,counts_01=counts_01,counts_10=counts_10,
                      counts_11=counts_11,sigma_zz=sigma_zz)
    if Is_plot_3q is True:
        plot_sigma_zzz(t_range=theta_max_range,counts_000=counts_000,counts_001=counts_001,counts_010=counts_010,
                       counts_011=counts_011,counts_100=counts_100,counts_101=counts_101,counts_110=counts_110,
                       counts_111=counts_111,sigma_zzz=sigma_zzz)
    return
#
#
if __name__ == '__main__':
    #
    scheme = 'alpha' # 'exact', 'alpha', 'trotter'
    if scheme is 'exact':
        # Obtain sigma_z sigma_zz sigma_zzz from the exact evolution
        Nqubits = 5
        Nbody = 3
        N_m = 3
        hx_1 = 0
        hx_2 = 0.99
        nhx = 100
        t_range = np.arange(0, 8, 0.1)
        hx_fix = 0.8
        loadpath = '.\\data\\H_heisenberg_hx\\exact_evolution\\Nbody%g\\' % Nbody
        savepath = '.\\data\\H_heisenberg_hx\\exact_evolution_fix_hx\\Nbody%g\\' % Nbody
        exact_evolution_results_to_sigma(t_range=t_range, h1=hx_1, h2=hx_2, nh=nhx,
                                         Nqubits=Nqubits, Nbody=Nbody, hx_fix=hx_fix,
                                         loadpath=loadpath, savepath=savepath,
                                         Is_save_1q=True, Is_save_2q=True, Is_save_3q=True,
                                         Is_plot_1q=True, Is_plot_2q=True, Is_plot_3q=True)
    elif scheme is 'trotter':
        #Obtain sigma_z sigma_zz sigma_zzz from the evolution on trotter circuit
        Nbody = 3
        hx_1 = 0
        hx_2 = 0.9
        nhx = 10
        t_range = np.arange(0, 8, 0.1)
        hx_fix = 0.8
        dt = 0.1
        shots = 1024
        loadpath_t = '.\\data\\H_heisenberg_hx\\trotter_qasm_simulator\\Nbody%g\\' % Nbody
        savepath_t = '.\\data\\H_heisenberg_hx\\trotter_qasm_simulator_fix_hx\\Nbody%g\\' % Nbody
        trotter_circuit_results_to_sigma(t_range=t_range, h1=hx_1, h2=hx_2, nh=nhx, Nbody=Nbody, hx_fix=hx_fix,
                                         dt=dt, shots=shots, loadpath=loadpath_t, savepath=savepath_t,
                                         Is_save_1q=True, Is_save_2q=True, Is_save_3q=True,
                                         Is_plot_1q=True, Is_plot_2q=True, Is_plot_3q=True)
    elif scheme is 'alpha':
        # obtain sigma_z sigma_zz sigma_zzz from the evolution on alpha circuit
        Nqubits = 5
        Nbody = 3
        shots = 1024
        theta_max_range = np.arange(0.1, 8, 0.1)  # theta max 就是我要旋转到一个角度
        n_theta_inter = 50  # 从 0 到 theta_max 之间取 10 个值。
        hx_fix = 0.8
        loadpath_a = '.\\data\\H_heisenberg_hx\\advance_qasm_simulator\\Nbody%g\\' % Nbody
        savepath_a = '.\\data\\H_heisenberg_hx\\advance_qasm_simulator_fix_hx\\Nbody%g\\' % Nbody
        alpha_circuit_results_to_sigma(theta_max_range=theta_max_range, n_theta_inter=n_theta_inter,
                                       Nqubits=Nqubits, Nbody=Nbody, hx_fix=hx_fix, loadpath=loadpath_a,
                                       savepath=savepath_a, Is_save_1q=True, Is_save_2q=True, Is_save_3q=True,
                                       Is_plot_1q=True, Is_plot_2q=True, Is_plot_3q=True, )

