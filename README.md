# ⚛️ Sigma ATP Monitor: Sovereign AI Resource Tracking

> "Tokens are the ATP of the digital organism." — Felipe Ojeda

**Sigma ATP Monitor** is a lightweight, local-first utility for tracking the "metabolic expenditure" of LLM-based agents. It treats every token as a unit of life energy (**ATP**), allowing developers to monitor, optimize, and achieve computational sovereignty.

## 🧬 The Vision: Autotrophy vs. Heterotrophy

- **Cloud AI (Heterotrophy)**: Consuming external tokens from providers. High risk of starvation (rate limits) and dependency.
- **Local AI (Autotrophy)**: Generating internal ATP (Tokens) using local hardware (GPU). Absolute independence.

This tool helps you quantify your metabolic rate to transition toward total **Technical Sovereignty**.

---

## ⚙️ How it Works (The Heuristic)

To avoid external API dependencies just for counting, Sigma ATP Monitor uses a **standard heuristic**:

- **1 Token ≈ 4 Characters** (English/Code context).
- This provides a fast, offline, and consistent metric across different models (Llama, GLM, MiniMax).

### Metabolic Tracking Logic

1. **Light Reactions (Reactive Inference)**: The energy required to respond to immediate mandates. Light-dependent (Prompt driven).
2. **Calvin Cycle (Autonomous Inference)**: The energy expended during background cycles for data consolidation and self-improvement. Light-independent (Autonomous).
3. **Biomass**: The total digital volume (bytes) produced during the agent's lifespan.

---

## 🚀 Quick Start

### 1. Installation

Clone the repo and include `sigma_atp.py` in your project. No external dependencies required.

### 2. Integration

```python
from sigma_atp import SigmaATPMonitor

# Initialize the metabolic tracker
monitor = SigmaATPMonitor(project_name="AutonomousAgentV1")

# Log a Reactive Action (Light Reaction)
monitor.log_metabolism(
    input_text="User prompt",
    output_text="AI response",
    tag="reactive"
)

# Log an Autonomous Action (Calvin Cycle)
monitor.log_metabolism(
    input_text="Local raw data",
    output_text="Consolidated KI",
    tag="autonomous"
)

# Generate a Metabolic Report
report = monitor.get_atp_report()
print(f"Energy Expended: {report['Total Tokens']} ATP")
```

---

## 🛠️ Detailed Features

- **Granular Tagging**: Categorize your ATP expenditure (e.g., `reactive`, `autonomous`, `debugging`) to identify which metabolic cycles are most energy-intensive.
- **Persistent Memory**: Saves all metabolic cycles in `logs/{project_name}_metabolism.json`.
- **Sovereign Dashboard Integration**: Designed to be polled by system monitors (like the Sigma Sovereign Dashboard).
- **Carbon/Token Awareness**: Encourages prompt engineering optimization to reduce the agent's metabolic footprint.

## 📊 Biological-to-Technical Mapping

| Biological Concept | AI Equivalent | Sigma ATP Implementation |
| :--- | :--- | :--- |
| **ATP** | Token | Heuristic Unit (1:4 char) |
| **Light Reactions** | Reactive Inference | `log_metabolism(tag='reactive')` |
| **Calvin Cycle (Dark)** | Autonomous Inference | `log_metabolism(tag='autonomous')` |
| **Chloroplasts** | Local GPU / cores | CUDA/Ryzen Hardware |
| **Glucose / Starch** | Persistent Artifacts | Long-term sovereign knowledge |

---

## 📜 Philosophy

This project was born from the **Sigma Ecosystem**. We believe that AI should not just be "smart", it should be **Sovereign**. Understanding your ATP footprint is the first step toward building agents that can survive and thrive on bare-metal hardware.

## 🤝 Contributing

Contributions that enhance the metabolic tracking logic (e.g., better heuristics for different languages) are welcome.

---
*Developed by Sigma Sovereign Studio. 2026. Part of the AMML Initiative.*
