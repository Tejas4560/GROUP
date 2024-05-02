mappings = {
    "Hello": "How may I help you?",
    "Hi": "How may I help you?",
    "How are you?": "I am good what about you?",
    "I am fine.": "Thats great! How may I help you?",
    "Recharge plans": "There are some popular combo plans:\nRs 299 ------------> Unlimited calls + 1.5gb data/day for 28 days\nRs 799 ------------> Unlimited calls + 1.5gb data/day for 84 days\nRs 399 ------------> Unlimited calls + 2.5gb data/day for 28 days\nRs 499 ------------> Unlimited calls + 3gb data/day for 28 days",
    "Data plans": "There are some popular data plans:\nRs 151 ------------> 8 gb for 28 days\nRs 108 ------------> 6 gb for 15 days\nRs 58 ------------> 3 gb for 28 days\nRs 38 ------------> 3 gb for 18 days",
    "Validity plans": "There are some plans:\nRs 99 ------------> Rs 99 talktime + 200 mb for 28 days\nRs 279 ------------> Rs 279 talktime + 500 mb for 90 days\nRs 107 ------------> Rs 107 talktime + 200 mb for 28 days\nRs 111 ------------> Rs 111 talktime + 100 mb for 31 days",
    "Yearly plan": "There are some yearly plans:\nRs 2099 ------------> Unlimited calls + 3gb data/day for 365 days\nRs 1899 ------------> Unlimited calls + 2.5gb data/day for 365 days\nRs 1799 ------------> Unlimited calls + 1.5gb data/day for 365 days",
    "Thank you": "Welcome"
}

print("Enter something to talk with chatbot")
while True:
    user_input = input("\nYou: ")
    if user_input.lower() in {"quit", "exit"}:
        print("\nChatbot: Thank you...")
        break
    elif user_input in mappings:
        print("\nChatbot:", mappings[user_input])
    else:
        print("\nChatbot: Sorry for inconvenience. I can only answer:\n- Recharge plans\n- Yearly plans\n- Data Plans\n- Validity plans")
