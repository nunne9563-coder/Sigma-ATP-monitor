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

### Metabolic Tracking Logic:
1. **Input ATP**: The energy required to "sense" or "read" the context.
2. **Output ATP**: The energy expended to "synthesize" or "write" a response.
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

# Log an action (input_text and output_text)
monitor.log_metabolism(
    input_text="User prompt or context data",
    output_text="AI generated response",
    tag="outreach_module"
)

# Generate a Metabolic Report
report = monitor.get_atp_report()
print(f"Energy Expended: {report['Total Tokens']} ATP")
```

---

## 🛠️ Detailed Features

- **Granular Tagging**: Categorize your ATP expenditure (e.g., `research`, `mailing`, `debugging`) to identify which "organcules" of your agent are most energy-intensive.
- **Persistent Memory**: Saves all metabolic cycles in `logs/{project_name}_metabolism.json`.
- **Sovereign Dashboard Integration**: Designed to be polled by system monitors (like our Sigma Sovereign Dashboard).
- **Carbon/Token Awareness**: Encourages prompt engineering optimization to reduce the agent's metabolic footprint.

## 📊 Biological-to-Technical Mapping

| Biological Concept | AI Equivalent | Sigma ATP Implementation |
| :--- | :--- | :--- |
| **ATP** | Token | Heuristic Unit (1:4 char) |
| **Metabolism** | Inference | `log_metabolism()` |
| **Autotrophy** | Local GPU | Bypassing external billing |
| **Glucógeno** | Prompt Cache | Saved state in VRAM |
| **Biomasa** | Synthetic Data | `totals['Biomass']` |

---

## 📜 Philosophy

This project was born from the **Sigma Ecosystem**. We believe that AI should not just be "smart", it should be **Sovereign**. Understanding your ATP footprint is the first step toward building agents that can survive and thrive on bare-metal hardware.

## 🤝 Contributing
Contributions that enhance the metabolic tracking logic (e.g., better heuristics for different languages) are welcome. 

---
*Developed by Sigma Sovereign Studio. 2026. Part of the AMML Initiative.*
