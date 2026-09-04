# CUDA-Q Developer Experience Lab

A small hands-on learning repository for exploring NVIDIA CUDA-Q from the perspective of both a quantum-computing user and a developer evaluating the onboarding experience.

## Goals

This repository has two goals:

1. Build practical familiarity with CUDA-Q by writing and running small quantum programs.
2. Record observations about the developer experience: what is intuitive, what requires documentation, where friction appears, and how AI-assisted development changes the workflow.

This is an independent learning project. It is not affiliated with or endorsed by NVIDIA.

## Primary learning resources and attribution

The initial exercises in this repository are based on NVIDIA's official CUDA-Q documentation, especially:

- **NVIDIA CUDA-Q Quick Start**  
  https://nvidia.github.io/cuda-quantum/latest/using/quick_start.html

- **Building your first CUDA-Q Program**  
  https://nvidia.github.io/cuda-quantum/latest/using/basics/build_kernel.html

- **Running your first CUDA-Q Program**  
  https://nvidia.github.io/cuda-quantum/latest/using/basics/run_kernel.html

The repository follows the concepts and workflow introduced in those resources, but the code and notes here are written independently for learning and experimentation.

## Environment setup

These exercises are currently being developed on macOS using Apple silicon.

CUDA-Q supports macOS on ARM64, but NVIDIA GPU acceleration is not available on this platform. As a result, the initial exercises focus on the CUDA-Q programming model, CPU-based simulation, API usage, and developer experience rather than GPU-accelerated simulation or performance benchmarking.

The first exercises use the Python interface to CUDA-Q. You can use either a standard Python virtual environment or the included Conda environment definition.

### Option 1: Python virtual environment

Create and activate a local virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Upgrade `pip` and install CUDA-Q:

```bash
python -m pip install --upgrade pip
pip install cudaq
```

### Option 2: Conda environment

Create the environment from `environment.yml`:

```bash
conda env create -f environment.yml
```

Activate it:

```bash
conda activate cudaq-lab
```

The `environment.yml` file contains:

```yaml
name: cudaq-lab

channels:
  - conda-forge

dependencies:
  - python=3.12
  - pip
  - pip:
      - cudaq
```

If the environment definition changes later, update it with:

```bash
conda env update -f environment.yml --prune
```

## First exercise

The first program creates a two-qubit Bell state and samples the measurement distribution.

Run:

```bash
python src/01_bell_state.py
```

Expected behavior: the results should be concentrated on `00` and `11`, with approximately equal frequencies over many shots.

This is intentionally close in spirit to the GHZ-state validation example in NVIDIA's CUDA-Q Quick Start, while being implemented here as a minimal two-qubit learning exercise.

## What I am paying attention to

While working through CUDA-Q, I am recording observations in [`notes/developer_journey.md`](notes/developer_journey.md), including:

- installation and environment setup
- API discoverability
- terminology and conceptual mapping from Qiskit
- quality and usefulness of examples
- error messages and debugging experience
- how easily AI tools can find and correctly use CUDA-Q documentation
- time to first successful program
- differences between what is easy for a human developer and what is easy for an AI coding assistant

## Planned exercises

- [x] Install CUDA-Q and validate the environment.
- [x] Run the Bell-state sampling example.
- [ ] Use `cudaq.draw()` to inspect the circuit.
- [ ] Write a small parameterized kernel.
- [ ] Use `cudaq.sample()`.
- [ ] Use `cudaq.observe()`.
- [ ] Reproduce a small algorithm already familiar from Qiskit.
- [ ] Compare the CUDA-Q and Qiskit developer experiences.
- [ ] Explore CUDA-Q execution targets available on the local machine.
- [ ] Record developer-experience observations after each exercise.

## Repository structure

```text
cudaq-developer-experience-lab/
├── README.md
├── requirements.txt
├── src/
│   └── 01_bell_state.py
└── notes/
    └── developer_journey.md
```

## Scope

This repository is intentionally small. The goal is not to build a production quantum application or benchmark CUDA-Q comprehensively. It is to gain hands-on familiarity with the platform while documenting the onboarding and developer experience carefully.
