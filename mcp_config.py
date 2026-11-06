"""Bright Data MCP server config shared by all agents."""
import os
from pathlib import Path

from dotenv import load_dotenv
from mcp_use.client.connectors.base import BaseConnector

load_dotenv()


def _drop_null_tool_args() -> None:
    """mcp-use fills omitted optional tool params with None and sends them as
    JSON null, which Bright Data's schema validation rejects (e.g. `country`).
    Strip None values so the server applies its own defaults."""
    if getattr(BaseConnector.call_tool, "_drops_nulls", False):
        return
    original = BaseConnector.call_tool

    async def call_tool(self, name, arguments, *args, **kwargs):
        arguments = {k: v for k, v in (arguments or {}).items() if v is not None}
        return await original(self, name, arguments, *args, **kwargs)

    call_tool._drops_nulls = True
    BaseConnector.call_tool = call_tool


_drop_null_tool_args()


def _npx_command() -> tuple[str, list, dict]:
    """Prefer the Node.js bundled by the `nodejs-wheel` pip package (used on
    Streamlit Community Cloud, which has no Node by default); fall back to a
    system `npx` on PATH."""
    try:
        import nodejs_wheel

        root = Path(nodejs_wheel.__file__).parent
        node = root / "bin" / "node"
        npx_cli = root / "lib" / "node_modules" / "npm" / "bin" / "npx-cli.js"
        if node.exists() and npx_cli.exists():
            # The MCP package's entry point uses `#!/usr/bin/env node`, so the
            # bundled node must also come first on the child process PATH.
            path = os.pathsep.join([str(node.parent), os.environ.get("PATH", "")])
            return str(node), [str(npx_cli)], {"PATH": path}
    except ImportError:
        pass
    return "npx", [], {}


def bright_data_mcp_config() -> dict:
    env = {
        "API_TOKEN": os.getenv("BRIGHT_DATA_API_TOKEN", ""),
        # Only expose the tools the agents actually use. This keeps the agent's
        # tool list small (better tool choice on Gemini Flash) and avoids
        # tools whose recursive JSON schemas mcp-use cannot convert.
        "TOOLS": os.getenv("BRIGHT_DATA_TOOLS", "search_engine,scrape_as_markdown"),
    }
    # Only pass zone names if explicitly configured; otherwise @brightdata/mcp
    # uses (and auto-creates) its own default zone in your account.
    for var in ("WEB_UNLOCKER_ZONE", "BROWSER_ZONE"):
        if os.getenv(var):
            env[var] = os.environ[var]
    command, prefix_args, extra_env = _npx_command()
    env.update(extra_env)
    return {
        "mcpServers": {
            "Bright Data": {
                "command": command,
                "args": [*prefix_args, "-y", "@brightdata/mcp"],
                "env": env,
            }
        }
    }
