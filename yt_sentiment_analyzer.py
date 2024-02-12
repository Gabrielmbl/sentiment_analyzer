from dotenv import dotenv_values
import googleapiclient.discovery
import googleapiclient.errors

# Load key variables from .env file
config = dotenv_values(".env")

# Access variables
api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = config.get("DEVELOPER_KEY")

# Authenticate
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=DEVELOPER_KEY)

request = youtube.commentThreads().list(
    part="snippet",
    videoId="WNrB1Q9Rry0",
    maxResults=100
)

response = request.execute()

for item in response['items']:
    print(item['snippet']['topLevelComment']['snippet']['textDisplay'])

