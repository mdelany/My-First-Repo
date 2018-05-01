#Mood improver - ie. stress, anxiety, boredom, anger

import pyautogui as pg
import webbrowser
import time

mood = pg.confirm("How are you feeling today?", "Your Mood", ['Stressed', 'Angry', 'Bored', 'Anxious'])


if mood == "Stressed":
    answer = pg.alert(
        """
Here are a few ways to calm yourself down and stay cool in the future:
Take a quick walk or just close your eyes, give yourself a few minutes to reset.
Take deep breaths and sort out your thoughts. What ever you're facing isn't as daunting as it seems.
Plan your next steps. Any task is achievable as long as you take baby steps.
""")

elif mood == "Angry":
    answer = pg.alert(
        """
Before anything else, remove yourself from whatever situation is making you angry. It's important to get out of that type situation before any tension breaks.
Don't be violent, don't yell or scream, just walk away, you can get your anger out in a controlled environment.
If you're still fuming even after you've left the situation, take yourself somewhere private and if you need to, punch a pillow or something.
Get the frustration out without hurting anyone.
Once you've gotten the anger out, take a technical standpoint. Look at the situation from all angles. Perhaps you overreacted or were being irrational.
Think about the situation before you do anything brash. Once you've calmed, maybe you should try to make better whatever was causing such stress in the environment.
""")

elif mood == "Bored":
    answer = pg.alert(
        """
Don't succumb to the internet just yet! There are plenty of other things you might want to do.
Read a book, Make some art, Cook or bake something, Organize what's messy, Go outside, Contact friends, Finish any unfinished projects, Craft something.
""")

elif mood == "Anxious":
    answer = pg.alert(
        """
Being anxious is very similar to being stressed, here are some ways to calm yourself down:
Take a minute to reset and sort out your thoughts
Take a reality check, it's possible your anxiety is making the situation seem worse than it is. Are you being anxious for nothing?
Deeeeeeeeep breaths
Figure out what is making you anxious.
Go to your happy place. Visualizing a calming scenario in your head can calm you down and distract you from the what is triggering the anxiety.
Try standing in a superhero pose. It sounds crazy but mimicking confident, powerful body language can make you feel confident and powerful. Try to find the stance or activity makes you feel confident.

""")

