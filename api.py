from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")

app = FastAPI()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="user-top-read playlist-modify-public",
    cache_path=os.path.join(os.path.dirname(__file__), "spotify_cache")
))

class MoodRequest(BaseModel):
    mood: str

@app.get("/health")
async def health_check():
    return {"status": "API is running"}

@app.post("/recommend")
async def recommend_songs(request: MoodRequest):
    try:
        query = f"genre:{'blues' if 'sad' in request.mood.lower() else 'pop'}"
        results = sp.search(q=query, type="track", limit=5)
        tracks = results["tracks"]["items"]
        return {"tracks": [f"{track['name']} by {track['artists'][0]['name']}" for track in tracks]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))