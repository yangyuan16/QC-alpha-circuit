# evolution of 5 qubits Heisenberg model by trotter numerical simulators
# 1) Obtain the observation sigma_z from the trotter numerical simulators
#
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
#
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
def trotter_numerical_results_to_sigma(t1, t2, nt, t_range,hx_fix,Nbody, loadpath,savepath,
                                     Is_save_1q, Is_save_2q, Is_save_3q,
                                     Is_plot_1q, Is_plot_2q, Is_plot_3q ):
    counts_0 = []; counts_1 = []
    counts_00 = []; counts_01 = []; counts_10 = []; counts_11 = []
    counts_000 = []; counts_001 = []; counts_010 = []; counts_011 = []
    counts_100 = []; counts_101 = []; counts_110 = []; counts_111 = []
    sigma_z = []; sigma_zz = []; sigma_zzz = []
    loadexp = 'Trotter_numerical_hx%g_Nbody%g_t(%g,%g,%g)' % (hx_fix, Nbody, t1, t2, nt) + '.pr'
    print(loadpath + loadexp)
    data = bf.load_pr(loadpath + loadexp)
    counts_sum = data['counts']
    for it in range(nt):
        c0 = counts_sum['000'][it] + counts_sum['001'][it] + counts_sum['010'][it] + counts_sum['011'][it]
        c1 = counts_sum['100'][it] + counts_sum['101'][it] + counts_sum['110'][it] + counts_sum['111'][it]
        c00 = counts_sum['000'][it] + counts_sum['001'][it]
        c01 = counts_sum['010'][it] + counts_sum['011'][it]
        c10 = counts_sum['100'][it] + counts_sum['101'][it]
        c11 = counts_sum['110'][it] + counts_sum['111'][it]
        c000 = counts_sum['000'][it]; c001 = counts_sum['001'][it]
        c010 = counts_sum['010'][it]; c011 = counts_sum['011'][it]
        c100 = counts_sum['100'][it]; c101 = counts_sum['101'][it]
        c110 = counts_sum['110'][it]; c111 = counts_sum['111'][it]
        #
        counts_0.append(c0); counts_1.append(c1)
        counts_00.append(c00); counts_01.append(c01); counts_10.append(c10); counts_11.append(c11)
        counts_000.append(c000); counts_001.append(c001); counts_010.append(c010); counts_011.append(c011)
        counts_100.append(c100); counts_101.append(c101); counts_110.append(c110); counts_111.append(c111)
        sigma_z.append(c0 - c1)
        sigma_zz.append(c00 - c01 - c10 + c11)
        sigma_zzz.append(c000 - c001 - c010 + c011 - c100 + c101 + c110 - c111)
    #
    if Is_save_1q is True:
        mkdir(savepath)
        saveexp = 'Trotter_numerical_sigmaz_t(%g,%g,%g)_Nbody%g_hx%g' % (t1, t2, nt, Nbody, hx_fix)
        save(savepath, saveexp + '.pr', (counts_0, counts_1, sigma_z, t_range),
             ('counts_0', 'counts_1', 'sigma_z', 't_range'))
    if Is_save_2q is True:
        mkdir(savepath)
        saveexp = 'Trotter_numerical_sigmazz_t(%g,%g,%g)_Nbody%g_hx%g' % (t1, t2, nt, Nbody, hx_fix)
        save(savepath, saveexp + '.pr', (counts_00, counts_01, counts_10, counts_11,
                                         sigma_zz, t_range),
             ('counts_00', 'counts_01', 'counts_10', 'counts_11', 'sigma_zz', 't_range'))
    if Is_save_3q is True:
        mkdir(savepath)
        saveexp = 'Tortter_numerical_sigmazzz_t(%g,%g,%g)_Nbody%d_hx%g' % (t1, t2, nt, Nbody, hx_fix)
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

if __name__ == '__main__':
    hx_fix = 0.5
    Nbody = 5
    t1 = 0
    t2 = 7.8
    nt = 40
    t_range = np.arange(0,8,0.2)
    loadpath = './data/H_heisenberg_hx/trotter_numerical/Nbody%g/' % Nbody
    savepath = './data/H_heisenberg_hx/trotter_numerical/Nbody%g/' % Nbody
    trotter_numerical_results_to_sigma(t1=t1,t2=t2,nt=nt, t_range=t_range,
                                       hx_fix=hx_fix,
                                       Nbody=Nbody,
                                       loadpath=loadpath,
                                       savepath=savepath,
                                       Is_save_1q=True, Is_save_2q=True, Is_save_3q=True,
                                       Is_plot_1q=True, Is_plot_2q=True, Is_plot_3q=True
                                       )