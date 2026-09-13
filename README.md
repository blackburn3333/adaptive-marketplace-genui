# Adaptive Marketplace: Generative UI Engine

An engineering prototype for a deterministic, schema-driven **Generative UI pipeline**. The system converts multi-choice onboarding survey responses into personalized user personas, dynamically ranks and matches catalog food items from a database, and generates custom UI configuration payloads using local LLMs (Ollama), FastAPI, MySQL, and Pydantic.

---

## 🏗️ Architecture Overview

The system operates across a sequential 3-stage pipeline:

1. **Persona Synthesis (Stage 1):** Transforms raw user survey responses into a standardized culinary profile (`gemma4:latest`).
2. **Food Selection & Matching (Stage 2):** Queries candidate catalog items from MySQL and ranks/evaluates them against the persona constraints (`gemma4:latest`).

### Repository Layout & Version Control

All YAML prompt assets, database migrations, and context parsing modules are organized within the backend structure:

```text
backend/
├── app/
│   ├── bridge/
│   │   ├── contexts/
│   │   │   ├── food_selection_home/
│   │   │   │   └── v1.0.0.yaml
│   │   │   └── person_bio/
│   │   │       └── v1.0.0.yaml
│   │   ├── __init__.py
│   │   └── context_parser.py
│   └── db/
│       └── migrations/
│           ├── 001_create_foods_table.sql
│           └── 002_seed_foods_data.sql