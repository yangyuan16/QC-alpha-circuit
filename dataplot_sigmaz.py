# plot fig.2 in the article
#
#============================================
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import numpy as np
import library.BasicFunctions as bf
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from mpl_toolkits.axes_grid1 import make_axes_locatable
#
fig = plt.figure(figsize=(8,8))
#plt.figure(facecolor='blue',edgecolor='black') # 设置画布的颜色。
params={
    'axes.labelsize': '30',
    'xtick.labelsize':'20',
    'ytick.labelsize':'20',
    'ytick.direction':'in',
    'xtick.direction':'in',
    'lines.linewidth':6 ,
    'legend.fontsize': '27'
   # 'figure.figsize'   : '12, 9'    # set figure size
}
pylab.rcParams.update(params)  #set figure parameter 更新绘图的参数

ISsave = True
####得到子图
ax1 = plt.axes([0.1,0.58,0.35,0.32])
ax2 = plt.axes([0.6,0.58,0.35,0.32])
ax3 = plt.axes([0.1,0.1,0.35,0.32])
ax4 = plt.axes([0.6,0.1,0.35,0.32])
#ax3 = plt.axes([0.61,0.17,0.26,0.78])  ##  原点坐标和长宽
#plt.subplots_adjust(left=0.1, bottom=0.1, right=0.98, top=0.96, wspace=0.32, hspace=0.26)
###################################################################
###选择子图
plt.sca(ax1)  ##选择对ax1进行绘图
ax1=plt.gca() #获得坐标轴的句柄
ax1_ = ax1.twiny()  # 共享 y 轴
#====================================
# 获取数据
Nbody = 3
hx_fix = 0.5
t1 = 0; t2 = 7.9;  nt = 80
# data from exact evolution
loadpath1 = '.\\data\\H_heisenberg_hx\\exact_evolution_fix_hx\\Nbody%g\\'%Nbody
loadexp1 = 'H_heisenberg_sigmaz_t(%g,%g,%g)_Nq%d_Nc%d_hx%g' % (t1, t2, nt, Nbody, Nbody, hx_fix) + 'exact' + '.pr'
print(loadpath1 + loadexp1)
data_exact = bf.load_pr(loadpath1 + loadexp1)
sigmaz_exact = data_exact['sigma_z']
t_range_exact = data_exact['t_range']
# data from trotter evolution
dt = 0.1; shots = 1024
loadpath2 = '.\\data\\H_heisenberg_hx\\trotter_qasm_simulator_fix_hx\\Nbody%g\\'%Nbody
loadexp2 = 'H_heisenberg_sigmaz_t(%g,%g,%g)_Nq%d_Nc%d_hx%g_dt%g_shots%g' % (t1,t2,nt,Nbody,Nbody,hx_fix,dt,shots) + 'trotter' + '.pr'
print(loadpath2 + loadexp2)
data_trotter = bf.load_pr(loadpath2 + loadexp2)
sigmaz_trotter = data_trotter['sigma_z']
t_range_trotter = data_trotter['t_range']
# data from advance circuit
theta1 = 0.1; theta2 = 7.9; ntheta = 79
loadpath3 = '.\\data\\H_heisenberg_hx\\advance_qasm_simulator_fix_hx\\Nbody%g\\'%Nbody
loadexp3 = 'H_heisenberg_sigmaz_thetamax(%g,%g,%g)_Nq%d_Nc%d_hx%g_shots%g' % (theta1,theta2,ntheta,Nbody,Nbody,hx_fix,shots) + 'advance' + '.pr'
print(loadpath3 + loadexp3)
data_advance =  bf.load_pr(loadpath3 + loadexp3)
sigmaz_advance = data_advance['sigma_z']
theta_advance = data_advance['theta_max_range'] * hx_fix
#
L3_,=ax1_.plot(theta_advance[::4], sigmaz_advance[::4], label=r'$\alpha$-circuit', ls='--', lw=3, color='blue',
             marker='o', alpha=1, markersize=10, markeredgewidth=1.5, markeredgecolor='blue', markerfacecolor='none')

L1,=ax1.plot(t_range_exact, sigmaz_exact, label=r'ED', ls='-', lw=5, color='red',
             marker='o', alpha=1, markersize=0, markeredgewidth=1.5, markeredgecolor='red', markerfacecolor='w')

L2,=ax1.plot(t_range_trotter[::4], sigmaz_trotter[::4], label=r'Trotter', ls='--', lw=3, color='orange',
             marker='o', alpha=1, markersize=10, markeredgewidth=1.5, markeredgecolor='orange', markerfacecolor='w')

# 画 3 根虚线
L3,=ax1.plot([0,8], [0.5,0.5], label=r'Trotter', ls='--', lw=1, color='grey',
             marker='o', alpha=0.5, markersize=0, markeredgewidth=1.5, markeredgecolor='black', markerfacecolor='w')
L4,=ax1.plot([0,8], [0,0], label=r'Trotter', ls='--', lw=1, color='grey',
             marker='o', alpha=0.5, markersize=0, markeredgewidth=1.5, markeredgecolor='black', markerfacecolor='w')
L5,=ax1.plot([0,8], [-0.5,-0.5], label=r'Trotter', ls='--', lw=1, color='grey',
             marker='o', alpha=0.5, markersize=0, markeredgewidth=1.5, markeredgecolor='black', markerfacecolor='w')


####图例设置
#label = ["Mg", "Mo", "Me","Ms"]
legfont = {'family' : 'Times New Roman','weight' : 'normal','size': 16, }###图例字体的大小###ncol 设置列的数量，使显示扁平化，当要表示的线段特别多的时候会有用
legend1=plt.legend(handles=[L1,L2,L3_], loc = 4, bbox_to_anchor=(0.98, 0.58),ncol = 1,prop=legfont,markerscale=1,fancybox=None,shadow=None,frameon=False)
#legend2=plt.legend(handles=[Le, Ls_a, Ls_b], loc = 4, bbox_to_anchor=(0.85, -0.05),ncol = 1,prop=legfont,markerscale=1,fancybox=None,shadow=None,frameon=False)
#plt.gca().add_artist(legend1)#####把图例legend1重新加载回来
## bty 图例框是否画出，o为画出，默认为n不画出
## markerscale 控制图例中maker的大小
## bbox_to_anchor被赋予的二元组中，num1用于控制legend的左右移动，值越大越向右边移动，
# num2用于控制legend的上下移动，值越大，越向上移动。用于微调图例的位置
#=======================================================================================================================
label_x = r't'
label_y = r'$\sigma^z(t,h_x)$'
label_x_= r'$\theta$'
ax1.set_xlabel(label_x, size = 14)
ax1.set_ylabel(label_y, size = 14)
ax1_.set_xlabel(label_x_, size=14, rotation = 0)
#ax2.set_title('Distance Matrix', size = 14)
ax1.tick_params(labelsize = 15) # 设置坐标刻度对应数字的大小
ax1_.tick_params(labelsize = 15)
#plt.xlim(0,8)
plt.ylim(-1,1)
ax1.set_xlim([0,8])
ax1.set_xticks([0,2,4,6,8])
ax1.set_yticks([-1,-0.5,0,0.5,1])

ax1_.set_xlim([0,4])
ax1_.set_xticks([0,1,2,3,4])

#==============================================================
ax1.text(0.3,-0.87, r'$\mathrm{(a)}$', fontsize=18)
#ax1.text(0.1,0.9, r'$\mathrm{perplexity = 18}$', fontsize=12)
# ax1.text(0.1,0.8, r'$\mathrm{n_{iter} = 5000}$', fontsize=12)
ax1.text(4,0.1, r'$h_x = 0.5$', fontsize = 16, color='black')
#ax1.text(5.5,0.53, r'Heisenberg', fontsize = 15, color='black')
#ax1.text(5.5,0.5, r'S=1', fontsize = 15, color='black')
#ax1.text(5.5,0.53, r'uniform', fontsize = 15, color='black')
ax1.text(8.1,-0.13, r'$\sigma^z(\theta)$', fontsize = 16, color='black', rotation = 90)
#=============================================================
# 坐标轴设置第一层
labels = ax1.get_xticklabels() + ax1.get_yticklabels()
#[label.set_fontname('Times New Roman') for label in labels]###设置ticket labled的字体格式
ax1.xaxis.set_minor_locator(MultipleLocator(50))###设置次刻度的间隔
ax1.yaxis.set_minor_locator(MultipleLocator(10))###设置次刻度的间隔
ax1.xaxis.set_major_formatter(FormatStrFormatter('%1.0f'))###设置X轴标签文本格式
ax1.yaxis.set_major_formatter(FormatStrFormatter('%1.1f'))###设置Y轴标签文本格式

#=====坐标轴的第二层： 坐标轴的设置
ax1.spines['bottom'].set_linewidth(2) ###设置底部坐标轴的粗细
ax1.spines['left'].set_linewidth(2)   ###设置左边坐标轴的粗细
ax1.spines['right'].set_linewidth(2)  ###设置右边坐标轴的粗细
ax1.spines['top'].set_linewidth(2)    ###设置上部坐标轴的粗细
#ax1.spines['right'].set_color('none')# 将右边上边的两条边颜色设置为空 其实就相当于抹掉这两条边
#ax1.spines['top'].set_color('none')
#====坐标轴的第三层：  刻度线的设置
for line in ax1.xaxis.get_ticklines():
    #line is a Line2D instance
    #line.set_color('green')
    line.set_markersize(2)####设置刻度线的长度
    line.set_markeredgewidth(1.5)####设置刻度线的宽度
for line in ax1.yaxis.get_ticklines():
    # line is a Line2D instance
    #line.set_color('green')
    line.set_markersize(2.5)####设置刻度线的长度
    line.set_markeredgewidth(1.5)####设置刻度线的宽度

#=====坐标轴的第四层： 坐标轴颜色
#ax1.spines['left'].set_color('red')
#ax1.patch.set_facecolor("gray")   #设置ax1区域背景颜色
#ax1.patch.set_alpha(0.5)         #设置ax1区域背景颜色透明度
######################
# 对 ax_ 进行设置
labels_ = ax1_.get_xticklabels() + ax1_.get_yticklabels()
#[label_.set_fontname('Times New Roman') for label_ in labels_]###设置ticket labled的字体格式
ax1_.xaxis.set_minor_locator(MultipleLocator(50))###设置次刻度的间隔
ax1_.yaxis.set_minor_locator(MultipleLocator(10))###设置次刻度的间隔
ax1_.xaxis.set_major_formatter(FormatStrFormatter('%1.0f'))###设置X轴标签文本格式
ax1_.yaxis.set_major_formatter(FormatStrFormatter('%1.1f'))###设置Y轴标签文本格式

for line in ax1_.yaxis.get_ticklines():
    # line is a Line2D instance
    #line.set_color('green')
    line.set_markersize(2.5)####设置刻度线的长度
    line.set_markeredgewidth(1.5)####设置刻度线的宽度

ax1_.spines['left'].set_linewidth(0)
ax1_.spines['right'].set_linewidth(2.5)  ###设置右边坐标轴的粗细。
ax1_.spines['top'].set_linewidth(2.5)
ax1_.spines['bottom'].set_linewidth(0)  ###设置下边坐标轴的粗细。
ax1_.spines['top'].set_color('blue') ### 设置右边坐标轴的颜色。
ax1_.spines['right'].set_color('blue') ### 设置右边坐标轴的颜色。
#=========================================================================

#=============================================================
###选择子图
plt.sca(ax2)  ##选择对ax1进行绘图
ax2=plt.gca() #获得坐标轴的句柄
ax2_ = ax2.twiny()
#====================================
# 获取数据
Nbody = 3
hx_fix = 0.8
t1 = 0; t2 = 7.9;  nt = 80
# data from exact evolution
loadpath1 = '.\\data\\H_heisenberg_hx\\exact_evolution_fix_hx\\Nbody%g\\'%Nbody
loadexp1 = 'H_heisenberg_sigmaz_t(%g,%g,%g)_Nq%d_Nc%d_hx%g' % (t1, t2, nt, Nbody, Nbody, hx_fix) + 'exact' + '.pr'
print(loadpath1 + loadexp1)
data_exact = bf.load_pr(loadpath1 + loadexp1)
sigmaz_exact = data_exact['sigma_z']
t_range_exact = data_exact['t_range']
# data from trotter evolution
dt = 0.1; shots = 1024
loadpath2 = '.\\data\\H_heisenberg_hx\\trotter_qasm_simulator_fix_hx\\Nbody%g\\'%Nbody
loadexp2 = 'H_heisenberg_sigmaz_t(%g,%g,%g)_Nq%d_Nc%d_hx%g_dt%g_shots%g' % (t1,t2,nt,Nbody,Nbody,hx_fix,dt,shots) + 'trotter' + '.pr'
print(loadpath2 + loadexp2)
data_trotter = bf.load_pr(loadpath2 + loadexp2)
sigmaz_trotter = data_trotter['sigma_z']
t_range_trotter = data_trotter['t_range']
# data from advance circuit
theta1 = 0.1; theta2 = 7.9; ntheta = 79
loadpath3 = '.\\data\\H_heisenberg_hx\\advance_qasm_simulator_fix_hx\\Nbody%g\\'%Nbody
loadexp3 = 'H_heisenberg_sigmaz_thetamax(%g,%g,%g)_Nq%d_Nc%d_hx%g_shots%g' % (theta1,theta2,ntheta,Nbody,Nbody,hx_fix,shots) + 'advance' + '.pr'
print(loadpath3 + loadexp3)
data_advance =  bf.load_pr(loadpath3 + loadexp3)
sigmaz_advance = data_advance['sigma_z']
theta_advance = data_advance['theta_max_range'] * hx_fix

L3_,=ax2_.plot(theta_advance[::4], sigmaz_advance[::4], label=r'$\alpha$-circuit', ls='--', lw=3, color='blue',
             marker='o', alpha=1, markersize=10, markeredgewidth=1.5, markeredgecolor='blue', markerfacecolor='none')

L1,=ax2.plot(t_range_exact, sigmaz_exact, label=r'ED', ls='-', lw=5, color='red',
             marker='o', alpha=1, markersize=0, markeredgewidth=1.5, markeredgecolor='red', markerfacecolor='w')

L2,=ax2.plot(t_range_trotter[::4], sigmaz_trotter[::4], label=r'Trotter', ls='--', lw=3, color='orange',
             marker='o', alpha=1, markersize=10, markeredgewidth=1.5, markeredgecolor='orange', markerfacecolor='w')

# 画 3 根虚线
L3,=ax2.plot([0,8], [0.5,0.5], label=r'Trotter', ls='--', lw=1, color='grey',
             marker='o', alpha=0.5, markersize=0, markeredgewidth=1.5, markeredgecolor='black', markerfacecolor='w')
L4,=ax2.plot([0,8], [0,0], label=r'Trotter', ls='--', lw=1, color='grey',
             marker='o', alpha=0.5, markersize=0, markeredgewidth=1.5, markeredgecolor='black', markerfacecolor='w')
L5,=ax2.plot([0,8], [-0.5,-0.5], label=r'Trotter', ls='--', lw=1, color='grey',
             marker='o', alpha=0.5, markersize=0, markeredgewidth=1.5, markeredgecolor='black', markerfacecolor='w')

####图例设置
#label = ["Mg", "Mo", "Me","Ms"]
#legfont = {'family' : 'Times New Roman','weight' : 'normal','size': 16, }###图例字体的大小###ncol 设置列的数量，使显示扁平化，当要表示的线段特别多的时候会有用
#legend1=plt.legend(handles=[L1,L2,L3_], loc = 4, bbox_to_anchor=(0.98, 0.58),ncol = 1,prop=legfont,markerscale=1,fancybox=None,shadow=None,frameon=False)
#legend2=plt.legend(handles=[Le, Ls_a, Ls_b], loc = 4, bbox_to_anchor=(0.85, -0.05),ncol = 1,prop=legfont,markerscale=1,fancybox=None,shadow=None,frameon=False)
#plt.gca().add_artist(legend1)#####把图例legend1重新加载回来
## bty 图例框是否画出，o为画出，默认为n不画出
## markerscale 控制图例中maker的大小
## bbox_to_anchor被赋予的二元组中，num1用于控制legend的左右移动，值越大越向右边移动，
# num2用于控制legend的上下移动，值越大，越向上移动。用于微调图例的位置
#=======================================================================================================================
label_x = r't'
label_y = r'$\sigma^z(t,h_x)$'
label_x_= r'$\theta$'
ax2.set_xlabel(label_x, size = 14)
ax2.set_ylabel(label_y, size = 14)
ax2_.set_xlabel(label_x_, size=14, rotation = 0)
#ax2.set_title('Distance Matrix', size = 14)
ax2.tick_params(labelsize = 15) # 设置坐标刻度对应数字的大小
ax2_.tick_params(labelsize = 15)
#plt.xlim(0,8)
plt.ylim(-1,1)
ax2.set_xlim([0,8])
ax2.set_xticks([0,2,4,6,8])
ax2.set_yticks([-1,-0.5,0,0.5,1])

ax2_.set_xlim([0,6.4])
ax2_.set_xticks([0,1.6,3.2,4.8,6.4])

#==============================================================
ax2.text(0.3,-0.87, r'$\mathrm{(b)}$', fontsize=18)
#ax1.text(0.1,0.9, r'$\mathrm{perplexity = 18}$', fontsize=12)
# ax1.text(0.1,0.8, r'$\mathrm{n_{iter} = 5000}$', fontsize=12)
ax2.text(2,0.52, r'$h_x = 0.8$', fontsize = 16, color='black')
#ax1.text(5.5,0.53, r'Heisenberg', fontsize = 15, color='black')
#ax1.text(5.5,0.5, r'S=1', fontsize = 15, color='black')
#ax1.text(5.5,0.53, r'uniform', fontsize = 15, color='black')
ax2.text(8.1,-0.13, r'$\sigma^z(\theta)$', fontsize = 16, color='black', rotation = 90)
#=============================================================
# 坐标轴设置第一层
labels = ax2.get_xticklabels() + ax2.get_yticklabels()
#[label.set_fontname('Times New Roman') for label in labels]###设置ticket labled的字体格式
ax2.xaxis.set_minor_locator(MultipleLocator(50))###设置次刻度的间隔
ax2.yaxis.set_minor_locator(MultipleLocator(10))###设置次刻度的间隔
ax2.xaxis.set_major_formatter(FormatStrFormatter('%1.0f'))###设置X轴标签文本格式
ax2.yaxis.set_major_formatter(FormatStrFormatter('%1.1f'))###设置Y轴标签文本格式

#=====坐标轴的第二层： 坐标轴的设置
ax2.spines['bottom'].set_linewidth(2) ###设置底部坐标轴的粗细
ax2.spines['left'].set_linewidth(2)   ###设置左边坐标轴的粗细
ax2.spines['right'].set_linewidth(2)  ###设置右边坐标轴的粗细
ax2.spines['top'].set_linewidth(2)    ###设置上部坐标轴的粗细
#ax2.spines['right'].set_color('none')# 将右边上边的两条边颜色设置为空 其实就相当于抹掉这两条边
#ax2.spines['top'].set_color('none')
#====坐标轴的第三层：  刻度线的设置
for line in ax2.xaxis.get_ticklines():
    #line is a Line2D instance
    #line.set_color('green')
    line.set_markersize(2)####设置刻度线的长度
    line.set_markeredgewidth(1.5)####设置刻度线的宽度
for line in ax2.yaxis.get_ticklines():
    # line is a Line2D instance
    #line.set_color('green')
    line.set_markersize(2.5)####设置刻度线的长度
    line.set_markeredgewidth(1.5)####设置刻度线的宽度

#=====坐标轴的第四层： 坐标轴颜色
#ax2.spines['left'].set_color('red')
#ax2.patch.set_facecolor("gray")   #设置ax1区域背景颜色
#ax2.patch.set_alpha(0.5)         #设置ax1区域背景颜色透明度
######################
# 对 ax_ 进行设置
labels_ = ax2_.get_xticklabels() + ax2_.get_yticklabels()
#[label_.set_fontname('Times New Roman') for label_ in labels_]###设置ticket labled的字体格式
ax2_.xaxis.set_minor_locator(MultipleLocator(50))###设置次刻度的间隔
ax2_.yaxis.set_minor_locator(MultipleLocator(10))###设置次刻度的间隔
ax2_.xaxis.set_major_formatter(FormatStrFormatter('%1.1f'))###设置X轴标签文本格式
ax2_.yaxis.set_major_formatter(FormatStrFormatter('%1.1f'))###设置Y轴标签文本格式

for line in ax2_.yaxis.get_ticklines():
    # line is a Line2D instance
    #line.set_color('green')
    line.set_markersize(2.5)####设置刻度线的长度
    line.set_markeredgewidth(1.5)####设置刻度线的宽度

ax2_.spines['left'].set_linewidth(0)
ax2_.spines['right'].set_linewidth(2.5)  ###设置右边坐标轴的粗细。
ax2_.spines['top'].set_linewidth(2.5)
ax2_.spines['bottom'].set_linewidth(0)  ###设置下边坐标轴的粗细。
ax2_.spines['top'].set_color('blue') ### 设置右边坐标轴的颜色。
ax2_.spines['right'].set_color('blue') ### 设置右边坐标轴的颜色。
#=========================================================================

#=============================================================
###选择子图
plt.sca(ax3)  ##选择对ax1进行绘图
ax3=plt.gca() #获得坐标轴的句柄
ax3_ = ax3.twiny()
# 获取数据
Nqubits = 5
Nbody = 3
t_fix = 5
hx1 = 0; hx2 = 0.98;  nhx = 50
# data from exact evolution
loadpath1 = '.\\data\\H_heisenberg_hx\\exact_evolution\\Nbody%g\\'%Nbody
loadexp1 = 'H_heisenberg_hx(%g,%g,%g)_Nq%d_Nc%d_t%g' % (hx1, hx2, nhx, Nqubits, Nbody, t_fix) + 'exact' + '.pr'
print(loadpath1 + loadexp1)
data_exact = bf.load_pr(loadpath1 + loadexp1)
sigmaz_exact = np.array(data_exact['counts']['000']) + np.array(data_exact['counts']['001']) + \
               np.array(data_exact['counts']['010']) + np.array(data_exact['counts']['011']) - \
               np.array(data_exact['counts']['100']) - np.array(data_exact['counts']['101']) - \
               np.array(data_exact['counts']['110']) - np.array(data_exact['counts']['111'])
hx_range_exact = data_exact['hx']

# data from trotter evolution
dt = 0.1; shots = 1024
loadpath2 = '.\\data\\H_heisenberg_hx\\trotter_qasm_simulator\\Nbody%g\\'%Nbody
loadexp2 = 'H_heisenberg_hx(%g,%g,%g)_Nq%d_Nc%d_t%g_dt%g_shots%g' % (hx1,hx2,nhx,Nbody,Nbody,t_fix,dt,shots) + 'trotter' + '.pr'
print(loadpath2 + loadexp2)
data_trotter = bf.load_pr(loadpath2 + loadexp2)

sigmaz_trotter = np.array(data_trotter['counts']['000']) + np.array(data_trotter['counts']['001']) + \
                 np.array(data_trotter['counts']['010']) + np.array(data_trotter['counts']['011']) - \
                 np.array(data_trotter['counts']['100']) - np.array(data_trotter['counts']['101']) - \
                 np.array(data_trotter['counts']['110']) - np.array(data_trotter['counts']['111'])
hx_range_trotter = data_trotter['hx']
# data from advance circuit
theta1 = 0; theta2 = t_fix; ntheta = 50
loadpath3 = '.\\data\\H_heisenberg_hx\\advance_qasm_simulator\\Nbody%g\\'%Nbody
loadexp3 = 'H_heisenberg_theta(%g,%g,%g)_Nq%d_Nc%d_shots%g' % (theta1,theta2,ntheta,Nqubits,Nbody,shots) + 'advance' + '.pr'
print(loadpath3 + loadexp3)
data_advance =  bf.load_pr(loadpath3 + loadexp3)
sigmaz_advance = np.array(data_advance['counts']['000']) + np.array(data_advance['counts']['001']) + \
               np.array(data_advance['counts']['010']) + np.array(data_advance['counts']['011']) - \
               np.array(data_advance['counts']['100']) - np.array(data_advance['counts']['101']) - \
               np.array(data_advance['counts']['110']) - np.array(data_advance['counts']['111'])
theta_range = data_advance['theta']

L3_,=ax3_.plot(theta_range[::2], sigmaz_advance[::2], label=r'$\alpha$-circuit', ls='--', lw=3, color='seagreen',
             marker='o', alpha=1, markersize=10, markeredgewidth=1.5, markeredgecolor='seagreen', markerfacecolor='none')

L1,=ax3.plot(hx_range_exact, sigmaz_exact, label=r'ED', ls='-', lw=5, color='magenta',
             marker='o', alpha=1, markersize=0, markeredgewidth=1.5, markeredgecolor='magenta', markerfacecolor='w')

L2,=ax3.plot(hx_range_trotter[::4], sigmaz_trotter[::4], label=r'Trotter', ls='--', lw=3, color='darkviolet',
             marker='o', alpha=1, markersize=10, markeredgewidth=1.5, markeredgecolor='darkviolet', markerfacecolor='w')

# 画 3 根虚线
L3,=ax3.plot([0,1], [0.5,0.5], label=r'Trotter', ls='--', lw=1, color='grey',
             marker='o', alpha=0.5, markersize=0, markeredgewidth=1.5, markeredgecolor='black', markerfacecolor='w')
L4,=ax3.plot([0,1], [0,0], label=r'Trotter', ls='--', lw=1, color='grey',
             marker='o', alpha=0.5, markersize=0, markeredgewidth=1.5, markeredgecolor='black', markerfacecolor='w')
L5,=ax3.plot([0,1], [-0.5,-0.5], label=r'Trotter', ls='--', lw=1, color='grey',
             marker='o', alpha=0.5, markersize=0, markeredgewidth=1.5, markeredgecolor='black', markerfacecolor='w')
####图例设置

#label = ["Mg", "Mo", "Me","Ms"]
legfont = {'family' : 'Times New Roman','weight' : 'normal','size': 16, }###图例字体的大小###ncol 设置列的数量，使显示扁平化，当要表示的线段特别多的时候会有用
legend1=plt.legend(handles=[L1,L2,L3_], loc = 4, bbox_to_anchor=(0.88, 0.58),ncol = 1,prop=legfont,markerscale=1,fancybox=None,shadow=None,frameon=False)
#legend2=plt.legend(handles=[Le, Ls_a, Ls_b], loc = 4, bbox_to_anchor=(0.85, -0.05),ncol = 1,prop=legfont,markerscale=1,fancybox=None,shadow=None,frameon=False)
#plt.gca().add_artist(legend1)#####把图例legend1重新加载回来
## bty 图例框是否画出，o为画出，默认为n不画出
## markerscale 控制图例中maker的大小
## bbox_to_anchor被赋予的二元组中，num1用于控制legend的左右移动，值越大越向右边移动，
# num2用于控制legend的上下移动，值越大，越向上移动。用于微调图例的位置
#=======================================================================================================================
label_x = r'$h_x$'
label_y = r'$\sigma^z(t,h_x)$'
label_x_= r'$\theta$'
ax3.set_xlabel(label_x, size = 14)
ax3.set_ylabel(label_y, size = 14)
ax3_.set_xlabel(label_x_, size=14, rotation = 0)
#ax2.set_title('Distance Matrix', size = 14)
ax3.tick_params(labelsize = 15) # 设置坐标刻度对应数字的大小
ax3_.tick_params(labelsize = 15)
#plt.xlim(0,8)
plt.ylim(-1,1)
ax3.set_xlim([0,1])
ax3.set_xticks([0,0.2,0.4,0.6,0.8,1])
ax3.set_yticks([-1,-0.5,0,0.5,1])

ax3_.set_xlim([0,4])
ax3_.set_xticks([0,1,2,3,4,5])

#==============================================================
ax3.text(0.03,-0.87, r'$\mathrm{(c)}$', fontsize=18)
#ax1.text(0.1,0.9, r'$\mathrm{perplexity = 18}$', fontsize=12)
# ax1.text(0.1,0.8, r'$\mathrm{n_{iter} = 5000}$', fontsize=12)
ax3.text(0.45, 0.1, r'$t = 5$', fontsize = 16, color='black')
#ax1.text(5.5,0.53, r'Heisenberg', fontsize = 15, color='black')
#ax1.text(5.5,0.5, r'S=1', fontsize = 15, color='black')
#ax1.text(5.5,0.53, r'uniform', fontsize = 15, color='black')
ax3.text(1.03,-0.13, r'$\sigma^z(\theta)$', fontsize = 16, color='black', rotation = 90)
#=============================================================
# 坐标轴设置第一层
labels = ax3.get_xticklabels() + ax3.get_yticklabels()
#[label.set_fontname('Times New Roman') for label in labels]###设置ticket labled的字体格式
ax3.xaxis.set_minor_locator(MultipleLocator(50))###设置次刻度的间隔
ax3.yaxis.set_minor_locator(MultipleLocator(10))###设置次刻度的间隔
ax3.xaxis.set_major_formatter(FormatStrFormatter('%1.1f'))###设置X轴标签文本格式
ax3.yaxis.set_major_formatter(FormatStrFormatter('%1.1f'))###设置Y轴标签文本格式

#=====坐标轴的第二层： 坐标轴的设置
ax3.spines['bottom'].set_linewidth(2) ###设置底部坐标轴的粗细
ax3.spines['left'].set_linewidth(2)   ###设置左边坐标轴的粗细
ax3.spines['right'].set_linewidth(2)  ###设置右边坐标轴的粗细
ax3.spines['top'].set_linewidth(2)    ###设置上部坐标轴的粗细
#ax3.spines['right'].set_color('none')# 将右边上边的两条边颜色设置为空 其实就相当于抹掉这两条边
#ax3.spines['top'].set_color('none')
#====坐标轴的第三层：  刻度线的设置
for line in ax3.xaxis.get_ticklines():
    #line is a Line2D instance
    #line.set_color('green')
    line.set_markersize(2)####设置刻度线的长度
    line.set_markeredgewidth(1.5)####设置刻度线的宽度
for line in ax3.yaxis.get_ticklines():
    # line is a Line2D instance
    #line.set_color('green')
    line.set_markersize(2.5)####设置刻度线的长度
    line.set_markeredgewidth(1.5)####设置刻度线的宽度

#=====坐标轴的第四层： 坐标轴颜色
#ax3.spines['left'].set_color('red')
#ax3.patch.set_facecolor("gray")   #设置ax3区域背景颜色
#ax3.patch.set_alpha(0.5)         #设置ax3区域背景颜色透明度
######################
# 对 ax_ 进行设置
labels_ = ax3_.get_xticklabels() + ax3_.get_yticklabels()
#[label_.set_fontname('Times New Roman') for label_ in labels_]###设置ticket labled的字体格式
ax3_.xaxis.set_minor_locator(MultipleLocator(50))###设置次刻度的间隔
ax3_.yaxis.set_minor_locator(MultipleLocator(10))###设置次刻度的间隔
ax3_.xaxis.set_major_formatter(FormatStrFormatter('%1.0f'))###设置X轴标签文本格式
ax3_.yaxis.set_major_formatter(FormatStrFormatter('%1.1f'))###设置Y轴标签文本格式

for line in ax3_.yaxis.get_ticklines():
    # line is a Line2D instance
    #line.set_color('green')
    line.set_markersize(2.5)####设置刻度线的长度
    line.set_markeredgewidth(1.5)####设置刻度线的宽度

ax3_.spines['left'].set_linewidth(0)
ax3_.spines['right'].set_linewidth(2.5)  ###设置右边坐标轴的粗细。
ax3_.spines['top'].set_linewidth(2.5)
ax3_.spines['bottom'].set_linewidth(0)  ###设置下边坐标轴的粗细。
ax3_.spines['top'].set_color('seagreen') ### 设置右边坐标轴的颜色。
ax3_.spines['right'].set_color('seagreen') ### 设置右边坐标轴的颜色。
#=========================================================================

###选择子图
plt.sca(ax4)  ##选择对ax1进行绘图
ax4=plt.gca() #获得坐标轴的句柄
ax4_ = ax4.twiny()
# 获取数据
Nbody = 3
Nqubits = 5
t_fix = 8
hx1 = 0; hx2 = 0.98;  nhx = 50
# data from exact evolution
loadpath1 = '.\\data\\H_heisenberg_hx\\exact_evolution\\Nbody%g\\'%Nbody
loadexp1 = 'H_heisenberg_hx(%g,%g,%g)_Nq%d_Nc%d_t%g' % (hx1, hx2, nhx, Nqubits, Nbody, t_fix) + 'exact' + '.pr'
print(loadpath1 + loadexp1)
data_exact = bf.load_pr(loadpath1 + loadexp1)
sigmaz_exact = np.array(data_exact['counts']['000']) + np.array(data_exact['counts']['001']) + \
               np.array(data_exact['counts']['010']) + np.array(data_exact['counts']['011']) - \
               np.array(data_exact['counts']['100']) - np.array(data_exact['counts']['101']) - \
               np.array(data_exact['counts']['110']) - np.array(data_exact['counts']['111'])
hx_range_exact = data_exact['hx']

# data from trotter evolution
dt = 0.1; shots = 1024
loadpath2 = '.\\data\\H_heisenberg_hx\\trotter_qasm_simulator\\Nbody%g\\' % Nbody
loadexp2 = 'H_heisenberg_hx(%g,%g,%g)_Nq%d_Nc%d_t%g_dt%g_shots%g' % (hx1,hx2,nhx,Nbody,Nbody,t_fix,dt,shots) + 'trotter' + '.pr'
print(loadpath2 + loadexp2)
data_trotter = bf.load_pr(loadpath2 + loadexp2)

sigmaz_trotter = np.array(data_trotter['counts']['000']) + np.array(data_trotter['counts']['001']) + \
                 np.array(data_trotter['counts']['010']) + np.array(data_trotter['counts']['011']) - \
                 np.array(data_trotter['counts']['100']) - np.array(data_trotter['counts']['101']) - \
                 np.array(data_trotter['counts']['110']) - np.array(data_trotter['counts']['111'])
hx_range_trotter = data_trotter['hx']
# data from advance circuit
theta1 = 0; theta2 = t_fix; ntheta = 50
loadpath3 = '.\\data\\H_heisenberg_hx\\advance_qasm_simulator\\Nbody%g\\' % Nbody
loadexp3 = 'H_heisenberg_theta(%g,%g,%g)_Nq%d_Nc%d_shots%g' % (theta1,theta2,ntheta,Nqubits,Nbody,shots) + 'advance' + '.pr'
print(loadpath3 + loadexp3)
data_advance =  bf.load_pr(loadpath3 + loadexp3)
sigmaz_advance = np.array(data_advance['counts']['000']) + np.array(data_advance['counts']['001']) + \
               np.array(data_advance['counts']['010']) + np.array(data_advance['counts']['011']) - \
               np.array(data_advance['counts']['100']) - np.array(data_advance['counts']['101']) - \
               np.array(data_advance['counts']['110']) - np.array(data_advance['counts']['111'])
theta_range = data_advance['theta']

L3_,=ax4_.plot(theta_range[::2], sigmaz_advance[::2], label=r'$\alpha$-circuit', ls='--', lw=3, color='seagreen',
             marker='o', alpha=1, markersize=10, markeredgewidth=1.5, markeredgecolor='seagreen', markerfacecolor='none')

L1,=ax4.plot(hx_range_exact, sigmaz_exact, label=r'ED', ls='-', lw=5, color='magenta',
             marker='o', alpha=1, markersize=0, markeredgewidth=1.5, markeredgecolor='magenta', markerfacecolor='w')

L2,=ax4.plot(hx_range_trotter[::4], sigmaz_trotter[::4], label=r'Trotter', ls='--', lw=3, color='darkviolet',
             marker='o', alpha=1, markersize=10, markeredgewidth=1.5, markeredgecolor='darkviolet', markerfacecolor='w')

# 画 3 根虚线
L3,=ax4.plot([0,1], [0.5,0.5], label=r'Trotter', ls='--', lw=1, color='grey',
             marker='o', alpha=0.5, markersize=0, markeredgewidth=1.5, markeredgecolor='black', markerfacecolor='w')
L4,=ax4.plot([0,1], [0,0], label=r'Trotter', ls='--', lw=1, color='grey',
             marker='o', alpha=0.5, markersize=0, markeredgewidth=1.5, markeredgecolor='black', markerfacecolor='w')
L5,=ax4.plot([0,1], [-0.5,-0.5], label=r'Trotter', ls='--', lw=1, color='grey',
             marker='o', alpha=0.5, markersize=0, markeredgewidth=1.5, markeredgecolor='black', markerfacecolor='w')
####图例设置
#label = ["Mg", "Mo", "Me","Ms"]
#legfont = {'family' : 'Times New Roman','weight' : 'normal','size': 16, }###图例字体的大小###ncol 设置列的数量，使显示扁平化，当要表示的线段特别多的时候会有用
#legend1=plt.legend(handles=[L1,L2,L3_], loc = 4, bbox_to_anchor=(0.98, 0.58),ncol = 1,prop=legfont,markerscale=1,fancybox=None,shadow=None,frameon=False)
#legend2=plt.legend(handles=[Le, Ls_a, Ls_b], loc = 4, bbox_to_anchor=(0.85, -0.05),ncol = 1,prop=legfont,markerscale=1,fancybox=None,shadow=None,frameon=False)
#plt.gca().add_artist(legend1)#####把图例legend1重新加载回来
## bty 图例框是否画出，o为画出，默认为n不画出
## markerscale 控制图例中maker的大小
## bbox_to_anchor被赋予的二元组中，num1用于控制legend的左右移动，值越大越向右边移动，
# num2用于控制legend的上下移动，值越大，越向上移动。用于微调图例的位置
#=======================================================================================================================
label_x = r'$h_x$'
label_y = r'$\sigma^z(t,h_x)$'
label_x_= r'$\theta$'
ax4.set_xlabel(label_x, size = 14)
ax4.set_ylabel(label_y, size = 14)
ax4_.set_xlabel(label_x_, size=14, rotation = 0)
#ax2.set_title('Distance Matrix', size = 14)
ax4.tick_params(labelsize = 15) # 设置坐标刻度对应数字的大小
ax4_.tick_params(labelsize = 15)
#plt.xlim(0,8)
plt.ylim(-1,1)
ax4.set_xlim([0,1])
ax4.set_xticks([0,0.2,0.4,0.6,0.8,1])
ax4.set_yticks([-1,-0.5,0,0.5,1])

ax4_.set_xlim([0,8])
ax4_.set_xticks([0,1.6,3.2,4.8,6.4,8])
#==============================================================
ax4.text(0.03,-0.87, r'$\mathrm{(d)}$', fontsize=18)
#ax1.text(0.1,0.9, r'$\mathrm{perplexity = 18}$', fontsize=12)
# ax1.text(0.1,0.8, r'$\mathrm{n_{iter} = 5000}$', fontsize=12)
ax4.text(0.26,0.53, r'$t = 8$', fontsize = 16, color='black')
#ax1.text(5.5,0.53, r'Heisenberg', fontsize = 15, color='black')
#ax1.text(5.5,0.5, r'S=1', fontsize = 15, color='black')
#ax1.text(5.5,0.53, r'uniform', fontsize = 15, color='black')
ax4.text(1.03,-0.13, r'$\sigma^z(\theta)$', fontsize = 16, color='black', rotation = 90)
#=============================================================
# 坐标轴设置第一层
labels = ax4.get_xticklabels() + ax4.get_yticklabels()
#[label.set_fontname('Times New Roman') for label in labels]###设置ticket labled的字体格式
ax4.xaxis.set_minor_locator(MultipleLocator(50))###设置次刻度的间隔
ax4.yaxis.set_minor_locator(MultipleLocator(10))###设置次刻度的间隔
ax4.xaxis.set_major_formatter(FormatStrFormatter('%1.1f'))###设置X轴标签文本格式
ax4.yaxis.set_major_formatter(FormatStrFormatter('%1.1f'))###设置Y轴标签文本格式

#=====坐标轴的第二层： 坐标轴的设置
ax4.spines['bottom'].set_linewidth(2) ###设置底部坐标轴的粗细
ax4.spines['left'].set_linewidth(2)   ###设置左边坐标轴的粗细
ax4.spines['right'].set_linewidth(2)  ###设置右边坐标轴的粗细
ax4.spines['top'].set_linewidth(2)    ###设置上部坐标轴的粗细
#ax3.spines['right'].set_color('none')# 将右边上边的两条边颜色设置为空 其实就相当于抹掉这两条边
#ax3.spines['top'].set_color('none')
#====坐标轴的第三层：  刻度线的设置
for line in ax4.xaxis.get_ticklines():
    #line is a Line2D instance
    #line.set_color('green')
    line.set_markersize(2)####设置刻度线的长度
    line.set_markeredgewidth(1.5)####设置刻度线的宽度
for line in ax4.yaxis.get_ticklines():
    # line is a Line2D instance
    #line.set_color('green')
    line.set_markersize(2.5)####设置刻度线的长度
    line.set_markeredgewidth(1.5)####设置刻度线的宽度

#=====坐标轴的第四层： 坐标轴颜色
#ax3.spines['left'].set_color('red')
#ax3.patch.set_facecolor("gray")   #设置ax3区域背景颜色
#ax3.patch.set_alpha(0.5)         #设置ax3区域背景颜色透明度
######################
# 对 ax_ 进行设置
labels_ = ax4_.get_xticklabels() + ax4_.get_yticklabels()
#[label_.set_fontname('Times New Roman') for label_ in labels_]###设置ticket labled的字体格式
ax4_.xaxis.set_minor_locator(MultipleLocator(50))###设置次刻度的间隔
ax4_.yaxis.set_minor_locator(MultipleLocator(10))###设置次刻度的间隔
ax4_.xaxis.set_major_formatter(FormatStrFormatter('%1.1f'))###设置X轴标签文本格式
ax4_.yaxis.set_major_formatter(FormatStrFormatter('%1.1f'))###设置Y轴标签文本格式

for line in ax4_.yaxis.get_ticklines():
    # line is a Line2D instance
    #line.set_color('green')
    line.set_markersize(2.5)####设置刻度线的长度
    line.set_markeredgewidth(1.5)####设置刻度线的宽度

ax4_.spines['left'].set_linewidth(0)
ax4_.spines['right'].set_linewidth(2.5)  ###设置右边坐标轴的粗细。
ax4_.spines['top'].set_linewidth(2.5)
ax4_.spines['bottom'].set_linewidth(0)  ###设置下边坐标轴的粗细。
ax4_.spines['top'].set_color('seagreen') ### 设置右边坐标轴的颜色。
ax4_.spines['right'].set_color('seagreen') ### 设置右边坐标轴的颜色。
#=========================================================================
fig.tight_layout()  #自动调整subplot间的参数 !!! feichangzhongyao
#======================================================================
ISsave = True
if ISsave:
    fig.savefig(r'.\Figs\fig2.eps',dpi=300, format='eps')
#===================================================
plt.show()











