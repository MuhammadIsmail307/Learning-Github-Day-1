# Exercise 9: Solution - Shoutouts to Everyone


# Leccture 88


# Use sapivoice in windows for shoutout voice


import win32com.client


names = ["Ismail", "Najeeb" , "Rehan"]

speaker = win32com.client.Dispatch("SAPI.SpVoice")

for name in names:
    speaker.speak(f"Shout Out to {name}")