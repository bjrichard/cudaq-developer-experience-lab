"""Create and sample a two-qubit Bell state with CUDA-Q.

This exercise is based on the GHZ-state validation workflow in NVIDIA’s official
CUDA-Q Quick Start documentation. The structure and API usage are similar, but
the example has been adapted here to prepare and sample a two-qubit Bell state.

References
----------
NVIDIA CUDA-Q Quick Start:
https://nvidia.github.io/cuda-quantum/latest/using/quick_start.html
"""

import cudaq


@cudaq.kernel
def bell_state():
    """Prepare a Bell state and measure both qubits."""
    num_qubits = 2
    qubits = cudaq.qvector(num_qubits)
    h(qubits[0])
    x.ctrl(qubits[0], qubits[1])
    mz(qubits)


def main():
    """Sample the Bell-state kernel and print the circuit and results."""
    print(f"CUDA-Q target: {cudaq.get_target().name}")
    print("\nCircuit:")
    print(cudaq.draw(bell_state))

    result = cudaq.sample(bell_state, shots_count=1000)

    print("\nMeasurement distribution:")
    print(result)


if __name__ == "__main__":
    main()
