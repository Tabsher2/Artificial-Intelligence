Trevor Absher
12-3-18
README

**Problem 1** For problem 1, I used an explicit policy based on movement speed. I initially started by making the car move to the right. As soon as the car starts to slip down the hill, I tell it to go left.
The car then goes up the left hill, until it starts to slip down again, when I then switch and tell it to go right. This goes back and forth until the cart has enough velocity to reach the goal. In my tests,
it only took 3 total switches, two sets of moving right, and one of moving left, receiving a consistent score of -122. I initially tried moving left first instead of right but this took longer and only got a
score of -173.

**Problem 2** For problem 2, my first attempt involved moving the cart based on its position. If it got too far to the left, move to the right, and vice versa. After a few attempts, this didn't seem to work.
I then switched it to be based off pole angle instead of cart position but it still was not quite right. Finally, I decided to test out constantly switching back and forth between directions until there was
a problem. This seemed to have much better results. I would switch actions every iteration until the pole angle got unbalanced. Whatever action made the pole go out of balance, I would do the opposite action
until the pole was back in balance, then I would switch back to alternating between actions.

I found out this strategy was behaving inconsistently after testing it a few more times. It would sometimes get good results, but not always. After testing around a little more, I kept pole angle involved in the solution
but also pulled in cart velocity. I correct the pole angle by moving towards it, provided the cart isn't moving too fast in that direction. If the cart is moving too fast in a certain direction, I change directions. After
testing this solution multiple times (and messing around finding out which values were best for angle and velocity) I was able to consistently get results over 180.

**Problem 3** To solve problem 3, I pulled a lot of data from the cart pole cross entropy solution. I used a modified reward as opposed to original as it appeared to have better results. Typically it took around
300 episodes to get a good policy that would reach the goal, with an optimal policy being learned around 500 episodes.