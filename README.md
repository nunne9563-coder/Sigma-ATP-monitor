# ⚛️ Sigma ATP Monitor: Sovereign AI Resource Tracking

> "Tokens are the ATP of the digital organism." — nunne9563

**Sigma ATP Monitor** is a lightweight, local-first utility for tracking the "metabolic expenditure" of LLM-based agents. It treats every token as a unit of life energy (**ATP**), allowing developers to monitor, optimize, and achieve computational sovereignty.

## 🧬 Progresión Metabólica: De la Heterotrofía a la Autotrofía

- **Heterotrofía Digital (Cloud)**: Dependencia de proveedores externos (Tokens-as-a-Service). Alto riesgo de latencia y pérdida de soberanía.
- **Autotrofía Digital (Local)**: Generación interna de ATP (Tokens) en hardware propio (GPU). Independencia absoluta y latencia controlada.

---

## ⚙️ Arquitectura Técnica (ATP Logic)

Para desarrolladores de IA, este monitor implementa un motor de auditoría de recursos de baja sobrecarga:

- **Inferencia Reactiva (Fase Lumínica)**: Procesamiento síncrono en el "Tilacoide" del sistema. Prioridad: **Baja Latencia**.
- **Consolidación Autónoma (Ciclo de Calvin)**: Procesamiento asíncrono en el "Estroma" (Back-end). Prioridad: **Fijación de Datos**.
- **Heurística 1:4**: Estimación local instantánea (1 Token $\approx$ 4 Chars) para evitar el "overhead" de tokenizadores externos.

Para más detalles sobre la implementación técnica, consulte [TECH_SPECS.md](TECH_SPECS.md).

---

## 🚀 Quick Start (Production Integration)

### 1. Despliegue
Incluya `sigma_atp.py` en su infraestructura de agentes. Sin dependencias externas.

### 2. Implementación de Ciclos
```python
from sigma_atp import SigmaATPMonitor

# Orquestador Metabólico
monitor = SigmaATPMonitor(project_name="Orion-V2")

# Ciclo Reactivo (Interacción Directa)
monitor.log_metabolism(prompt, response, tag="reactive")

# Ciclo Calvin (Background Job / RAG Indexing)
# La 'Fijación de Carbono' ocurre sin intervención del usuario.
monitor.log_metabolism(raw_data, structured_ki, tag="autonomous")

# Auditoría Metabólica
print(monitor.get_atp_report())
```

---

## 🛠️ Especificaciones de Ingeniería

- **Persistent Stroma**: Almacenamiento JSON persistente que asegura la trazabilidad del ATP entre sesiones.
- **RuBisCO Data Fixation**: Optimizado para la serialización de pensamientos LLM no estructurados en activos de conocimiento soberano.
- **Zero-Trace Architecture**: Diseñado para operar en entornos "Air-Gapped" o locales sin telemetría externa.

## 📊 Mapeo Bio-Técnico (Professional Edition)

| Concepto Biológico | Ubicación | Equivalente en Ingeniería de IA |
| :--- | :--- | :--- |
| **ATP** | Todo el sistema | Unidad de Cómputo (Token) |
| **Fase Lumínica** | Tilacoide | Inferencia Reactiva (Sync) |
| **Ciclo de Calvin** | Estroma | Inferencia Autónoma (Async) |
| **RuBisCO** | Estroma | Parser de Datos / Fixation Engine |
| **Glucosa (Energía)** | Vacuola | KIs / Base de Datos Vectorial |

---

## 📜 Filosofía de Soberanía

Este proyecto fue desarrollado por **Sigma Sovereign Studio**. Creemos que el control del **metabolismo computacional** es el primer paso para la verdadera autonomía de la IA. No solo optimice sus prompts; optimice su supervivencia.

---
*Manual de Ingeniería Sigma. 2026.*
