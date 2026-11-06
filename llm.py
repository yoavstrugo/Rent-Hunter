"""Central LLM factory - all agents get their chat models from here (Google Gemini)."""
import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

API_KEY_VAR = "GOOGLE_AI_STUDIO_API_KEY"

# Override in .env if you want a different model (see https://ai.google.dev/gemini-api/docs/models)
DEFAULT_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.5-flash")
FAST_MODEL = os.getenv("GEMINI_FAST_MODEL", "gemini-3.5-flash-lite")


def _make(model: str) -> ChatGoogleGenerativeAI:
    api_key = os.getenv(API_KEY_VAR)
    if not api_key:
        raise RuntimeError(f"{API_KEY_VAR} is not set - add it to your .env file")
    return ChatGoogleGenerativeAI(
        model=model,
        google_api_key=api_key,
        temperature=0,
        max_retries=6,  # free tier is rate limited; back off and retry on 429s
    )


def get_llm() -> ChatGoogleGenerativeAI:
    """Stronger model for structured extraction / analysis."""
    return _make(DEFAULT_MODEL)


def get_fast_llm() -> ChatGoogleGenerativeAI:
    """Cheaper, faster model for tool-calling agents and simple tasks."""
    return _make(FAST_MODEL)
