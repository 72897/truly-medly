from tools.github_tool import search_repositories
from tools.weather_tool import get_weather


class ExecutorAgent:

    def normalize_weather_input(self, input_data):
        """
        Normalize different LLM parameter names
        """
        if "city" in input_data:
            return {"city": input_data["city"]}

        if "location" in input_data:
            return {"city": input_data["location"]}

        if "place" in input_data:
            return {"city": input_data["place"]}

        raise ValueError("WeatherTool requires a city/location parameter")

    def execute(self, plan: dict):
        results = []

        for step in plan.get("steps", []):
            tool = step.get("tool")
            input_data = step.get("input", {})

            try:
                if tool == "GitHubTool":
                    output = search_repositories(**input_data)

                elif tool == "WeatherTool":
                    normalized = self.normalize_weather_input(input_data)
                    output = get_weather(**normalized)

                else:
                    output = {"error": "Unknown tool"}

            except Exception as e:
                output = {"error": str(e)}

            results.append({
                "step_id": step.get("id"),
                "tool": tool,
                "output": output
            })

        return results
