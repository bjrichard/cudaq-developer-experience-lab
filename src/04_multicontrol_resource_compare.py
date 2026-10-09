import cudaq
import cudaq.logical as cql


@cudaq.kernel
def explicit_ladder():
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
    qubits = cudaq.qvector(5)

    x.ctrl(
        [qubits[0], qubits[1], qubits[2], qubits[3]],
        qubits[4],
    )

    mz(qubits)


def report(name, kernel):
    print(f"\n{name}")

    try:
        estimate = cudaq.estimate(kernel)
    except RuntimeError as error:
        message = str(error)

        detail = next(
            (
                line.strip()
                for line in message.splitlines()
                if "unsupported gate shape" in line
            ),
            message.splitlines()[0] if message else "Unknown compiler error",
        )

        print("  status: unsupported by current CUDA-Q Logical import path")
        print(f"  compiler message: {detail}")
        return

    resources = cql.estimate.LogicalEstimate.from_annotations(
        estimate.annotations
    )

    print(f"  peak logical qubits: {resources.logical_qubits_peak}")
    print(f"  logical action depth: {resources.action_depth_upper_bound}")
    print(f"  logical actions: {dict(resources.actions)}")
    print(f"  logical instruments: {dict(resources.instruments)}")
    print(f"  synthesis demand: {dict(resources.synthesis_demand)}")


cudaq.set_target(cql.targets.estimator)

report("Explicit clean-ancilla ladder", explicit_ladder)
report("Direct four-control X", direct_multicontrol)
