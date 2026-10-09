"""Compare two representations of a four-control X operation.

The explicit construction uses a clean-ancilla ladder of supported CCX
operations. The direct construction tests whether the current CUDA-Q Logical
import path accepts a higher-order controlled-X operation.
"""

import cudaq
import cudaq.logical as cql


@cudaq.kernel
def explicit_ladder():
    """Implement a four-control X using five CCX gates and two clean ancillas."""
    qubits = cudaq.qvector(7)

    # Controls: 0, 1, 2, 3
    # Target: 4
    # Clean ancillas: 5, 6
    x.ctrl([qubits[0], qubits[1]], qubits[5])
    x.ctrl([qubits[2], qubits[5]], qubits[6])
    x.ctrl([qubits[3], qubits[6]], qubits[4])
    x.ctrl([qubits[2], qubits[5]], qubits[6])
    x.ctrl([qubits[0], qubits[1]], qubits[5])

    mz(qubits)


@cudaq.kernel
def direct_multicontrol():
    """Express the same operation directly as a four-control X."""
    qubits = cudaq.qvector(5)

    x.ctrl(
        [qubits[0], qubits[1], qubits[2], qubits[3]],
        qubits[4],
    )

    mz(qubits)


def unsupported_gate_detail(message: str) -> str:
    """Extract the most useful unsupported-gate diagnostic."""
    return next(
        (
            line.strip()
            for line in message.splitlines()
            if "unsupported gate shape" in line
        ),
        message.splitlines()[0] if message else "Unknown compiler error",
    )


def report(name, kernel):
    """Estimate and print the logical resources for one kernel."""
    print(f"\n{name}")

    try:
        estimate = cudaq.estimate(kernel)
    except RuntimeError as error:
        message = str(error)

        # Only convert the known preview limitation into a concise report.
        # Unexpected runtime/compiler failures should remain visible.
        if "unsupported gate shape" not in message:
            raise

        print("  status: unsupported by current CUDA-Q Logical import path")
        print(f"  compiler message: {unsupported_gate_detail(message)}")
        return

    resources = cql.estimate.LogicalEstimate.from_annotations(
        estimate.annotations
    )

    print(f"  peak logical qubits: {resources.logical_qubits_peak}")
    print(f"  logical action depth: {resources.action_depth_upper_bound}")
    print(f"  logical actions: {dict(resources.actions)}")
    print(f"  logical instruments: {dict(resources.instruments)}")
    print(f"  synthesis demand: {dict(resources.synthesis_demand)}")


def main():
    """Run both multi-control resource-estimation paths."""
    cudaq.set_target(cql.targets.estimator)

    report("Explicit clean-ancilla ladder", explicit_ladder)
    report("Direct four-control X", direct_multicontrol)


if __name__ == "__main__":
    main()