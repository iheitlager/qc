import cirq
import qsimcirq

# Pick up to ~25 qubits to simulate (requires ~256MB of RAM)
qubits = [cirq.GridQubit(i,j) for i in range(5) for j in range(5)]

# Define a circuit to run
# (Example is from the 2019 "Quantum Supremacy" experiement)
circuit = (cirq.experiments.
    random_rotations_between_grid_interaction_layers_circuit(
    qubits=qubits, depth=16))

# Measure qubits at the end of the circuit
circuit.append(cirq.measure(*qubits, key='all_qubits'))

# Simulate the circuit with qsim and return just the measurement values
# just like you would with Cirq
qsim_simulator = qsimcirq.QSimSimulator()
qsim_results = qsim_simulator.run(circuit, repetitions=5)
print('qsim results:')
print(qsim_results)