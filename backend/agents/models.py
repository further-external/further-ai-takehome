##########
# ### Import Packages

from functools import lru_cache
from langchain_google_genai import ChatGoogleGenerativeAI

# Uncomment below if using alternative providers
# from langchain_openai import ChatOpenAI
# from langchain_anthropic import ChatAnthropic

##########
# ### Define Model Get Functions

# lru_cache allows reuse of HTTP connection pool
@lru_cache(maxsize=4)
def chat_model(model: str = "default"):
    """Return a chat model instance. Defaults to Gemini (provided API key).

    To use your own keys for other providers, uncomment the relevant
    imports above and add elif branches below.
    """

    if model == "default":
        return ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=1.0,
        )

    # Example: add your own provider
    # elif model == "openai":
    #     return ChatOpenAI(model="gpt-4.1-2025-04-14", stream_usage=True)

    raise ValueError(f"Unknown model: {model}")


@lru_cache(maxsize=8)
def search_model(model: str = 'default'):

    search_llm = ChatGoogleGenerativeAI(
            model='gemini-3-flash-preview',
            temperature=1.0,  # Gemini 3.0 recommend temp=1
        )
    search_llm = search_llm.bind_tools([{"google_search": {}}])

    if model == 'sonnet-4.5':
        search_llm = ChatAnthropic(
            model='claude-sonnet-4-5-20250929',  # type: ignore
        ) # type: ignore
        search_llm = search_llm.bind_tools([
            {
                "type": "web_search_20250305",
                "name": "web_search",
            }
        ])

    if model == 'gpt-4.1':
        search_llm = ChatOpenAI(
            model='gpt-4.1-2025-04-14',
            stream_usage=True,
            output_version='responses/v1',
        )
        search_llm = search_llm.bind_tools([{"type": "web_search"}])

    return search_llm