Trevor Absher
12-3-18
README

**Problem 1** For problem 1, I used an explicit policy based on movement speed. I initially started by making the car move to the right. As soon as the car starts to slip down the hill, I tell it to go left.
The car then goes up the left hill, until it starts to slip down again, when I then switch and tell it to go right. This goes back and forth until the cart has enough velocity to reach the goal. In my tests,
it only took 3 total switches, two sets of moving right, and one of moving left, receiving a consistent score of -122. I initially tried moving left first instead of right but this took longer and only got a
score of -173.