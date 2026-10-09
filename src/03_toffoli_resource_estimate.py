import cudaq
import cudaq.logical as cql


@cudaq.kernel
def toffoli_kernel():
    qubits = cudaq.qvector(3)
    x.ctrl([qubits[0], qubits[1]], qubits[2])
    mz(qubits)


cudaq.set_target(cql.targets.estimator)

estimate = cudaq.estimate(toffoli_kernel)
resources = cql.estimate.LogicalEstimate.from_annotations(estimate.annotations)

print("Logical Toffoli resources:")
print(f"  peak logical qubits: {resources.logical_qubits_peak}")
print(f"  logical action depth: {resources.action_depth_upper_bound}")
print(f"  logical actions: {dict(resources.actions)}")
print(f"  logical instruments: {dict(resources.instruments)}")
print(f"  synthesis demand: {resources.synthesis_demand}")
