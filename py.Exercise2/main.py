import datetime

current_hour = datetime.datetime.now().hour

if 5 <= current_hour < 12:
    print("Good Morning!")
elif 12 <= current_hour < 17:
    print("Good Afternoon!")
elif 17 <= current_hour < 22:
    print("Good Evening!")
else:
    print("Good Night!")