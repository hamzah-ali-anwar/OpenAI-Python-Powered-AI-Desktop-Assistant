import speech_recognition as sr  # For speech recognition
import subprocess  # For executing system commands
import webbrowser  # For opening web pages

# Function to make the system speak the given text
def say(text):
    try:
        # Use subprocess to run the 'say' command (macOS-specific) for text-to-speech
        subprocess.run(["say", text])
    except Exception as e:
        # Handle any exceptions that occur while running the 'say' command
        print(f"Error in 'say' function: {e}")

# Function to capture and recognize speech input from the microphone
def takeCommand():
    r = sr.Recognizer()  # Initialize the recognizer
    try:
        with sr.Microphone() as source:  # Use the microphone as the audio input source
            print("Listening...")  # Notify the user that the assistant is listening
            r.pause_threshold = 1  # Set a pause threshold (1 second of silence)
            audio = r.listen(source)  # Capture audio from the microphone
            # Convert speech to text using Google Speech Recognition API
            query = r.recognize_google(audio, language="en-us")
            print(f"You said: {query}")  # Output the recognized text
            return query  # Return the recognized text
    except sr.UnknownValueError:
        # Handle cases where speech is not understood
        print("Sorry, I didn't catch that.")
        return None
    except sr.RequestError as e:
        # Handle errors from the recognition service
        print(f"Recognition service error: {e}")
        return None
    except Exception as e:
        # Handle any other unexpected errors
        print(f"Unexpected error: {e}")
        return None

# Start of the assistant's main logic
say("Hello! I am your AI assistant. Say 'stop' to exit.")  # Greet the user

while True:
    text = takeCommand()  # Capture and recognize user input
    if text is None:
        continue  # If no valid input is captured, retry

    # Check if the user wants to exit the program
    if "stop" in text.lower():
        say("Goodbye!")  # Bid farewell
        break  # Exit the loop

    # Check for commands to open specific websites
    sites = [
        ["youtube", "https://www.youtube.com"],
        ["wikipedia", "https://www.wikipedia.org"],
        ["google", "https://www.google.com"],
        ["linkedin", "https://www.linkedin.com/feed/"]
    ]
    for site in sites:
        # If the command matches a website name, open it
        if f"open {site[0]}" in text.lower():
            say(f"Opening {site[0]}")  # Notify the user
            webbrowser.open(site[1])  # Open the website in the default browser

    # Check for a command to open a specific video file
    if "open video" in text.lower():
        videoPath = ""  # Replace with the absolute path to your video file
        try:
            subprocess.call(["open", videoPath])  # Open the video file (macOS-specific)
            say("Opening video.")  # Notify the user
        except Exception as e:
            # Handle errors while trying to open the video
            say("Sorry, I couldn't open the video.")
            print(f"Error opening video: {e}")

    # Echo back the recognized text as a response
    say(text)
