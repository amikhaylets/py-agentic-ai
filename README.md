# py-agentic-ai
This section implements a basic agentic AI system with several key components:
- [agent_functions.py](agent_functions.py) - Core functionality for an AI-powered code generation agent:
    - Uses LiteLLM to interface with GPT-4
    - Implements an interactive function development workflow that iteratively improves code through multiple LLM calls
    - Takes user descriptions → generates basic function → adds documentation → creates test cases
    - Automatically saves the complete solution to a file
- [connection_test.py](connection_test.py) - Simple LLM connectivity test:
    - Handles API key management for both Google Colab and local environments
    - Tests the LiteLLM connection by asking GPT-4o to write a dictionary key-value swap function
- [simple_agent.py](simple_agent.py) - Fragment of an agent execution loop:
    - Implements the core agent pattern: prompt construction → LLM response → action parsing → tool execution → memory update
    - Supports basic file operations (list_files, read_file) and error handling
    - Uses conversational memory to maintain context across iterations