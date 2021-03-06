""""The Monty Hall problem is named for its similarity to the Let's Make a Deal television game show hosted by Monty Hall.
The problem is stated as follows. Assume that a room is equipped with three doors. Behind two are goats, and behind the
third is a shiny new car. You are asked to pick a door, and will win whatever is behind it. Let's say you pick door 1.
Before the door is opened, however, someone who knows what's behind the doors (Monty Hall) opens one of the other two doors,
revealing a goat, and asks you if you wish to change your selection to the third door (i.e., the door which neither you
picked nor he opened). The Monty Hall problem is deciding whether you do.

The correct answer is that you do want to switch. If you do not switch, you have the expected 1/3 chance of winning
the car, since no matter whether you initially picked the correct door, Monty will show you a door with a goat.
But after Monty has eliminated one of the doors for you, you obviously do not improve your chances of winning to better
than 1/3 by sticking with your original choice. If you now switch doors, however, there is a 2/3 chance you will win the
car (counterintuitive though it seems).
http://mathworld.wolfram.com/MontyHallProblem.html """


""""roni goldsmid IL --- github.com/ronigold"""

"""The Monty Hall problem"""

import pandas as pd
import random
import seaborn as sns

"""enter the number of doors and experiments"""
amount_of_doors = 1
amount_of_experiments = 100

"""an experiment on the Monty Hall problem many times to test the probabilities"""

def montyhall():
    # Initializes DF to save the results
    res = pd.DataFrame(columns=('original player choice', 'new player choice', 'another player choice'))

    # Montyhall loop:
    for i in range(amount_of_experiments):

        # Initializes a list wish amount_of_doors:
        doors = list(range(0, amount_of_doors + 1))
        car = random.choice(doors)

        # the first player choice:
        original_player_choice = random.choice(doors)

        # Removing all elements from the game except the player's choice and another one:
        while len(doors) > 2:
            ran = random.choice(doors)
            doors.remove(ran) if ran != car and ran != original_player_choice else None

        # Now, there are only two options. A foreign player approaches and chooses one of them:
        another_player_choice = random.choice(doors)

        # Finally, we will look at a case where the actor changes his choice:
        doors.remove(original_player_choice)
        new_player_choice = doors[0]

        # Check which of the players guessed correctly:
        original_player = True if original_player_choice == car else False
        new_player = True if new_player_choice == car else False
        another_player = True if another_player_choice == car else False

        # Save the result to the df:
        res.loc[i] = [original_player, new_player, another_player]

    return res


res = montyhall()
res.mean()
sns.barplot(data=res)
