# CUDA-Q Developer Experience Lab

A hands-on evaluation of NVIDIA CUDA-Q and CUDA-Q Logical, with an emphasis on onboarding, logical resource estimation, compiler boundaries, diagnostics, and the developer experience of moving from ordinary CUDA-Q kernels into fault-tolerant workflows.

This is an independent learning and evaluation project. It is not affiliated with or endorsed by NVIDIA.

## What this repository explores

- CUDA-Q installation and first-program workflows on macOS with Apple silicon
- Bell-state construction, circuit visualization, and sampling
- CUDA-Q Logical resource estimation for Bell and Toffoli kernels
- the relationship between logical actions, instruments, and synthesis demand
- imported CUDA-Q kernels versus programs authored directly in native P0
- multi-controlled-X lowering through an explicit clean-ancilla CCX ladder
- current gate-shape boundaries in the Quake-to-P0 import path
- CUDA-Q Logical's linear-ownership model and `UseAfterConsume` diagnostic
- documentation discoverability, platform transitions, and AI-assisted development

The detailed developer-experience record is maintained in [`notes/documentation_user_experience.md`](notes/documentation_user_experience.md).

## Current findings

The observations below are specific to CUDA-Q 0.16.0 and the tested environments.

- Base CUDA-Q installed and ran successfully on macOS with Apple silicon using CPU simulation.
- `cudaq.logical` was not available in the tested macOS installation, while the same CUDA-Q version exposed it successfully in a Linux GitHub Codespace.
- An imported CUDA-Q Bell kernel and a Bell program authored directly with `@cql.program` produced the same P0 logical resource profile.
- A Toffoli kernel was retained as one logical CCX action and one CCX synthesis demand at P0.
- An explicit four-control-X clean-ancilla ladder produced five CCX actions, five CCX synthesis demands, and seven peak logical qubits, matching the scaling convention in my independent [FTQC Workbench](https://github.com/bjrichard/ftqc-workbench).
- A direct four-control X was accepted by base CUDA-Q but rejected by the current CUDA-Q Logical Quake-to-P0 import path, which supports up to two controls for X/Z in this workflow.
- CUDA-Q Logical's typed `UseAfterConsume` error clearly identified reuse of a consumed logical value, although the printed diagnostic did not include the originating Python source line.

These are focused observations from small examples, not a comprehensive evaluation of CUDA-Q or CUDA-Q Logical.

## Exercises

| File | Purpose |
|---|---|
| [`src/01_bell_state.py`](src/01_bell_state.py) | Build, draw, and sample a two-qubit Bell state with base CUDA-Q. |
| [`src/02_logical_resource_estimate.py`](src/02_logical_resource_estimate.py) | Import a Bell kernel into CUDA-Q Logical and inspect its P0 resource profile. |
| [`src/03_toffoli_resource_estimate.py`](src/03_toffoli_resource_estimate.py) | Inspect logical actions and synthesis demand for a Toffoli/CCX kernel. |
| [`src/04_multicontrol_resource_compare.py`](src/04_multicontrol_resource_compare.py) | Compare an explicit clean-ancilla CCX ladder with a direct four-control X. |
| [`src/05_native_p0_compare.py`](src/05_native_p0_compare.py) | Compare an imported Bell kernel with a Bell program authored directly in native P0. |
| [`src/06_linear_ownership_error.py`](src/06_linear_ownership_error.py) | Demonstrate CUDA-Q Logical's linear-ownership error and the corrected rebinding pattern. |

## Environment and setup

### Base CUDA-Q on macOS

The repository includes a Conda environment pinned to CUDA-Q 0.16.0:

```bash
conda env create -f environment.yml
conda activate cudaq-lab
python src/01_bell_state.py
```

The tested macOS setup uses Apple silicon and CPU simulation. NVIDIA GPU acceleration is not available on macOS.

### CUDA-Q Logical on Linux

The Logical exercises were run in a Linux GitHub Codespace because `cudaq.logical` was unavailable in the tested macOS installation.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install "cudaq==0.16.0"
```

Verify the installation:

```bash
python -c "import cudaq; print(cudaq.__version__)"
python -c "import cudaq.logical as cql; print('CUDA-Q Logical import successful')"
```

Run the Logical exercises:

```bash
python src/02_logical_resource_estimate.py
python src/03_toffoli_resource_estimate.py
python src/04_multicontrol_resource_compare.py
python src/05_native_p0_compare.py
python src/06_linear_ownership_error.py
```

CUDA-Q Logical is a preview feature, so APIs and behavior may change.

## Developer-experience method

For each step, the project records:

1. the environment and CUDA-Q version;
2. the exact command or program used;
3. the observed output or failure mode;
4. the distinction between verified behavior and interpretation;
5. the developer-experience implication; and
6. the next question to investigate.

The notes cover installation, documentation discovery, platform support, warnings, compiler diagnostics, logical resource profiles, and the use of AI assistance for command lookup and note organization.

## Repository structure

```text
cudaq-developer-experience-lab/
├── README.md
├── environment.yml
├── notes/
│   └── documentation_user_experience.md
└── src/
    ├── 01_bell_state.py
    ├── 02_logical_resource_estimate.py
    ├── 03_toffoli_resource_estimate.py
    ├── 04_multicontrol_resource_compare.py
    ├── 05_native_p0_compare.py
    └── 06_linear_ownership_error.py
```

## Scope and limitations

This repository is intentionally small and inspectable. It does not attempt to:

- benchmark CUDA-Q performance;
- model a complete fault-tolerant architecture;
- estimate physical qubits, code distance, magic-state factories, or runtime;
- evaluate GPU or QPU execution targets;
- provide a production compiler or reusable SDK; or
- comprehensively review the CUDA-Q documentation ecosystem.

The examples are designed to expose specific programming and resource-modeling concepts while preserving the current preview limitations and error behavior.

## Primary references

- [NVIDIA CUDA-Q Quick Start](https://nvidia.github.io/cuda-quantum/latest/using/quick_start.html)
- [CUDA-Q Logical documentation](https://nvidia.github.io/cuda-quantum/latest/preview/logical/)
- [CUDA-Q Logical core concepts](https://nvidia.github.io/cuda-quantum/latest/preview/logical/getting-started/concepts.html)
- [CUDA-Q Logical resource estimation](https://nvidia.github.io/cuda-quantum/latest/preview/logical/use-cases/estimation.html)
