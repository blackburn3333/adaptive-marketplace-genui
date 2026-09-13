"""
Filename: context_parser.py
Author: Jayendra Matarage
Created on: 9/6/2026 12:22 PM
Description: 
"""

from backend.app.utils.file_reader import load_yaml
from pathlib import Path
from typing import Dict, Any, Optional
import json

class ContextParser:
    def __init__(self,version):
        self.context_version = version
        self.root_path = PACKAGE_ROOT = Path(__file__).parent
        self.contex = {}

    def get_person_context(self, survey_answers: Dict[str, Any])-> Optional[Dict[str, Any]]:
        try:

            path = f"{self.root_path}/person_bio/{self.context_version}.yaml"
            config = load_yaml(path)

            system_instruction = config.get("system_prompt", "").strip()
            format_schema = config.get("output_schema", {})

            formatted_inputs = {}
            for key, template_str in survey_answers.items():
                value = survey_answers.get(key, "")
                formatted_inputs[key] = template_str.replace(f"{{{{ {key} }}}}", str(value))

            # 3. Construct user prompt string from inputs
            user_prompt = "\n".join([f"{k}: {v}" for k, v in formatted_inputs.items()])

            # 4. Extract model configuration and execution options
            model_cfg = config.get("model_config", {})
            ollama_exec = config.get("ollama_execution", {})

            # 5. Build structured Ollama payload
            self.context = {
                "model": ollama_exec.get("model", "gemma4:latest"),
                "prompt": user_prompt,
                "system": system_instruction,
                "stream": ollama_exec.get("stream", False),
                "keep_alive": ollama_exec.get("keep_alive", 0),
                "format": format_schema if model_cfg.get("format") == "json" else "json",
                "options": {
                    "temperature": model_cfg.get("temperature", 0.2),
                    "num_predict": model_cfg.get("max_tokens", 300)
                }
            }
            print(json.dumps(self.context, indent=2))
            return self.context

        except FileNotFoundError:
            print(f"Error: Prompt file not found at path")
            return None
        except Exception as e:
            print(f"Error building persona context: {e}")
            return None

