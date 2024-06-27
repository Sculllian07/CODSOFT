import pytz
import datetime
import webbrowser
import random
import threading

# Define the predefined rules and responses
def chatbot_response(user_input):
    greetings = ["hello", "hi", "hey"]
    thanks = ["thanks", "thank you"]
    jokes = ["joke", "humor", "funny"]
    time_queries = ["date and time", "current time", "what time is it"]
    videos = ["play a video", "watch a video", "show me a video", "entertainment"]
    songs = ["play a song", "listen to music", "music", "song"]
    weather = ["weather", "forecast", "temperature"]

    if any(greeting in user_input.lower() for greeting in greetings):
        return "Hey there! How can I assist you today?"

    if "how are you" in user_input.lower():
        return "I'm just a bot, but I'm here to help you with anything you need."

    if any(thank in user_input.lower() for thank in thanks):
        return "You're welcome! Feel free to ask if you need any more help."

    if any(joke_word in user_input.lower() for joke_word in jokes):
        # List of jokes
        bot_jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Parallel lines have so much in common. It’s a shame they’ll never meet.",
            "I told my wife she should embrace her mistakes. She gave me a hug.",
            "What do you get when you cross a snowman and a vampire? Frostbite.",
            "Why did the scarecrow win an award? Because he was outstanding in his field.",
            "I'm reading a book on anti-gravity. It's impossible to put down!",
            "I would tell you a joke about an elevator, but it’s an uplifting experience.",
            "Why was the math book sad? It had too many problems.",
            "Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them.",
            "Parallel lines have so much in common. It’s a shame they’ll never meet.",
            "Why don’t skeletons fight each other? They don’t have the guts.",
            "I used to play piano by ear, but now I use my hands.",
            "What’s orange and sounds like a parrot? A carrot.",
            "Why did the scarecrow become a successful neurosurgeon? He was outstanding in his field."
        ]
        # Randomly select a joke
        selected_joke = random.choice(bot_jokes)
        return selected_joke

    if any(time_query in user_input.lower() for time_query in time_queries):
        # Convert the current UTC time to IST
        utc_now = datetime.datetime.now(tz=pytz.utc)
        ist_now = utc_now.astimezone(pytz.timezone('Asia/Kolkata'))
        # Format the date and time in IST
        ist_time_str = ist_now.strftime("%Y-%m-%d %H:%M:%S %Z%z")
        return f"The current date and time in IST is: {ist_time_str}"

    if any(video_word in user_input.lower() for video_word in videos):
        # Example YouTube links for videos
        youtube_videos = [
            "https://www.youtube.com/watch?v=dQw4w9WgXcQ",  # Rickroll
            "https://www.youtube.com/watch?v=DLzxrzFCyOs",  # Cat video
            "https://www.youtube.com/watch?v=9bZkp7q19f0"   # Gangnam Style
        ]
        # Randomly select a YouTube link for videos
        video_url = random.choice(youtube_videos)
        # Open the selected YouTube link in a new tab
        threading.Thread(target=webbrowser.open_new_tab, args=(video_url,)).start()
        return "Sure, let me play a video for you!"

    if any(song_word in user_input.lower() for song_word in songs):
        # Example YouTube links for songs
        youtube_songs = [
            "https://www.youtube.com/watch?v=RgKAFK5djSk",  # See you Again - Wiz
            "https://www.youtube.com/watch?v=k85mRPqvMbE",  # Crazy Frog - Axel F
            "https://www.youtube.com/watch?v=RUuZV3iJQTs"   # Despacito - Luis Fonsi ft. Daddy Yankee
        ]

        # Randomly select a YouTube link for songs
        song_url = random.choice(youtube_songs)
        # Open the selected YouTube link in a new tab
        threading.Thread(target=webbrowser.open_new_tab, args=(song_url,)).start()
        return "Sure, let me play a song for you!"

    if any(weather_word in user_input.lower() for weather_word in weather):
        # You can integrate a weather API to fetch real-time weather information
        return "I'm sorry, I don't have access to real-time weather information at the moment."

    return "I'm not entirely sure how to respond to that. Can you please be more specific?"

# Main loop to interact with the chatbot
while True:
    user_input = input("User: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Alright, goodbye! If you need anything else, just ask.")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)