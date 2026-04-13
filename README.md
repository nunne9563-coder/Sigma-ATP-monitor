# ⚛️ Sigma ATP Monitor: Sovereign AI Resource Tracking

> "Tokens are the ATP of the digital organism." — Felipe Ojeda

Sigma ATP Monitor is a lightweight, local-first utility for tracking the "metabolic expenditure" of LLM-based agents. It treats every token as a unit of life energy (ATP), allowing developers to monitor, optimize, and achieve computational sovereignty.

## 🧬 The Vision: Autotrophy vs. Heterotrophy

- **Cloud AI (Heterotrophy)**: Consuming external tokens from providers. High risk of starvation (rate limits) and dependency.
- **Local AI (Autotrophy)**: Generating internal ATP (Tokens) using local hardware (GPU). Absolute independence.

This tool helps you quantify your metabolic rate to transition toward total Technical Sovereignty.

## 🚀 Quick Start

```python
from sigma_atp import SigmaATPMonitor

# Initialize the metabolic tracker
monitor = SigmaATPMonitor(project_name="AutonomousAgentV1")

# Log an action (input_text and output_text)
# Establishes a 1:4 character-to-token heuristic
monitor.log_metabolism(input_data, output_data)

# Get current ATP stats
stats = monitor.get_atp_report()
print(f"Total ATP Expended: {stats['Total Tokens']}")
```

## 🛠️ Features

- **Heuristic Token Counting**: Fast, local-only estimation without API calls.
- **Biomass Tracking**: Monitor the total volume of data (bytes) synthesized by your agent.
- **Sovereign Logging**: Persistent JSON-based tracking of all metabolic cycles.
- **Zero-Dependency**: Pure Python, compatible with all local LLM wrappers.

## 📜 Philosophy

This project was born from the **Sigma Ecosystem**, where we believe that AI should not just be "smart", but should be **Sovereign**. Understanding your ATP footprint is the first step toward building agents that can survive and thrive on bare-metal.

---
*Developed by Sigma Sovereign Studio. 2026.*
