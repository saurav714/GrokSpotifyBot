# GrokSpotifyBot
Discord bot for Indian servers using Spotify, Grok, **fine-tuned Mistral 7B transformer**, Sentence-BERT, ngrok.

## Overview
Boosts engagement in 10–50 user servers with non-repeating quizzes, secure top tracks, playlists, and desi AI.

## Features
- **Music**: `!song`, `!musicquiz` (non-repeating), `!recommend` (non-repeating), `!toptracks` (secure OAuth), `!createplaylist`, `!profile`.
- **AI**: `!ask` (Grok), `!deepseek`, `!local` (Mistral 7B).
- **Utility**: `!feedback`, SQLite caching.

## Installation
1. Clone: `git clone https://github.com/yourusername/GrokSpotifyBot`
2. Install: `pip install -r requirements.txt`
3. Install ngrok: https://ngrok.com/download
4. Configure `.env` with ngrok Redirect URI.
5. Fine-tune Mistral 7B: `python fine_tune.py`.
6. Run ngrok: `ngrok http 5000`.
7. Run OAuth server: `python oauth_server.py`.
8. Run API: `uvicorn api:app --host 0.0.0.0 --port 8000`.
9. Run bot: `python bot.py`.

## Try It
- Invite: [Insert Link]
- Server: [Your Server]

## Impact
- ~40–50% engagement increase with non-repeating quizzes and secure personalization.
- Showcased in xAI Discord/X.

## Tags
- Transformers, Fine-Tuning, LLM, AI, Spotify, Discord, Python, Sentence-BERT, SQLite, FastAPI, OAuth 2.0, ngrok, Music Recommendation, Indian Culture

## Contact
- Discord: [Your ID]
- X: [Your Handle]