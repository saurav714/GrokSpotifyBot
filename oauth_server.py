from flask import Flask, request, redirect
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import json

load_dotenv()
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")

app = Flask(__name__)

sp_oauth = SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="user-top-read playlist-modify-public",
    cache_path=os.path.join(os.path.dirname(__file__), "spotify_cache")
)

@app.route("/login")
def login():
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route("/callback")
def callback():
    try:
        code = request.args.get("code")
        token_info = sp_oauth.get_access_token(code)
        with open(os.path.join(os.path.dirname(__file__), "user_tokens.json"), "w") as f:
            json.dump(token_info, f)
        return "Authentication successful! You can close this window."
    except Exception as e:
        return f"Authentication failed: {str(e)}"

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)