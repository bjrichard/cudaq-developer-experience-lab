## CUDA-Q documentation and learning-path experience

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

### Next step

First, verify that the existing CUDA-Q exercises still run correctly under CUDA-Q 0.16.0. Then evaluate a supported Linux workflow for CUDA-Q Logical and document the setup path, any additional friction, and the resulting resource-estimation workflow.

### Compatibility check after the 0.16.0 upgrade

I reran the existing Bell-state exercise under CUDA-Q 0.16.0. The program still completed successfully, `cudaq.draw()` rendered the expected circuit, and the sampled measurement distribution remained concentrated on `00` and `11` as expected for the Bell-state preparation.

The same `FutureWarning` about upcoming changes to the `sample` and `observe` primitives appeared during normal execution. In other words, the upgrade did not break the existing exercise, but the migration warning is now part of the normal developer experience even for code that still executes correctly.

This separates two issues that initially appeared together:

- existing CUDA-Q code remains functional under 0.16.0, subject to a forward-looking API migration warning;
- CUDA-Q Logical is a separate availability/platform issue in the current macOS environment.

### Next step

Pin the project environment to CUDA-Q 0.16.0 for reproducibility, then move the CUDA-Q Logical experiment to a supported Linux environment and document that setup path.
