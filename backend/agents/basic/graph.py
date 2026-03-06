##########
# ### Import Packages

from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent

from agents.models import chat_model

##########
# ### Starter Agent
#
# This is a minimal working agent to verify your environment is set up.
# Replace it with your own agent for your chosen domain:
#   - Car Purchasing Agent
#   - Travel Planning Agent
#   - Meal Planning Agent
#

@tool(description="A placeholder tool. Replace with your own.")
def hello(name: str) -> str:
    """Say hello — confirms your agent is running."""
    return f"Hello, {name}! Your agent is working. Time to build something great."


graph = create_react_agent(
    model=chat_model(),
    tools=[hello],
    prompt="You are a helpful assistant. Replace this with your agent's system prompt.",
)
