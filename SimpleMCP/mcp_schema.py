# Defines the basic structure of an MCP context window

MCP_CONTEXT = {
    "system": {
        "name": "LegacyLink Host",
        "purpose": "Facilitate AI-based access to local data and tools"
    },
    "tools": [
        {"name": "file_reader", "description": "Read contents of a file"},
        {"name": "data_search", "description": "Search local database"},
    ],
    "memory": {
        "recent_tasks": ["Searched 'gene expression'", "Read file 'notes.txt'"]
    },
    "input": "",
}
