"""Estimate logical resources for a Toffoli CUDA-Q kernel."""

import cudaq
import cudaq.logical as cql


@cudaq.kernel
def toffoli_kernel():
    """Apply a doubly controlled X and measure all three qubits."""
    qubits = cudaq.qvector(3)
    x.ctrl([qubits[0], qubits[1]], qubits[2])
    mz(qubits)


def main():
    """Run the CUDA-Q Logical estimator for the Toffoli kernel."""
    cudaq.set_target(cql.targets.estimator)

    estimate = cudaq.estimate(toffoli_kernel)
    resources = cql.estimate.LogicalEstimate.from_annotations(
        estimate.annotations
    )

    print("Logical Toffoli resources:")
    print(f"  peak logical qubits: {resources.logical_qubits_peak}")
    print(f"  logical action depth: {resources.action_depth_upper_bound}")
    print(f"  logical actions: {dict(resources.actions)}")
    print(f"  logical instruments: {dict(resources.instruments)}")
    print(f"  synthesis demand: {dict(resources.synthesis_demand)}")


if __name__ == "__main__":
    main()
