import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import openai
from config import apikey
import datetime
from googleapiclient.discovery import build

# Set up the YouTube Data API client
api_key = " Add Your Youtube API Here "  # Replace with your YouTube API key
youtube = build("youtube", "v3", developerKey=api_key)


chatStr = ""
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"You: {query}\n Jarvis: "
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=chatStr,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        # todo: Wrap this inside of a  try catch block
        say(response["choices"][0]["text"])
        chatStr += f"{response['choices'][0]['text']}\n"
        return response["choices"][0]["text"]
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def search_and_play_video(song_name):
    # Search for videos related to the song
    search_response = youtube.search().list(
        q=song_name,
        type="video",
        part="id",
        maxResults=1  # You can adjust the number of search results as needed
    ).execute()

    # Extract the video ID of the first result
    if "items" in search_response and search_response["items"]:
        video_id = search_response["items"][0]["id"]["videoId"]
        # Construct the YouTube video URL
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        try:
            say(f"Playing {song_name} Sir.")
            webbrowser.open(video_url)
        except Exception as e:
            say(f"An error occurred: {str(e)}")
    else:
        say(f"Sorry, I couldn't find any results for {song_name} on YouTube.")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing")
            query = r.recognize_google(audio, language="en-pk")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"

if __name__ == '__main__':
    print('Starting...')
    say("Hello, I am Jarvis AI")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube", "http://www.youtube.com"], ["snapchat", "https://web.snapchat.com/"], ["google", "http://www.google.com"], ["wikipedia", "http://www.wikipedia.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} Sir...")
                webbrowser.open(site[1])
        if "play music" in query:
            musicPath = r'C:\Users\"Add Your Music Path"'
            if os.path.isfile(musicPath):
                os.startfile(musicPath)
            else:
                print("The music is not found:", musicPath)


        elif "play" in query.lower() and "on youtube" in query.lower():
            song_name = query.replace("play", "").replace("on youtube", "").strip()
            print(song_name)
            search_and_play_video(song_name)

        if "the time" in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir, the time is {current_time}")
            print(current_time)

        elif "the date" in query:
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            say(f"Sir, the date is {current_date}")
            print(current_date)

        elif "the day" in query:
            current_day = datetime.datetime.now().strftime("%A")
            say(f"Sir, today is {current_day}")
            print(current_day)

######## Yha pr list bna kr ksi b applicaton ko open kia ja skta he  ##########
        elif "open face cam".lower() in query.lower():
            os.startfile("microsoft.windows.camera:")

        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "Jarvis Exit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)

        # say(query)
