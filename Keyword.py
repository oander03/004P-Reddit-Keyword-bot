import praw
import unicodedata

# Reddit API Credentials
reddit = praw.Reddit(
    client_id="wzgKAk7CBdP4nMAQNiGOyQ",
    client_secret="519pDj1lo7F73KkuEDqPr8gWIYUgLA",
    user_agent="KeywordCounterBot"
)

subreddit_name = "leagueoflegends"
keyword = "toxic"

subreddit = reddit.subreddit(subreddit_name)
count = sum(1 for post in subreddit.search(keyword, limit=10000))

print(f"Number of posts containing '{keyword}' in r/{subreddit_name}: {count}")

posts = list(subreddit.search(keyword, limit=30, sort="relevance"))

if posts:
    print(f"Top 30 posts containing '{keyword}' in r/{subreddit_name}:\n")
    for i, post in enumerate(posts, start=1):
        title_cleaned = unicodedata.normalize('NFKD', post.title).encode('ascii', 'ignore').decode('ascii')
        print(f"{i}. {title_cleaned}")
        print(f"   URL: {post.url}\n")
else:
    print(f"No posts found for '{keyword}' in r/{subreddit_name}.")