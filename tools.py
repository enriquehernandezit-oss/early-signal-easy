import os
import requests
from dotenv import load_dotenv

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

def search_web(query: str) -> str:
    """Search the web using Tavily and return results as text."""
    try:
        response = requests.post(
            "https://api.tavily.com/search",
            json={
                "api_key": TAVILY_API_KEY,
                "query": query,
                "max_results": 5,
                "search_depth": "basic"
            }
        )
        data = response.json()
        results = data.get("results", [])
        if not results:
            return "No results found."
        output = []
        for r in results:
            output.append(f"Title: {r.get('title')}\nURL: {r.get('url')}\nSummary: {r.get('content', '')}\n")
        return "\n".join(output)
    except Exception as e:
        return f"Search error: {str(e)}"


def search_reddit(query: str, subreddit: str = "all") -> str:
    """Search Reddit for posts matching a query."""
    try:
        headers = {"User-Agent": "EarlySignal/1.0"}
        url = f"https://www.reddit.com/r/{subreddit}/search.json"
        params = {
            "q": query,
            "sort": "new",
            "limit": 10,
            "t": "month"
        }
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        if not posts:
            return "No Reddit posts found."
        output = []
        for post in posts[:5]:
            p = post["data"]
            output.append(
                f"Title: {p.get('title')}\n"
                f"Subreddit: r/{p.get('subreddit')}\n"
                f"Upvotes: {p.get('ups')}\n"
                f"Text: {p.get('selftext', '')[:200]}\n"
            )
        return "\n".join(output)
    except Exception as e:
        return f"Reddit search error: {str(e)}"
    