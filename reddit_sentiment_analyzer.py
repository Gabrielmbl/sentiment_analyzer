from dotenv import dotenv_values
import praw
from pmaw import PushshiftAPI

# Load key variables from .env file
config = dotenv_values(".env")

# Access variables
CLIENT_ID = config.get("CLIENT_ID")
CLIENT_SECRET = config.get("CLIENT_SECRET")

reddit = praw.Reddit(
    user_agent=True,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
)

url = "https://www.reddit.com/r/compsci/comments/1anbb1b/the_most_beautiful_computer_science_paper_i_have/"
post = reddit.submission(url=url)
print(post)
print(post.selftext)