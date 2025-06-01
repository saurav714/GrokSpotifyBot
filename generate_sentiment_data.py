import pandas as pd
import os
import random

# Define sample phrases for each language and sentiment
english_phrases = {
    "sad": [
        "This song makes me feel so lonely.",
        "I miss the old vibes of this track.",
        "!recommend sad song, this one’s too depressing.",
        "The lyrics are so heartbreaking.",
        "This melody brings back sad memories."
    ],
    "happy": [
        "Love this track, it’s so uplifting!",
        "!recommend happy song, this is awesome!",
        "This beat makes me wanna dance!",
        "Such a feel-good song, amazing!",
        "This artist always brings joy."
    ],
    "neutral": [
        "This song is okay, nothing special.",
        "!recommend something like this track.",
        "It’s a decent song, I guess.",
        "Just another track in the playlist.",
        "The melody is alright."
    ]
}

bengali_phrases = {
    "sad": [
        "এই রবীন্দ্রসঙ্গীত আমাকে কাঁদায়।",
        "গানটি শুনে মন ভারী হয়ে যায়।",
        "!recommend sad song, এটা খুব দুঃখের।",
        "নাজরুল গীতি এত বিষণ্ণ কেন?",
        "এই সুর আমার হৃদয় ভাঙে।"
    ],
    "happy": [
        "এই গানটি আমার মেজাজ ঠিক করে!",
        "!recommend happy song, এটা দারুণ!",
        "নাজরুল গীতি শুনতে ভালো লাগে।",
        "এই রবীন্দ্রসঙ্গীত এত আনন্দদায়ক!",
        "গানটি শুনে মন উৎফুল্ল।"
    ],
    "neutral": [
        "গানটি ঠিক আছে, খুব একটা বিশেষ নয়।",
        "!recommend এই ধরনের গান।",
        "এটা একটা সাধারণ গান।",
        "সুরটা মোটামুটি।",
        "এই গান শুনতে পারা যায়।"
    ]
}

tamil_phrases = {
    "sad": [
        "இந்த பாடல் மிகவும் சோகமாக உள்ளது。",
        "இந்த பாடல் என் மனதை உடைக்கிறது。",
        "!recommend sad song, இது மிகவும் வருத்தமாக உள்ளது。",
        "இந்த மெலடி என்னை அழ வைக்கிறது。",
        "பாடல் வரிகள் மிகவும் கவலையாக உள்ளன。"
    ],
    "happy": [
        "இந்த பாடல் என் மனதை தொடுகிறது!",
        "!recommend happy song, இது அருமை!",
        "இந்த இசை என்னை ஆட வைக்கிறது!",
        "மிகவும் மகிழ்ச்சியான பாடல்!",
        "இந்த கலைஞர் எப்போதும் மகிழ்ச்சி அளிக்கிறார்。"
    ],
    "neutral": [
        "இந்த பாடல் சரியாக உள்ளது, சிறப்பு இல்லை。",
        "!recommend இது போன்ற பாடல்。",
        "ஒரு சாதாரண பாடல் தான்。",
        "இசை ஓகே, ஆனால் பெரிதாக இல்லை。",
        "இந்த பாடல் கேட்கலாம்。"
    ]
}

hindi_phrases = {
    "sad": [
        "यह गाना मुझे बहुत उदास करता है।",
        "इस गाने ने मेरा दिल तोड़ दिया।",
        "!recommend sad song, यह बहुत दुखद है।",
        "इस गाने की धुन बहुत दर्दनाक है।",
        "ये गीत सुनकर आँखें नम हो जाती हैं।"
    ],
    "happy": [
        "ये गाना बहुत सुंदर है!",
        "!recommend happy song, यह कमाल है!",
        "इस गाने से मूड अच्छा हो जाता है!",
        "बॉलीवुड का यह गाना शानदार है!",
        "यह गीत सुनकर मन खुश हो जाता है।"
    ],
    "neutral": [
        "यह गाना ठीक है, कुछ खास नहीं।",
        "!recommend इस तरह का गाना।",
        "यह एक औसत गाना है।",
        "गीत सुनने में ठीक लगता है।",
        "यह गाना सामान्य है।"
    ]
}

# Generate 1000 entries
data = []
languages = ["english", "bengali", "tamil", "hindi"]
sentiments = ["sad", "happy", "neutral"]
target_counts = {"sad": 333, "happy": 333, "neutral": 334}

for sentiment, count in target_counts.items():
    for _ in range(count):
        lang = random.choice(languages)
        if lang == "english":
            text = random.choice(english_phrases[sentiment])
        elif lang == "bengali":
            text = random.choice(bengali_phrases[sentiment])
        elif lang == "tamil":
            text = random.choice(tamil_phrases[sentiment])
        else:  # hindi
            text = random.choice(hindi_phrases[sentiment])
        data.append({"text": text, "label": 0 if sentiment == "sad" else 1 if sentiment == "happy" else 2})

# Shuffle data
random.shuffle(data)

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
output_path = os.path.join(os.path.dirname(__file__), "sentiment_data.csv")
df.to_csv(output_path, index=False, encoding='utf-8')
print(f"Dataset with {len(df)} entries saved to {output_path}")