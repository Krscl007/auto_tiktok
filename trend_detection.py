import config
from TikTokApi import TikTokApi
from collections import Counter

def fetch_trends(count=10):
    api = TikTokApi()
    trends = api.trending(count=count)
    hashtags = [tag for vid in trends for tag in vid['desc'].split() if tag.startswith('#')]
    top = Counter(hashtags).most_common()
    return trends, top

if __name__ == '__main__':
    trends, top_hashtags = fetch_trends()
    print("Top Hashtags:", top_hashtags)
