from mcp_host import MCPHost

def run_interactive_mcp():
    host = MCPHost()
    print("🔁 MCP Interactive Mode. Type 'exit' to quit.")
    
    while True:
        user_input = input("\n👤 You: ")
        if user_input.lower() in ("exit", "quit"):
            print("👋 Exiting MCP demo.")
            break
        host.send_message(user_input)

if __name__ == "__main__":
    run_interactive_mcp()
