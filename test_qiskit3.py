# Taken from https://towardsdatascience.com/what-is-quantum-entanglement-anyway-4ea97df4bb0e
# https://qiskit.org/documentation/intro_tutorial1.html

from qiskit import __version__
import sys

print("Qiskit Version: ", __version__)
print("Python Version: ", sys.version)

# The tools we will need
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, execute, transpile
from qiskit_aer import AerSimulator
 # Qiskit allows us to make beautiful plots 
from qiskit.visualization import plot_histogram                                     
import matplotlib.pyplot as plt

# allows us to do quantum simulation of measurements 
#M_simulator=Aer.backends(name='qasm_simulator')[0] 
M_simulator=AerSimulator()

qr=QuantumRegister(3) # qreg is filled with two qubits 
creg=ClassicalRegister(3) # creg is filled with two classical bits 

circuit=QuantumCircuit(qr,creg) # we put our qreg and creg together to make our Quantum Circuit, called entangler here. 

circuit.h(qr)
circuit.cx(qr[0], qr[1]) 
circuit.cx(qr[0], qr[2])
circuit.barrier()
circuit.x(qr[1]) # Action Oracle
circuit.h(qr[0])

circuit.measure([0,1,0],[1,0,0]) # measure the first qubit and record it in the first classical bit

circuit.draw(output='mpl') 

# Compile the circuit for the support instruction set (basis_gates)
# and topology (coupling_map) of the backend
compiled_circuit = transpile(circuit, M_simulator)

# Execute the circuit on the aer simulator
job = M_simulator.run(compiled_circuit, shots=1000)

# Grab results from the job
result = job.result()

# Returns counts
counts = result.get_counts(compiled_circuit)
print("\nTotal count for 00 and 11 are:", counts)

plot_histogram(counts)
plt.show()

input('Press any key to finish')