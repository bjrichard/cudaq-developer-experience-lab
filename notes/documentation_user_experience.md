# CUDA-Q Developer Experience and Documentation Notes

This document is a running record of my experience learning and using CUDA-Q. The goal is to capture not only whether individual exercises work, but also how the developer journey feels: installation, documentation discovery, terminology, environment setup, error messages, AI-assisted development, and the transition from basic CUDA-Q workflows into newer functionality such as CUDA-Q Logical.

## Exercise 0 — Installation

**Date:** 09/03/2026  
**Platform:** macOS 26.6.2, Apple Silicon (M3 Pro)  
**Python version:** 3.12.14  
**Initial CUDA-Q version:** 0.15.1

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

- CUDA-Q support for macOS on Apple silicon.
- The limitations of running CUDA-Q on macOS, particularly the lack of NVIDIA GPU acceleration.
- The recommended installation method for the Python package.

### Where did I get stuck?

There were no technical problems during installation.

### How useful were the error messages?

No CUDA-Q errors occurred during the installation, so there was not yet enough experience to evaluate CUDA-Q error messages.

### AI-assisted developer experience

I used ChatGPT selectively to accelerate setup and documentation tasks, including:

- refining the structure of the developer-journey notes;
- clarifying Python and Conda commands;
- helping compare setup options.

The technical work remained straightforward to understand and validate independently. AI mainly reduced the time required to look up commands, organize notes, and resolve minor questions. I treated the official CUDA-Q documentation as the primary technical reference.

### Time to first success

About 15 minutes, including creation of the repository and Conda environment.

### What would I improve for another developer?

For a developer running macOS without GPU access, the [NVIDIA CUDA-Q Quick Start](https://nvidia.github.io/cuda-quantum/latest/using/quick_start.html) instructions were clear, direct, and sufficient. I did not encounter a roadblock during the initial setup. I cannot yet comment on onboarding for GPU-enabled systems or more complex heterogeneous configurations, which may introduce additional setup requirements.

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

The underlying quantum logic was immediately recognizable, so the main task was learning how CUDA-Q expresses the same ideas.

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

Yes. Once the kernel was defined, using `cudaq.sample()` to execute repeated shots and inspect the measurement distribution was straightforward.

### Did I use AI assistance?

The [NVIDIA CUDA-Q Quick Start](https://nvidia.github.io/cuda-quantum/latest/using/quick_start.html) was sufficient for understanding and running the exercise. AI was mainly useful for workflow questions, syntax lookups as a complement to the [NVIDIA CUDA-Q API Reference](https://nvidia.github.io/cuda-quantum/latest/api/api.html), and organizing the notes.

### What would have made this easier?

Nothing significant. The exercise was straightforward, and the Quick Start and API Reference were sufficient for completing it.

---

## Documentation and learning-path review

I started with the [CUDA-Q Quick Start](https://nvidia.github.io/cuda-quantum/latest/using/quick_start.html), which worked well as an entry point. The page quickly directs users toward the broader [CUDA-Q developer page](https://developer.nvidia.com/cuda-q) to explore the key benefits of CUDA-Q and additional learning resources.

The developer page contains a substantial amount of material, including starter kits, videos, examples, and an interactive circuit-building widget. The widget was particularly useful: it allows users to construct circuits by dragging gates, displays the corresponding CUDA-Q kernel, and can execute the generated code. It also includes example circuits that can be run directly. This provides a low-friction way to connect the visual structure of a quantum circuit with CUDA-Q syntax.

The starter-kit links initially looked as though they might introduce another layer of navigation, but in practice they mostly point to more specialized material. The first resource, focused on getting started with quantum-GPU supercomputing, is broadly relevant, while the others are more topic-specific. As a result, the additional material did not make the initial learning path significantly more confusing.

I also explored the [CUDA-Q Academic learning path](https://nvidia.github.io/cuda-q-academic/learningpath.html). This was particularly interesting from an instructional perspective. The instructor guide provides a collection of modules and several suggested learning pathways. These pathways are useful starting points, but they do not appear to constitute a complete course on their own. Additional explanation, exercises, assessment material, and connective content would likely be needed to turn them into a self-contained undergraduate or graduate curriculum.

Overall, there is a large amount of useful material linked from the CUDA-Q developer page. My impression is that much of it is best treated as a next step after completing the Quick Start rather than as part of the initial onboarding flow.

As I moved between the different pages, I noticed some redundancy in the material. This did not feel excessive or problematic. In most cases, the repetition seemed intended to make individual pages more self-contained, so that users could arrive at a page independently without needing to follow a single linear path through the documentation.

One small gap I noticed concerns environment setup on macOS. The Quick Start recommends using:

```bash
python3 -m venv .venv
```

for macOS, while Conda appears more prominently in the Linux setup guidance. Conda works naturally for macOS users as well, so explicitly documenting it as an alternative would make the setup options feel more complete.

Overall, the Quick Start is doing what I would expect it to do: it gets a new user to a working CUDA-Q example quickly, while providing links to deeper installation guidance and more advanced material if the basic instructions are not sufficient. The broader documentation ecosystem is extensive and useful, though the amount of material becomes much larger once the user moves beyond the Quick Start.

---

## 2026-10-07 — CUDA-Q 0.16.0 upgrade and CUDA-Q Logical discovery

### Environment

- macOS on Apple silicon
- Conda environment: `cudaq-lab`
- CUDA-Q upgraded from 0.15.1 to 0.16.0

### Upgrade result

I verified the installed CUDA-Q version with:

```bash
python -c "import cudaq; print(cudaq.__version__)"
```

The command confirmed CUDA-Q 0.16.0:

```text
CUDA-Q Version 0.16.0 (https://github.com/NVIDIA/cuda-quantum 9ceceba030d737655f8a4fb15fadbc3bdee6f30d)
```

Importing CUDA-Q also produced a `FutureWarning` indicating that the `sample` and `observe` algorithmic primitives will change in a future release and linking to the migration documentation. This is useful migration guidance, although it appears on import even before those primitives are called.

### Attempt to use CUDA-Q Logical

I then tried to import the Logical API:

```bash
python -c "import cudaq.logical as cql; print('CUDA-Q Logical import successful')"
```

The result was:

```text
ModuleNotFoundError: No module named 'cudaq.logical'
```

### Developer-experience observation

The base CUDA-Q 0.16.0 installation succeeds in this macOS environment, but `cudaq.logical` is not available from that installation. From a developer-onboarding perspective, this is a meaningful discovery point: a user can successfully upgrade CUDA-Q, see current CUDA-Q documentation describing Logical functionality, and then encounter an import failure when attempting to use it.

The initial error itself does not explain whether the problem is package installation, platform support, version mismatch, or an incorrect import path. Resolving that ambiguity requires additional investigation outside the failed command.

### Questions raised

- Where in the CUDA-Q Logical learning path is platform support first stated?
- Is the platform requirement obvious before a developer attempts to import or install the Logical functionality?
- Could the quick-start path surface supported platforms earlier?
- Could an installation or import failure provide a more actionable explanation?
- What is the recommended workflow for a macOS developer who wants to experiment with CUDA-Q Logical?
- How should the migration warning for `sample` and `observe` be presented so that it is informative without distracting from unrelated import or setup work?

### Compatibility check after the 0.16.0 upgrade

I reran the existing Bell-state exercise under CUDA-Q 0.16.0:

```bash
python src/01_bell_state.py
```

The program still completed successfully, `cudaq.draw()` rendered the expected circuit, and the sampled measurement distribution remained concentrated on `00` and `11` as expected for the Bell-state preparation.

The same `FutureWarning` about upcoming changes to the `sample` and `observe` primitives appeared during normal execution. In other words, the upgrade did not break the existing exercise, but the migration warning is now part of the normal developer experience even for code that still executes correctly.

This separates two issues that initially appeared together:

- existing CUDA-Q code remains functional under 0.16.0, subject to a forward-looking API migration warning;
- CUDA-Q Logical is a separate availability/platform issue in the current macOS environment.

### Reproducibility update

The project environment was pinned to CUDA-Q 0.16.0 so the local project state matches the version used for subsequent experiments.

---

## 2026-10-07 — Linux Codespace setup for CUDA-Q Logical

### Environment inspection

Before installing anything in the GitHub Codespace, I inspected the environment with:

```bash
uname -a
uname -m
python3 --version
cat /etc/os-release | head
```

This established the Linux environment and architecture before adding project dependencies.

### Setup

Inside the Codespace, I created a clean Python virtual environment and installed the same CUDA-Q version used by the local macOS project:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install "cudaq==0.16.0"
```

I then verified both the base CUDA-Q package and the Logical API:

```bash
python -c "import cudaq; print(cudaq.__version__)"
python -c "import cudaq.logical as cql; print('CUDA-Q Logical import successful')"
```

Both checks succeeded. In contrast with the local macOS environment, `cudaq.logical` was available immediately after installing CUDA-Q 0.16.0 in the Linux Codespace.

### Existing-project compatibility

I reran the existing Bell-state exercise in the Codespace:

```bash
python src/01_bell_state.py
```

The program completed successfully, rendered the circuit, and produced the expected Bell-state measurement distribution concentrated on `00` and `11`.

### Developer-experience observation

The transition from macOS to a Linux Codespace resolved the CUDA-Q Logical import problem without requiring changes to the project code. This confirms that the earlier failure was environment/platform-specific rather than a problem with the import syntax or CUDA-Q version.

The experience also highlights a potentially important onboarding distinction: a developer can use the base CUDA-Q package successfully on macOS, but a workflow that moves into CUDA-Q Logical may require switching to a supported Linux environment. A hosted Linux environment such as GitHub Codespaces provides a relatively low-friction workaround, but discovering that path currently requires the developer to diagnose the platform limitation first.

### Questions raised

- Could the CUDA-Q Logical quick-start documentation surface platform support before the first installation or import step?
- Should the documentation recommend a hosted Linux option, such as Codespaces or another containerized environment, for macOS users who want to experiment with CUDA-Q Logical?
- Could the CUDA-Q installation or import experience distinguish more clearly between base CUDA-Q platform support and CUDA-Q Logical platform support?
- Is there a recommended reproducible environment specification for developers who want to move between local CUDA-Q work and CUDA-Q Logical experimentation?

### Next step

Build the first CUDA-Q Logical exercise by taking the existing Bell-state workflow and adding logical resource estimation. This provides a controlled comparison between ordinary CUDA-Q execution and CUDA-Q Logical's resource-estimation path before moving to a more substantive fault-tolerant primitive.

---

## 2026-10-07 — First CUDA-Q Logical resource estimate

### Exercise

I created a second exercise, `src/02_logical_resource_estimate.py`, using an ordinary CUDA-Q Bell-pair kernel and the CUDA-Q Logical estimator target. The goal was to move from successful import/setup into the first resource-estimation workflow.

I ran:

```bash
python src/02_logical_resource_estimate.py
```

### Output

The script ran successfully in the Linux Codespace. Importing CUDA-Q Logical produced a preview warning:

```text
UserWarning: cudaq-logical is in preview. Its APIs, behavior, and documentation may change substantially in upcoming versions.
```

The existing CUDA-Q migration warning for `sample` and `observe` also appeared on import.

The estimator reported the backend stack as:

```text
== estimator :: CUDA-Q Logical backend stack =====================
---- CUDA-Q / QUAKE -> P0 --------------------------------
  ProgramBackend
    source: CUDA-Q / Quake
---- launch policies ---------------------------------------
  (none)
```

The logical resource estimate reported:

```text
Logical Bell-pair resources:
  peak logical qubits: 2
  logical action depth: 6
  logical actions: {'qlx_standard_cx': 1, 'qlx_standard_h': 1}
  logical instruments: {'qlx_standard_measure_z': 2, 'qlx_standard_prepare_zero': 2}
```

### Interpretation

The first Logical estimate completed successfully and reported the expected peak logical-qubit count of two for a Bell-pair kernel. The estimator stack also made the compilation boundary visible: the target stops at the portable logical P0 stage rather than selecting a code, device, or physical implementation.

The returned profile separates logical gate-like actions from state-preparation and measurement instruments. For this Bell-pair example, the profile contains one logical Hadamard action, one logical controlled-X action, two zero-state preparations, and two Z-basis measurements. The reported action-depth upper bound is six for this imported CUDA-Q kernel. In this small example, that value is numerically equal to the total number of reported actions and instruments, but it should still be treated as an upper-bound depth metric rather than assumed to be a general raw-operation count.

### Developer-experience observations

- The preview status of CUDA-Q Logical is surfaced immediately at import time, which is useful context for a developer experimenting with the API.
- The estimator's printed stack provides a concise view of where the workflow stops in the compilation pipeline.
- The action and instrument dictionaries make the resource model substantially easier to interpret than the depth value alone.
- Preparation and measurement are represented explicitly rather than being hidden behind the source kernel. This is an important distinction from a simple gate-count view of a circuit.
- The field name `action_depth_upper_bound` is not self-explanatory enough to infer its semantics safely without consulting documentation or inspecting the accompanying profile fields.

### Next step

Compare the CUDA-Q Logical profile with the resource-accounting conventions used in the FTQC Workbench, then choose a slightly richer reversible primitive whose logical-resource structure makes the comparison more informative.

---

## General observations

The early CUDA-Q experience has been positive overall. Basic installation and first-program workflows were straightforward, and the Quick Start provided enough information to get to a successful quantum program quickly.

The first notable friction appeared only when moving from base CUDA-Q into newer Logical functionality. That transition exposed a platform-support distinction that was not obvious during the initial macOS workflow. The resulting macOS-to-Linux Codespace transition is therefore useful both technically and as a developer-experience case study.

AI assistance has been most useful for accelerating command lookup, organizing observations, and identifying questions to investigate. The most valuable technical conclusions have come from directly running the software, comparing behavior across environments, and validating results against the official CUDA-Q documentation.
