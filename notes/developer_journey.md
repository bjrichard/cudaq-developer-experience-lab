# Developer Journey Notes

This file is used as a running log while learning CUDA-Q. The goal is to notice what the experience is like for a new developer and what could make that experience better.

## Exercise 0 — Installation

**Date:** 09/03/2026  
**Platform:** macOS 26.6.2, Apple Silicon (M3 Pro)
**Python version:** 3.12.14 [from python --version in the dedicated Conda environment]
**CUDA-Q version:** 0.15.1 [from python -c "import cudaq; print(cudaq.__version__)" in the dedicated Conda environment]

### What I tried

I set up a dedicated Conda environment for the project using the repository's `environment.yml` file:

```bash
conda env create -f environment.yml
conda activate cudaq-lab
```

The environment installs Python, pip, and CUDA-Q.

### What was intuitive?

The basic environment setup was straightforward. Creating and activating the Conda environment followed a familiar workflow, and CUDA-Q installed without requiring additional configuration.

### Where did I need documentation?

I needed to confirm:

* CUDA-Q support for macOS on Apple silicon.
* The limitations of running CUDA-Q on macOS, particularly the lack of NVIDIA GPU acceleration.
* The recommended installation method for the Python package.

### Where did I get stuck?

There were no technical problems during installation.

### How useful were the error messages?

No CUDA-Q errors occurred during the installation. As a result, I have not yet had enough experience to evaluate CUDA-Q error messages.

### Did I use AI assistance?

Yes, selectively.

I used ChatGPT mainly to accelerate setup and documentation tasks, including:

- Refining the structure of the developer-journey notes
- Clarifying a few Python and Conda commands
- Helping compare setup options

The technical work itself remained straightforward to understand and validate independently. AI mainly reduced the time required to look up commands, organize notes, and resolve minor questions.

### Did the AI have the right information?

So far, yes. The guidance was consistent with the CUDA-Q documentation and the environment worked successfully. I still treated the official documentation as the primary reference.

### AI-assisted developer experience

AI was useful as a productivity aid rather than a dependency. Its main value was reducing the time spent on small setup questions, command lookup, and organizing the notes. The CUDA-Q documentation was clear, and the underlying technical work was straightforward to follow and validate independently.

### Time to first success

About 15 minutes, including the creation of the repository and the Conda environment.

### What would I improve for another developer?

For a developer running macOS without GPU access, the [NVIDIA CUDA-Q Quick Start](https://nvidia.github.io/cuda-quantum/latest/using/quick_start.html) instructions were clear, direct, and sufficient. I did not encounter any roadblock during the initial exercises. I cannot yet comment on the onboarding experience for GPU-enabled systems or more complex heterogeneous configurations, which may introduce additional setup and configuration requirements.

---

## Exercise 1 — Bell-state sampling

### Goal

Create a two-qubit Bell state and sample its measurement distribution.

### Expected result

Measurements should be concentrated on `00` and `11`, with approximately equal frequencies over sufficiently many shots.

### What I tried

I created a two-qubit CUDA-Q kernel that applies a Hadamard gate to the first qubit, a controlled-X gate to the second, measures both qubits in the Z basis, and samples the circuit over repeated shots.

The program ran successfully and produced the expected Bell-state measurement distribution.

### What felt familiar from previous quantum software experience?

The overall workflow was familiar: allocate qubits, apply gates, create entanglement, measure, and inspect the resulting shot distribution.

The underlying quantum logic was therefore immediately recognizable, so the main task was learning how CUDA-Q expresses the same ideas.

### What felt new or different?

The main difference was the programming model.

CUDA-Q expresses the quantum program as a kernel decorated with `@cudaq.kernel`, with quantum operations written directly inside the function. Execution is then handled separately with functions such as `cudaq.sample()`.

That felt different from workflows where the circuit itself is primarily constructed as an object step by step.

### What CUDA-Q terminology or syntax did I have to look up?

- `@cudaq.kernel`
- `cudaq.qvector`
- controlled-gate syntax
- `cudaq.sample()`

### Was `cudaq.sample()` intuitive?

Yes.

Once the kernel was defined, using `cudaq.sample()` to execute repeated shots and inspect the measurement distribution was straightforward.

### Did I use AI assistance?

The [NVIDIA CUDA-Q Quick Start](https://nvidia.github.io/cuda-quantum/latest/using/quick_start.html) was sufficient for understanding and running the exercise. AI was mainly useful for workflow questions, syntax lookups as a complement to the [NVIDIA CUDA-Q API Reference](https://nvidia.github.io/cuda-quantum/latest/api/api.html), and organizing the notes.

### What would have made this easier?

Nothing significant. The exercise was straightforward, and the [Quick Start](https://nvidia.github.io/cuda-quantum/latest/using/quick_start.html) and [API Reference](https://nvidia.github.io/cuda-quantum/latest/api/api.html) were sufficient for completing it.

---

## General observations
