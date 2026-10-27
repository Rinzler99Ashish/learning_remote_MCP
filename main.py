from fastmcp import FastMCP

mcp = FastMCP("Text Analyzer")

@mcp.tool()
def analyze_text(text: str) -> dict:
    """Analyze text and return word and character counts."""
    return {
        "characters": len(text),
        "words": len(text.split()),
        "uppercase": text.upper(),
        "lowercase": text.lower()
    }

if __name__ == "__main__":
    mcp.run(transport='http', host='0.0.0.0', port=8000)