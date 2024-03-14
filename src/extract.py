import os
import requests
import pandas
from dotenv import load_dotenv

load_dotenv()

games_url = "https://api.igdb.com/v4/games"

requests_header = {
    "Client-ID": os.getenv('CLIENT_ID'),
    "Authorization": "Bearer " + os.getenv('CLIENT_SECRET')
}

games_body = """fields id, name, cover, game_engines, genres, involved_companies, platforms, aggregated_rating, aggregated_rating_count, rating, rating_count, release_dates,updated_at, websites;
 where first_release_date > 1704096000 & category = 0 & status = (0,4) & platforms = (169,167,130,6) & id = 221335;limit 500;"""

response = requests.post(games_url, headers=requests_header, data=games_body)

#CHECK RESPONSE
print("Status Code", response.status_code)
print("JSON Response", response.json())