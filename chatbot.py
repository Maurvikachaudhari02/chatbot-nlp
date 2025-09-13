import nltk
from nltk.chat.util import Chat, reflections

# Pairs = pattern-response pairs
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you?", "Hi there!", "Hey! What’s up?"]
    ],
    [
        r"my name is (.*)",
        ["Nice to meet you %1!", "Hello %1, how can I assist you today?"]
    ],
    [
        r"what is your name ?",
        ["I’m a simple chatbot created with NLTK.", "You can call me ChatBot!"]
    ],
    [
        r"how are you ?",
        ["I’m doing great! How about you?", "I’m fine, thanks for asking."]
    ],
    [
        r"(.*) weather (.*)",
        ["I can’t check live weather now, but you can try Task 1 project 😉"]
    ],
    [
        r"(.*) (goodbye|bye)",
        ["Goodbye! Have a great day.", "Bye! See you soon."]
    ],
    [
        r"(.*)",
        ["I’m not sure about that. Can you rephrase?", "Interesting... tell me more!"]
    ]
]

# Chatbot setup
def chatbot():
    print("Hi, I'm ChatBot! Type 'bye' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
