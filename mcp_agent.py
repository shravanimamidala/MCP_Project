import json

class MCPAgent:
    def __init__(self, context):
        self.context = context

    def process_context(self, user_input):
        self.context["input"] = user_input
        print("🧠 Agent received context:")
        print(json.dumps(self.context, indent=2))

        response = self._generate_response(user_input)
        return response

    def _generate_response(self, user_input):
        tools = [tool["name"] for tool in self.context["tools"]]
        if "read" in user_input.lower():
            if "file_reader" in tools:
                return "Using `file_reader` to fetch the file contents..."
            else:
                return "No file tool available."
        elif "search" in user_input.lower():
            if "data_search" in tools:
                return "Using `data_search` to perform your query..."
            else:
                return "No search tool available."
        else:
            return "I'm ready. What would you like me to do?"
