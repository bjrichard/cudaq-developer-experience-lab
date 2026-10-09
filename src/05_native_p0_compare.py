"""Compare imported CUDA-Q and native CUDA-Q Logical P0 workflows."""

import cudaq
import cudaq.logical as cql


@cudaq.kernel
def imported_bell():
    """Prepare and measure a Bell pair with an ordinary CUDA-Q kernel."""
    qubits = cudaq.qvector(2)
    h(qubits[0])
    x.ctrl(qubits[0], qubits[1])
    mz(qubits)


@cql.program
def native_bell() -> tuple[bool, bool]:
    """Prepare and measure a Bell pair as a native Logical P0 program."""
    qubits = cql.allocate(2, state=cql.types.zero)

    qubits[0] = cql.h(qubits[0])
    qubits[0], qubits[1] = cql.cx(qubits[0], qubits[1])

    return (
        cql.measure_z(qubits[0]),
        cql.measure_z(qubits[1]),
    )


def report_imported():
    """Estimate and print resources for the imported CUDA-Q kernel."""
    cudaq.set_target(cql.targets.estimator)

    estimate = cudaq.estimate(imported_bell)
    resources = cql.estimate.LogicalEstimate.from_annotations(
        estimate.annotations
    )

    print("Imported CUDA-Q kernel")
    print(f"  peak logical qubits: {resources.logical_qubits_peak}")
    print(f"  logical action depth: {resources.action_depth_upper_bound}")
    print(f"  logical actions: {dict(resources.actions)}")
    print(f"  logical instruments: {dict(resources.instruments)}")
    print(f"  synthesis demand: {dict(resources.synthesis_demand)}")


def report_native():
    """Compile and estimate resources for the native Logical P0 program."""
    build = cql.compile(native_bell)

    assert build.stage == cql.stages.P0

    resources = cql.estimate(
        build,
        tier=cql.estimate.Tier.LOGICAL,
    )

    print("\nNative CUDA-Q Logical P0 program")
    print("  stage: P0")
    print(f"  peak logical qubits: {resources.logical_qubits_peak}")
    print(f"  logical action depth: {resources.action_depth_upper_bound}")
    print(f"  logical actions: {dict(resources.actions)}")
    print(f"  logical instruments: {dict(resources.instruments)}")
    print(f"  synthesis demand: {dict(resources.synthesis_demand)}")


def main():
    """Compare the imported-kernel and native-P0 resource profiles."""
    report_imported()
    report_native()


if __name__ == "__main__":
    main()
