from qiskit import  *

def circ_2q(t,couple):
    '''
    :param t: time for evolution
    :param couple: coupling interaction form: Ising, XXZZ or Heisenberg
    :return:
    '''
    return
#=====================================================================
def circ_initialize(Q,ini_way):
    '''
    :param Q:  线路比特数
    :param ini_way: 线路初始化方式
    '''
    q = QuantumRegister(Q)
    circ = QuantumCircuit(q)
    if ini_way is 'Hadmard':
        for it in range(Q):
            circ.h(q[it])
    return circ
#=====================================================================
def circ_2q_Ising(t, couple):
    '''
    # 用的是pauli 算符
    :param t:  time for evolution
    :param couple: 相互作用耦合强度
    :return: two qubit circuit
    '''
    q = QuantumRegister(2)
    circ = QuantumCircuit(q)
    circ.cx(q[1], q[0])
    circ.rz(2 * t * couple, q[0])
    circ.cx(q[1], q[0])
    circ1 = circ.to_instruction()
    return circ1

def circ_2q_Ising_hx(t, couple):
    '''
    # 用的是自旋算符  而不是 pauli 算符
    :param t:  time for evolution
    :param couple: hx 磁场强度
    :return: two qubit circuit
    '''
    q = QuantumRegister(2)
    circ = QuantumCircuit(q)
    circ.cx(q[1], q[0])
    circ.rz(0.5 * t , q[0])
    circ.cx(q[1], q[0])
    hx = couple
    circ.h(q[0])
    circ.rz(-t * hx, q[0])
    circ.h(q[0])
    circ1 = circ.to_instruction()
    return circ1
#===========================================================
# 线路上写入测量
def circ_add_measure(circuit,Nq,Nmeasure,Nposition):
    '''
    # 注意该函数目前还不能使用  容易出现 bug
    :param circuit: 输入的量子线路
    :param Nq: 量子线路的量子比特数目
    :param Nmeasure: 测量的个数
    :param Nposition: 在哪个线路上进行测量
    '''
    meas = QuantumCircuit(Nq, Nmeasure)
    meas.barrier(range(Nq))
    for it in range(len(Nposition)):
        meas.measure([Nposition[it]], [it])
    qc = circuit + meas
    return qc
#============================================================
# 执行circuit 得到理论上的 simulate 的结果。
def circ_simulate(circuit,backend='statevector_simulator'):
    backend2 = Aer.get_backend(backend)
    job = execute(circuit, backend2)
    return job.result()

# 将circuit 放在 qasm 模拟器上进行模拟, 得到的是统计的 count 数:
def circ_qasm(circuit, shots):
    # 使用 qasm_simulator 时 测量算符必须要加载在线路上。
    backend = BasicAer.get_backend('qasm_simulator')
    job = execute(circuit, backend, shots=shots)
    return job.result()

#=============================================================
# 这几个关于 count 的函数 后面还是需要修改的
def circjob_count_1q(counts):
    count_0 = []
    count_1 = []
    for it in range(len(counts)):
        if '0' in counts[it]:
            count_0.append(counts[it]['0'])
        else:
            count_0.append(0)
        if '1' in counts[it]:
            count_1.append(counts[it]['1'])
        else:
            count_1.append(0)
    return count_0, count_1

def circjob_count_2q(counts):
    count_00 = []
    count_10 = []
    count_01 = []
    count_11 = []
    for it in range(len(counts)):
        if '00' in counts[it]:
            count_00.append(counts[it]['00'])
        else:
            count_00.append(0)
        if '10' in counts[it]:
            count_10.append(counts[it]['10'])
        else:
            count_10.append(0)
        if '01' in counts[it]:
            count_01.append(counts[it]['01'])
        else:
            count_01.append(0)
        if '11' in counts[it]:
            count_11.append(counts[it]['11'])
        else:
            count_11.append(0)

    return count_00, count_10, count_01, count_11

def circjob_count_3q(counts):
    count_000 = []
    count_100 = []
    count_010 = []
    count_110 = []
    count_001 = []
    count_101 = []
    count_011 = []
    count_111 = []
    for it in range(len(counts)):
        if '000' in counts[it]:
            count_000.append(counts[it]['000'])
        else:
            count_000.append(0)
        if '100' in counts[it]:
            count_100.append(counts[it]['100'])
        else:
            count_100.append(0)
        if '010' in counts[it]:
            count_010.append(counts[it]['010'])
        else:
            count_010.append(0)
        if '110' in counts[it]:
            count_110.append(counts[it]['110'])
        else:
            count_110.append(0)
        if '001' in counts[it]:
            count_001.append(counts[it]['001'])
        else:
            count_001.append(0)
        if '101' in counts[it]:
            count_101.append(counts[it]['101'])
        else:
            count_101.append(0)
        if '011' in counts[it]:
            count_011.append(counts[it]['011'])
        else:
            count_011.append(0)
        if '111' in counts[it]:
            count_111.append(counts[it]['111'])
        else:
            count_111.append(0)
    return count_000, count_100, count_010, count_110, count_001,count_101,count_011,count_111
#===============================================================================================
def circjob_count_nq(counts,nbody):
    # nbody 比特数目
    counts_new={} # 相当于要补全所有测量到的比特排列的信息
    for it in range(2**nbody):
        A = format(it, 'b').zfill(nbody)
        if A in counts:
            counts_new[A] = counts[A]
        else:
            counts_new[A] = 0
    return counts_new
def circjob_count_maxtrix(counts_sum):
    count_matrix = []  # M * N 的矩阵， N = 2 ** Nbody, M = len(hx) 即磁场的个数
    for it in range(len(counts_sum)):
        count_matrix.append(list(counts_sum[it].values()))
    return count_matrix
#=============================================================================================
