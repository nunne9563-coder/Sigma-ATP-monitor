# Sigma ATP Monitor: Technical Specifications (v3.0)

## 1. Computational Metabolism Framework

The Sigma ATP Monitor treats LLM inference as a metabolic process. For developers, this translates to the management of **Token Throughput** and **Compute Cost**.

### 1.1 Reactive Inference (Light Reactions)
- **Definition**: Real-time, synchronous LLM calls triggered by user interaction (Prompts).
- **Technical Scope**: Interactive Chat UI, live RAG retrieval, real-time command execution.
- **ATP Priority**: High (Priority is given to low latency over energy efficiency).

### 1.2 Autonomous Consolidation (The Calvin Cycle)
- **Definition**: Asynchronous, background processing independent of user activity.
- **Technical Scope**: Database indexing, Knowledge Item (KI) synthesis, self-correction logs, mass-data validation.
- **ATP Priority**: Optimized (Focus on high-density data fixation/serialization).

---

## 2. ATP Heuristic Logic

To maintain zero-latency and 100% local operation, the monitor uses a **Character-to-Token Heuristic (CTH)**.

- **Formula**: `ATP_estimate = total_chars / 4`
- **Rationale**: Based on common tokenizers (Tiktoken/Llama-tokenizer) where 4 characters represent the average sub-word unit in English/Code.
- **Implementation**: Pure Python linear complexity `O(n)`. No heavy dependencies required.

---

## 3. Data Fixation (The RuBisCO Engine)

In biology, RuBisCO is the enzyme that fixes CO2. In the Sigma ATP Monitor, this refers to the **Structured Output Persistence**:

- **Input Raw**: Unstructured text/context.
- **Process**: LLM Reasoning + Output Parsing.
- **Fixation**: Persistent JSON storage (`history` and `totals` nodes).
- **Stability**: Ensures the agent's work survives session crashes (Persistence Tier 1).

---

## 4. Architectural Autotrophy (Local vs Cloud)

| Metric | Heterotroph (Cloud) | Autotroph (Local) |
| :--- | :--- | :--- |
| **Energy Source** | External Credits / API Keys | Local Electricity + VRAM |
| **Latency** | Network Dependent | Hardware Dependent |
| **Sovereignty** | Limited (Third-party logs) | Absolute (Zero-trace) |
| **Recovery** | Waiting on Rate Limits | GPU Cycle Turnaround |

---

## 5. Integration Best Practices

Developers should integrate the ATP Monitor at the **Orchestrator Level**:

```python
# Best Practice: Wrap the completion call
def get_completion(prompt):
    response = llm.generate(prompt)
    atp_monitor.log_metabolism(prompt, response, tag="autonomous")
    return response
```

Use tags like `reactive`, `autonomous`, `system_health`, and `security_audit` for granular metabolic analysis.

---
*Technical Sovereignty through Precise Resource Management.*
