import speech_recognition as sr  # For recognizing speech input
import subprocess  # For running system commands

# Function to make the system speak the given text
def say(text):
    try:
        # Use subprocess to execute the 'say' command (macOS specific)
        subprocess.run(["say", text])
    except Exception as e:
        # Handle any errors that occur while executing the command
        print(f"Error in 'say' function: {e}")

# Function to capture and recognize speech input
def takeCommand():
    r = sr.Recognizer()  # Initialize the recognizer
    try:
        with sr.Microphone() as source:  # Use the microphone as the audio source
            print("Listening...")  # Notify the user that the system is listening
            r.pause_threshold = 1  # Set a pause threshold (1 second of silence)
            audio = r.listen(source)  # Listen to the audio input
            # Recognize and convert speech to text using Google Speech Recognition API
            query = r.recognize_google(audio, language="en-us")
            print(f"You said: {query}")  # Print the recognized text
            return query  # Return the recognized text
    except sr.UnknownValueError:
        # Handle cases where the speech input could not be understood
        print("Sorry, I didn't catch that.")
        return None
    except sr.RequestError as e:
        # Handle errors related to the speech recognition service
        print(f"Recognition service error: {e}")
        return None
    except Exception as e:
        # Handle any other unexpected errors
        print(f"Unexpected error: {e}")
        return None

# Example usage of the assistant
say("Hello! I am your AI assistant. Say 'stop' to exit.")  # Greet the user
while True:
    text = takeCommand()  # Capture and recognize user input
    if text is None:
        continue  # If no valid input is recognized, retry
    if "stop" in text.lower():  # Check if the user wants to exit
        say("Goodbye!")  # Bid farewell
        break  # Exit the loop
    say(text)  # Echo back the recognized text
