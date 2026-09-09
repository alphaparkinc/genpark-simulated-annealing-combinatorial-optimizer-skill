# genpark-simulated-annealing-combinatorial-optimizer-skill

[![GitHub stars](https://img.shields.io/github/stars/alphaparkinc/genpark-simulated-annealing-combinatorial-optimizer-skill?style=social)](https://github.com/alphaparkinc/genpark-simulated-annealing-combinatorial-optimizer-skill/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-0%20external-brightgreen.svg)](#)
[![Model Context Protocol](https://img.shields.io/badge/MCP-Standard%20Compatible-orange.svg)](#)

> Autonomous Agent Simulated Annealing Combinatorial Metaheuristic Optimizer with 2-Opt Neighborhood Perturbation

Part of the **GenPark Autonomous Operations Research & Combinatorial Optimization Swarm**.

## Architecture Overview

```mermaid
graph TD
    A[Combinatorial Problem Initial State] --> B[Initial Temperature & Cooling Schedule]
    B --> C[Generate Neighbor Solution 2-Opt / Swap]
    C --> D[Calculate Objective Delta ΔE]
    D --> E{ΔE < 0?}
    E -->|Yes: Improvement| F[Accept Neighbor Solution]
    E -->|No: Worse Solution| G{Random < exp -ΔE / T?}
    G -->|Yes| F
    G -->|No| H[Reject Neighbor]
    F --> I[Update Incumbent Best Solution]
    H --> J[Cool Temperature T = T * alpha]
    I --> J
    J --> K{T < T_min or Max Iterations?}
    K -->|No| C
    K -->|Yes| L[Global Optimal Approximation & History]
```

## Features

- **Pure Python Standard Library**: Zero external dependencies (no NumPy, SciPy, or PuLP needed). Runs anywhere.
- **Production-Grade Design**: Type annotations, exhaustive edge cases, robust numerical stability.
- **MCP Server Ready**: Built-in stdio Model Context Protocol (MCP) server for Claude / Cursor / Agent tool calling.
- **Benchmark Validated**: 100% verified test coverage in isolated sandbox environments.

## Quickstart

```bash
git clone https://github.com/alphaparkinc/genpark-simulated-annealing-combinatorial-optimizer-skill.git
cd genpark-simulated-annealing-combinatorial-optimizer-skill
python example_usage.py
```

## Model Context Protocol (MCP) Usage

```bash
python mcp_server.py
```

## License

MIT License. Designed for autonomous agentic workflows.
