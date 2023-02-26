#### QC-alpha-circuit

##### Introduction
> * The real time evolution of Heisenberg model with transverse magnetic filed.
> * Three schemes: classical exact evolution, trotter circuits, quantum circuits. 

##### Key Words
> * Time evolution
> * parameterized Quantum Circuits, fast-forward,   
> * Trotter evolution, Quantum many-body system 

##### Usage

> Runing the whole project should follow the running order:

> * $ python exact_evolution.py 
>> * show the results of measuring 1 qubits and 2 qubits by exact evolution. 

> * $ python exact_evolution_m3.py
>> * 1) show the results of measuring 3 qubits by exact evolution.
>> * 2) write the data to files in '.pr' format, which is useful for further analysis
>> * 3) data output along folder: './data/H_heisenberg_hx/exact_evolution/'

> * $ python exact_evolution_mn.py
>> * 1) show the results of measuring n qubits by exact evolution, where n > 3 .
>> * 2) write the data to files in '.pr' format, which is useful for further analysis
>> * 3) data output along folder: './data/H_heisenberg_hx/exact_evolution/'

> * $ python trotter_circuit.py
>> * 1) The evolution operator is decomposed into trotter slices, 
and then the circuit is evolved by trotter decomposition evolution.
>> * 2) Note: trotter slice is also decomposed as a series of Quantum Gates!
>> * 3) Obtain the the quantum gate decomposition form of  trotter 
evolution operator slice corresponding to different magnetic fields is obtained
>> * 4) show the results of measuring 1 qubits and 2 qubits by trotter_circuit.

> * $ python trotter_circuit_m3.py
>> * 1) realize the trotter scheme by quantum gates
>> * 2) results of measuring 3 qubits based on trotter scheme
>> * 3) write the data to files in '.pr' format, which is useful for further analysis
>> * 4) data output along folder: './data/H_heisenberg_hx/trotter_qasm_simulator/'

> * $ python trotter_circuit_mn.py
>> * 1) realize the trotter scheme by quantum gates
>> * 2) results of measuring n qubits (n > 3) based on trotter scheme
>> * 3) write the data to files in '.pr' format, which is useful for further analysis
>> * 4) data output along folder: './data/H_heisenberg_hx/trotter_qasm_simulator/'

> * $ python alpha_circuit_5qubits.py
>> * 1) show how to construct 5 qubits alpha circuit
>> * 2) show the result of measuring 1 qubit on 5-qubits alpha circuit
>> * 3) show the result of measuring 2 qubits on 5-qubits alpha circuit

> * $ python alpha_circuit_5qubits_m3.py
>> * 1) show the result of measuring 3 qubits on 5-qubits alpha circuit
>> * 2) write the data to files in '.pr' format, which is useful for further analysis
>> * 3) data output along folder: './data/H_heisenberg_hx/advance_qasm_simulator/'

> * $ python alpha_circuit_5qubits_mn.py
>> * 1) show the result of measuring n qubits (n = 4, 5,) on 5-qubits alpha circuit
>> * 2) write the data to files in '.pr' format, which is useful for further analysis
>> * 3) data output along folder: './data/H_heisenberg_hx/advance_qasm_simulator/'

> * $ python sigma_z_zz_zzz.py
>> * Obtain the evolution results of sigma_z, sigma_zz, and sigma_zzz
>> * 1) sigma_z by exact_evolution with fixed hx
>> * 2) sigma_z by alpha_circuit with fixed hx
>> * 3) sigma_z by trotter_circuit with fixed hx
>> * 4) sigma_zz by exact_evolution with fixed hx
>> * 5) sigma_zz by alpha_circuit with fixed hx
>> * 6) sigma_zz by trotter_circuit with fixed hx
>> * 7) sigma_zzz by exact_evolution with fixed hx,
>> * 8) sigma_zzz by alpha_circuit with fixed hx
>> * 9) sigma_zzz by trotter_circuit with fixed hx
>> * data output along folders: './data/H_heisenberg_hx/exact_evolution_fix_hx/', 
'./data/H_heisenberg_hx/advance_qasm_simulator_fix_hx/', and 
'./data/H_heisenberg_hx/trotter_qasm_simulator_fix_hx/' .

> * $ python sigma_z_string.py
>> *  Obtain the evolution results of sigma_z_string i.e. sigma_z^n with n > 3
>> * 1) sigma_z_string by exact_evolution with fixed hx
>> * 2) sigma_z_string by alpha_circuit with fixed hx
>> * 3) sigma_z_string by trotter_circuit with fixed hx 
>> * data output along folders: './data/H_heisenberg_hx/exact_evolution_fix_hx/', 
'./data/H_heisenberg_hx/advance_qasm_simulator_fix_hx/', and 
'./data/H_heisenberg_hx/trotter_qasm_simulator_fix_hx/' .

> * $ python dataplot_sigmaz.py
>> * plot fig.2 in the article
>> * figures output along folder: './Figs/'

> * $ python dataplot_sigmazz.py
>> * plot fig.3 in the article
>> * figures output along folder: './Figs/'

> * $ python dataplot_sigmaz_string.py
>> * plot fig.4 in the article
>> * figures output along folder: './Figs/'

##### Contact:
> * messiyuan16@gmail.com

##### Tips: 
> * If you use this codes, plese cite our paper [Towards simulating time evolution of specific quantum many-body system by lower counts of quantum gates](https://iopscience.iop.org/article/10.1209/0295-5075/acad25/meta) .


