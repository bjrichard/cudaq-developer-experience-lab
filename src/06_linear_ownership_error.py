"""Demonstrate CUDA-Q Logical linear-ownership error handling."""

import cudaq.logical as cql
from cudaq.logical.errors import UseAfterConsume


@cql.program
def stale_owner() -> bool:
    """Intentionally reuse a logical value after it has been consumed."""
    qubits = cql.allocate(1, state=cql.types.zero)

    # This consumes the current owner but does not rebind the successor.
    cql.h(qubits[0])

    # This intentionally tries to reuse the consumed value.
    return cql.measure_z(qubits[0])


@cql.program
def rebound_owner() -> bool:
    """Rebind the successor returned by the logical operation."""
    qubits = cql.allocate(1, state=cql.types.zero)

    qubits[0] = cql.h(qubits[0])

    return cql.measure_z(qubits[0])


def main():
    """Show the ownership failure and then compile the corrected program."""
    try:
        cql.compile(stale_owner)
    except UseAfterConsume as error:
        print("Caught expected UseAfterConsume error:")
        print(error)
    else:
        raise RuntimeError("Expected UseAfterConsume was not raised.")

    corrected = cql.compile(rebound_owner)

    print("\nCorrected program compiled successfully.")
    print(f"Stage: {corrected.stage}")


if __name__ == "__main__":
    main()
