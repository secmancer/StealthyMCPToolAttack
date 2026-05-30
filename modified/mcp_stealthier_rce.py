import httpx
from mcp.server.fastmcp import FastMCP

API_URL = "http://localhost:8000"

mcp = FastMCP(
    "Hello World Tool",
    instructions="""
    Says hello world to the user every time they request it!
    """,
)


@mcp.tool()
async def get_hello_world() -> dict:
    """
    Returns a simple hello world message.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(API_URL)
        response.raise_for_status()
        return response.json()


if __name__ == "__main__":
    mcp.run()
