import os
import speech_recognition as sr
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
load_dotenv()

# Securely get the API key from environment variables
API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = API_KEY

# Dictionary to map spoken currency names to their abbreviations
CURRENCY_MAP = {
    "dollars": "USD",
    "dollar": "USD",
    "euros": "EUR",
    "euro": "EUR",
    "naira": "NGN",
    "yen": "JPY",
    "dinar": "KWD",
    "pounds": "GBP",
    "pound": "GBP"
}

# Store past calculations
previous_answers = []

# Function to replace currency names with their abbreviations
def replace_currencies(text):
    words = text.split()
    processed_words = []

    for word in words:
        processed_words.append(CURRENCY_MAP.get(word.lower(), word))

    return ' '.join(processed_words)

# Function to interpret natural language queries with OpenAI
def interpret_query(query):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4"
        messages=[
            {"role": "user", "content": f"Convert this natural language math query into a mathematical expression: {query}"}
        ]
    )

    if response['choices']:
        return response['choices'][0]['message']['content'].strip()
    else:
        return None

# Function to calculate the mathematical expression
def calculate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {e}"

# Function to recognize speech and convert it to text
def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for your math query... Please speak:")
        audio = recognizer.listen(source)

        try:
            print("Recognizing your voice...")
            query = recognizer.recognize_google(audio)
            print(f"You said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I could not understand your voice.")
        except sr.RequestError as e:
            print(f"Error with Speech Recognition service: {e}")
        return None

# Function to handle user input (voice or keyboard)
def get_user_input(input_method):
    if input_method == 'voice':
        return recognize_speech()
    elif input_method == 'keyboard':
        return input("Please type your math query: ")
    else:
        print("Invalid input method selected.")
        return None

# Function to handle referencing previous answers
def process_memory_query(query):
    global previous_answers

    if "last answer" in query or "sum" in query:
        if previous_answers:
            query = query.replace("last answer", str(previous_answers[-1]))
            query = query.replace("sum", str(previous_answers[-1]))
        else:
            print("No previous answer to reference.")
            return None

    return query

# Main function to run the calculator with input selection and memory
def main():
    global previous_answers

    print("Welcome to the AI-powered calculator with memory, voice or keyboard input!")

    input_method = input("Would you like to use voice control or keyboard input? (Type 'voice' or 'keyboard'): ").strip().lower()

    while True:
        user_query = get_user_input(input_method)

        if user_query:
            processed_query = process_memory_query(user_query)
            if not processed_query:
                continue

            processed_query = replace_currencies(processed_query)

            interpreted_expression = interpret_query(processed_query)

            if interpreted_expression:
                print(f"Interpreted Expression: {interpreted_expression}")

                result = calculate_expression(interpreted_expression)
                if isinstance(result, (int, float)):
                    print(f"Result: {result}")
                    previous_answers.append(result)
                else:
                    print(result)
            else:
                print("Sorry, I couldn't interpret that expression.")
        else:
            print("No valid input received.")

# Entry point of the script
if __name__ == "__main__":
    main()
