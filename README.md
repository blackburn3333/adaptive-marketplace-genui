# Adaptive Marketplace: Generative UI Engine

An engineering prototype for a deterministic, schema-driven **Generative UI pipeline**. The system converts multi-choice onboarding survey responses into personalized user personas, dynamically ranks and matches catalog food items from a database, and generates custom UI configuration payloads using local LLMs (Ollama), FastAPI, MySQL, and Pydantic.

---

## 🏗️ Architecture Overview

The system operates across a sequential 3-stage pipeline:

1. **Persona Synthesis (Stage 1):** Transforms raw user survey responses into a standardized culinary profile (`gemma4:latest`).
2. **Food Selection & Matching (Stage 2):** Queries candidate catalog items from MySQL and ranks/evaluates them against the persona constraints (`gemma4:latest`).