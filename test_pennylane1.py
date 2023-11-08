# https://pennylane.ai/qml/demos/tutorial_circuit_compilation
import pennylane as qml
import matplotlib.pyplot as plt

dev = qml.device("default.qubit", wires=3)


def circuit(angles):
    qml.Hadamard(wires=1)
    qml.Hadamard(wires=2)
    qml.RX(angles[0], 0)
    qml.CNOT(wires=[1, 0])
    qml.CNOT(wires=[2, 1])
    qml.RX(angles[2], wires=0)
    qml.RZ(angles[1], wires=2)
    qml.CNOT(wires=[2, 1])
    qml.RZ(-angles[1], wires=2)
    qml.CNOT(wires=[1, 0])
    qml.Hadamard(wires=1)
    qml.CY(wires=[1, 2])
    qml.CNOT(wires=[1, 0])
    return qml.expval(qml.PauliZ(wires=0))


angles = [0.1, 0.3, 0.5]
qnode = qml.QNode(circuit, dev)
qml.draw_mpl(qnode, decimals=1, style="sketch")(angles)
plt.show()


commuted_circuit = qml.transforms.commute_controlled(direction="right")(circuit)

qnode = qml.QNode(commuted_circuit, dev)
qml.draw_mpl(qnode, decimals=1, style="sketch")(angles)
plt.show()

cancelled_circuit = qml.transforms.cancel_inverses(commuted_circuit)


qnode = qml.QNode(cancelled_circuit, dev)
qml.draw_mpl(qnode, decimals=1, style="sketch")(angles)
plt.show()

merged_circuit = qml.transforms.merge_rotations(atol=1e-8, include_gates=None)(cancelled_circuit)


qnode = qml.QNode(merged_circuit, dev)
qml.draw_mpl(qnode, decimals=1, style="sketch")(angles)
plt.show()

@qml.qnode(dev)
@qml.transforms.merge_rotations(atol=1e-8, include_gates=None)
@qml.transforms.cancel_inverses
@qml.transforms.commute_controlled(direction="right")
def q_fun(angles):
    qml.Hadamard(wires=1)
    qml.Hadamard(wires=2)
    qml.RX(angles[0], 0)
    qml.CNOT(wires=[1, 0])
    qml.CNOT(wires=[2, 1])
    qml.RX(angles[2], wires=0)
    qml.RZ(angles[1], wires=2)
    qml.CNOT(wires=[2, 1])
    qml.RZ(-angles[1], wires=2)
    qml.CNOT(wires=[1, 0])
    qml.Hadamard(wires=1)
    qml.CY(wires=[1, 2])
    qml.CNOT(wires=[1, 0])
    return qml.expval(qml.PauliZ(wires=0))


qml.draw_mpl(q_fun, decimals=1, style="sketch")(angles)
plt.show()


compiled_circuit = qml.compile()(circuit)

qnode = qml.QNode(compiled_circuit, dev)
qml.draw_mpl(qnode, decimals=1, style="sketch")(angles)
plt.show()

compiled_circuit = qml.compile(num_passes=2)(circuit)

qnode = qml.QNode(compiled_circuit, dev)
qml.draw_mpl(qnode, decimals=1, style="sketch")(angles)
plt.show()

compiled_circuit = qml.compile(
    pipeline=[
        qml.transforms.commute_controlled(direction="left"),  # Opposite direction
        qml.transforms.merge_rotations(include_gates=["RZ"]),  # Different threshold
        qml.transforms.cancel_inverses,  # Cancel inverses after rotations
    ],
    num_passes=3,
)(circuit)

qnode = qml.QNode(compiled_circuit, dev)
qml.draw_mpl(qnode, decimals=1, style="sketch")(angles)
plt.show()

compiled_circuit = qml.compile(basis_set=["CNOT", "RX", "RY", "RZ"], num_passes=2)(circuit)

qnode = qml.QNode(compiled_circuit, dev)
qml.draw_mpl(qnode, decimals=1, style="sketch")(angles)
plt.show()