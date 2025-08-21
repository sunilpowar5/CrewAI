from crewai.tools import BaseTool
from langchain_community.tools import WikipediaQueryRun, ArxivQueryRun
from langchain_community.utilities import WikipediaAPIWrapper, ArxivAPIWrapper
from typing import Type
from pydantic import BaseModel, Field

class ArxivSearchInput(BaseModel):
    """Input schema for ArxivSearchTool."""
    query: str = Field(..., description="Search query for arXiv papers")

class WikipediaSearchInput(BaseModel):
    """Input schema for WikipediaSearchTool."""
    query: str = Field(..., description="Search query for Wikipedia articles")

class ArxivSearchTool(BaseTool):
    name: str = "arxiv_ai_research"
    description: str = "Search for AI research papers on arXiv. Use this to find recent papers about AI agents, machine learning, natural language processing, and related topics. Input should be a specific search query like 'AI agents', 'large language models', or 'machine learning optimization'. Returns paper titles, authors, summaries, and publication dates."
    args_schema: Type[BaseModel] = ArxivSearchInput

    def _run(self, query: str) -> str:
        """Execute the arXiv search."""
        try:
            # Create arXiv wrapper and tool
            arxiv_wrapper = ArxivAPIWrapper(
                top_k_results=5,
                doc_content_chars_max=4000
            )
            arxiv_tool = ArxivQueryRun(api_wrapper=arxiv_wrapper)
            
            # Execute search
            result = arxiv_tool.run(query)
            return result
        except Exception as e:
            return f"Error searching arXiv: {str(e)}"

class WikipediaSearchTool(BaseTool):
    name: str = "wikipedia_ai_concepts"
    description: str = "Search Wikipedia for AI-related concepts, definitions, and background information. Use this to understand AI terminology, historical context, and fundamental concepts mentioned in research papers. Input should be a specific term or concept like 'artificial intelligence', 'neural networks', or 'deep learning'."
    args_schema: Type[BaseModel] = WikipediaSearchInput

    def _run(self, query: str) -> str:
        """Execute the Wikipedia search."""
        try:
            # Create Wikipedia wrapper and tool
            wikipedia_wrapper = WikipediaAPIWrapper(
                top_k_results=3,
                doc_content_chars_max=4000
            )
            wikipedia_tool = WikipediaQueryRun(api_wrapper=wikipedia_wrapper)
            
            # Execute search
            result = wikipedia_tool.run(query)
            return result
        except Exception as e:
            return f"Error searching Wikipedia: {str(e)}"

# Create tool instances
arxiv_tool = ArxivSearchTool()
wikipedia_tool = WikipediaSearchTool()

# # Export functions
# def get_research_tools():
#     """Return a list of research tools for CrewAI agents."""
#     return [arxiv_tool, wikipedia_tool]

# def get_arxiv_tool():
#     """Return the arXiv search tool."""
#     return arxiv_tool

# def get_wikipedia_tool():
#     """Return the Wikipedia search tool."""
#     return wikipedia_tool

# # Main tools list
# tools = [arxiv_tool, wikipedia_tool]