import speech_recognition as sr  # Library for speech recognition
import subprocess  # Library to run system commands

# Function to convert text to speech using the 'say' command (macOS-specific)
def say(text):
    # Subprocess is a safer alternative to os.system for running shell commands.
    # It avoids issues with special characters and offers better security and functionality.
    subprocess.run(["say", text])  # Execute the 'say' command with the provided text

# Function to listen to audio input from the microphone and convert it to text
def listen():
    recognizer = sr.Recognizer()  # Create an instance of the Recognizer class
    with sr.Microphone() as source:  # Use the microphone as the audio input source
        print("Listening...")  # Notify the user that the system is listening
        try:
            # Capture audio from the microphone with a timeout to prevent indefinite waiting
            audio = recognizer.listen(source, timeout=5)
        except sr.WaitTimeoutError:
            # Handle cases where no audio is received within the timeout period
            return "I didn't hear anything. Please try again."
    try:
        # Use Google Speech Recognition API to convert the captured audio to text
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        # Handle cases where the speech was not understood
        return "Sorry, I didn't catch that."
    except sr.RequestError:
        # Handle cases where the recognition service is unavailable or returns an error
        return "Error with the recognition service."

# Example usage of the functions
say("Hello! What is your name?")  # Use the 'say' function to greet the user
name = listen()  # Capture and recognize the user's response
say(f"Nice to meet you, {name}!")  # Use the 'say' function to respond to the user
