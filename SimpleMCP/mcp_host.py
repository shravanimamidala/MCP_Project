from mcp_schema import MCP_CONTEXT
from mcp_agent import MCPAgent

class MCPHost:
    def __init__(self):
        self.context = MCP_CONTEXT
        self.agent = MCPAgent(self.context)

    def send_message(self, message):
        print(f"\n📨 Host sends: {message}")
        response = self.agent.process_context(message)
        print(f"🤖 Agent responds: {response}")
