"""
Filename: context_parser.py
Author: Jayendra Matarage
Created on: 9/6/2026 12:22 PM
Description: 
"""

from backend.app.utils.file_reader import load_yaml
from pathlib import Path
from typing import Dict, Any, Optional, List
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

    def get_matching_foods(
            self, persona: Dict[str, Any], candidate_foods: List[Dict[str, Any]]
    ) -> Optional[Dict[str, Any]]:

        try:
            file_path = f"{self.root_path}/food_selection_home/{self.context_version}.yaml"
            config = load_yaml(str(file_path))

            # 1. Extract system instruction and output schema
            system_instruction = config.get("system_prompt", "").strip()
            format_schema = config.get("output_schema", {})

            # 2. Extract dynamic inputs map from YAML template
            input_templates = config.get("inputs", {})

            # Convert python objects to structured JSON strings for template injection
            persona_json_str = json.dumps(persona, indent=2)
            foods_json_str = json.dumps(candidate_foods, indent=2)

            input_values = {
                "user_persona_json": persona_json_str,
                "candidate_foods_json": foods_json_str
            }

            formatted_inputs = {}
            for key, template_str in input_values.items():
                value = input_values.get(key, "")
                formatted_inputs[key] = template_str.replace(f"{{{{ {key} }}}}", str(value))

            user_prompt = "\n\n".join([f"{k.upper()}:\n{v}" for k, v in formatted_inputs.items()])

            model_cfg = config.get("model_config", {})
            ollama_exec = config.get("ollama_execution", {})

            self.context = {
                "model": ollama_exec.get("model", "gemma4:latest"),
                "prompt": user_prompt,
                "system": system_instruction,
                "stream": ollama_exec.get("stream", False),
                "keep_alive": ollama_exec.get("keep_alive", 0),
                "format": format_schema if model_cfg.get("format") == "json" else "json",
                "options": {
                    "temperature": model_cfg.get("temperature", 0.2),
                    "num_predict": model_cfg.get("max_tokens", 600)
                }
            }
            return self.context

        except FileNotFoundError:
            print(f"Error: Prompt file not found at path")
            return None
        except Exception as e:
            print(f"Error building food matching context: {e}")
            return None





person = {
  "persona_code": "Eco-Conscious Efficiency Seeker",
  "target_archetype": "The Health-Minded Pragmatist",
  "synthesized_profile": "This user is highly motivated by weight loss and operates under strict budgetary constraints. They prioritize speed and convenience, suggesting a busy lifestyle. The vegan requirement narrows the protein and ingredient pool significantly, while the spicy preference adds a flavor dimension. The low budget dictates a focus on staple, nutrient-dense, and affordable whole foods.",
  "suitable_food_types": [
    "High-Protein Vegan Snacks",
    "Quick-Prep Meal Bases (e.g., Lentil Bowls, Tofu Scrambles)",
    "Spicy, Fiber-Rich Sides"
  ],
  "key_attributes": [
    "Vegan",
    "Spicy Flavor",
    "Under 100 LKR per serving",
    "Minimal Preparation Time (<10 minutes)"
  ],
  "max_budget_lkr": 100.00
}

foods_list = [
    {
        "food_id": 101,
        "name": "Spicy Roasted Chickpeas",
        "price_per_unit": 90,
        "unit": "pack",
        "description": "Crunchy oven-roasted chickpeas spiced with chili, cumin, and sea salt.",
        "tags": ["vegan", "organic", "spicy", "snack", "low-calorie"],
        "image_url": "https://example.com/images/chickpeas.jpg",
        "nutrition_facts": {"calories": 160, "protein": 7, "carbohydrates": 22, "fats": 4}
    },
    {
        "food_id": 102,
        "name": "Organic Moringa Herbal Tea",
        "price_per_unit": 80,
        "unit": "pack",
        "description": "Nutrient-rich, hand-picked moringa leaf tea bags packed with thermogenic antioxidants.",
        "tags": ["vegan", "organic", "beverage", "zero-prep", "low-calorie"],
        "image_url": "https://example.com/images/moringa.jpg",
        "nutrition_facts": {"calories": 10, "protein": 1, "carbohydrates": 2, "fats": 0}
    },
    {
        "food_id": 103,
        "name": "Deviled Chili Cashews",
        "price_per_unit": 150,
        "unit": "pack",
        "description": "Premium Sri Lankan cashews roasted with crushed red pepper flakes and curry leaves.",
        "tags": ["vegan", "spicy", "snack", "high-protein"],
        "image_url": "https://example.com/images/cashews.jpg",
        "nutrition_facts": {"calories": 280, "protein": 9, "carbohydrates": 14, "fats": 22}
    }
]

parser = ContextParser(version="v1.0.0")
ollama_payload = parser.get_matching_foods(persona=person, candidate_foods=foods_list)

print(json.dumps(ollama_payload, indent=2))