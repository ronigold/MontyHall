# MontyHall
Monty Hall Problem in Python

The Monty Hall problem is named for its similarity to the Let's Make a Deal television game show hosted by Monty Hall.
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

The function runs many identical scenarios where random selection of doors occurs.

First, determine the amount of iterations you want and the number of doors at a time.

In each of the iterations, we save three results: the player's first choice result,
the result of switching his choice after being rejected by the moderator, and the result
of a new player arriving after the moderator revealed the remaining doors.

Finally we graph how many times each of the participants won the car.

When the number of iterations is large enough (n> 100), it seems that if the player
does not change his or her choice, the explanation aims for a third, if he changes his choice,
to two-thirds, and if a foreign player chooses from what is left - to 50%.
