Trevor Absher
12-3-18
HW4 - Problem 4

Depth First Search is designed to look for the deepest node first. It will search children nodes until a node does
not have a child anymore. It is useful when the desired node is far away from the root node and deep in the tree / graph
but it is bad when this node is far to the right of the tree / graph since this strategy will completely search all the
left paths first.

Breadth First Search searches all of a nodes children before moving on to its childrens' children. It is good at finding
nodes that are very close to the root node quicker than DFS. However, if a node is deep in the tree / graph this strategy
will take a long time to find it.

Uniform Cost Search is a useful strategy when each edge has a certain weight. UCS chooses the cheapest edge to traverse
and will search for its target by going along all the cheapest edges. It is good since it will eventually find the 
best solution with a cheapest cost but it may take a long time to do so as it explores in every direction.

Dijkstras Algorithm applies a variant of UCS. It is designed with no goal state in mind, rather to find the cheapest
cost to every node in the graph / tree. This is useful for when a graph must be used multiple times and the user 
wants to find paths to multiple different nodes.

A* Search is a type of Informed Search (meaning we know where the goal state is) that expands upon UCS. It uses a 
heuristic to evaluate how close each state is to the goal along with assigning each edge a cost. 
It adds these values together to give a total value for each edge and then takes the most optimal path to the goal.

Minimax Search is an AI strategy that can be used in games when the AI actively acts against the player. The player
wants to minimize the possible loss out of a maximum loss situation (minimax). The opponent will make the move that
forces the lowest possible score from the player, and the player will choose a move that is the least bad decision
they can make in that state.

Expectimax Search is similar to Minimax, except that the AI isn't necessarily acting perfectly against the player
and some states are more based on random chance. In this strategy, the player still will choose the best action
out of the worst actions they've been forced to take. However, the difference is that the worst actions are 
calculated based on a weighted probability of what is likely to occur and what effect it would have on the player 
instead of being an active decision by the AI.

Markov Decision Process is a strategy for decision making when the outcome is based partly on decision and partly on
chance such as in Grid World. Search rewards can help persuade the agent to explore potentially dangerous states 
(that have a risk of a high penalty) while Living Rewards might persuade the agent to stay away from dangerous states. 
Discounting is another concept in MDPs that reduces the value of far away rewards, especially given the risk of 
accidentally falling into a bad state due to the random chance of movement. 

Reinforcement Learning is a strategy for teaching AI that relies on many successive runs of a certain environment. A
learning agent will attempt a certain environment and find out what states provided rewards and what states penalized. 
After each run, the agent will attempt the environment again using the data from last time to influence it to pursue 
receiving the rewards and avoiding the penalties until it has completed all the training runs and is ready to execute
on a real environment. 