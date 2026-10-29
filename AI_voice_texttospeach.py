import pyttsx3
from datetime import datetime

def speak(text):
    print("Oliver:", text)

    # Har response ke liye speech engine dobara initialize karo
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()


print("Oliver: Hello! I am your Python AI assistant. Type 'exit' to end.")

speak("Hello! I am Oliver, your Python AI assistant.")

while True:
    user_input = input("You: ").lower().strip()

    if user_input == "exit":
        speak("Goodbye Azhar! Have a nice day.")
        break

    elif "hello" in user_input or "hi" in user_input:
        speak("Hello! How can I assist you today?")

    elif "how are you" in user_input:
        speak("I am just a program, but I am functioning as expected!")

    elif "what is your name" in user_input:
        speak("I am Oliver, your Python AI assistant.")

    elif "time" in user_input:
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    elif "date" in user_input:
        current_date = datetime.now().strftime("%d-%m-%Y")
        speak(f"Today's date is {current_date}")

    elif "calculate" in user_input:
        speak("Please enter a mathematical expression.")
        expression = input("You: ").strip()

        try:
            result = eval(expression, {"__builtins__": {}}, {})
            speak(f"The result is {result}")
        except Exception:
            speak("Sorry, I could not calculate that.")

    else:
        speak("Sorry, I do not understand that command yet.")