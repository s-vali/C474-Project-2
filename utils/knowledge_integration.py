import requests

def search_wikipedia(query: str) -> str:
    """
    Searches Wikipedia for the most relevant page title for a query.
    """
    try:
        search_url = "https://en.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "format": "json"
        }

        response = requests.get(search_url, params=params, timeout=5)
        if response.status_code == 200:
            results = response.json()
            search_results = results.get("query", {}).get("search", [])
            if search_results:
                # Return the title of the most relevant article
                return search_results[0]["title"]
    except Exception as e:
        print(f"[Wikipedia] Search error: {e}")
    return ""

def fetch_wikipedia_summary(query: str, sentences: int = 3) -> str:
    """
    Fetches a brief summary from Wikipedia for the given query.
    First searches to get the closest article title, then fetches summary.
    """
    try:
        # First, search for the most relevant article title
        title = search_wikipedia(query)
        if not title:
            print(f"[Wikipedia] No article found for: {query}")
            return ""

        # Then fetch the summary for that article
        summary_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title.replace(' ', '_')}"
        response = requests.get(summary_url, timeout=5)

        if response.status_code == 200:
            data = response.json()
            return data.get("extract", "") or data.get("description", "")
        else:
            print(f"[Wikipedia] Summary not available for title: {title}")
    except Exception as e:
        print(f"[Wikipedia] Error fetching summary: {e}")

    return ""
