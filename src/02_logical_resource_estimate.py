import cudaq
import cudaq.logical as cql


@cudaq.kernel
def bell_pair():
    qubits = cudaq.qvector(2)
    h(qubits[0])
    x.ctrl(qubits[0], qubits[1])
    mz(qubits)


cudaq.set_target(cql.targets.estimator)
cql.targets.estimator.print_stack()

estimate = cudaq.estimate(bell_pair)
resources = cql.estimate.LogicalEstimate.from_annotations(estimate.annotations)

print("Logical Bell-pair resources:")
print(f"  peak logical qubits: {resources.logical_qubits_peak}")
print(f"  logical action depth: {resources.action_depth_upper_bound}")
print(f"  logical actions: {dict(resources.actions)}")
print(f"  logical instruments: {dict(resources.instruments)}")
