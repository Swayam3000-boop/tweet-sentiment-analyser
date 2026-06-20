import os


def _tweet_text(tweet):
    if isinstance(tweet, dict):
        text = tweet.get("text") or tweet.get("full_text")
        return text.strip() if isinstance(text, str) else ""

    text = getattr(tweet, "text", None) or getattr(tweet, "full_text", None)
    if isinstance(text, str):
        return text.strip()

    to_dict = getattr(tweet, "to_dict", None)
    if callable(to_dict):
        return _tweet_text(to_dict())

    return ""


def search_xquik_posts(query, limit=1):
    api_key = os.environ.get("X_TWITTER_SCRAPER_API_KEY")
    if not api_key:
        raise RuntimeError("Set X_TWITTER_SCRAPER_API_KEY to load X posts.")

    cleaned_query = query.strip()
    if not cleaned_query:
        raise RuntimeError("Enter a search query first.")

    from x_twitter_scraper import XTwitterScraper

    client = XTwitterScraper(api_key=api_key)
    result = client.x.tweets.search(q=cleaned_query, limit=limit)
    return [text for tweet in getattr(result, "items", []) if (text := _tweet_text(tweet))]
