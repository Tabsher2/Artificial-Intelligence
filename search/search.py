# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    
    # Create a stack for the moves and push the starting spot on
    moves = util.Stack()
    moves.push((problem.getStartState(), []))

    # Create a set for the nodes we've expanded
    expanded = set()
    
    # While we still have possible moves
    while not (moves.isEmpty()):
        # Get the best one
        state, actions = moves.pop()

        # If we've already been here, skip it
        if state in expanded:
            continue

        # If we haven't, add it
        else:
            expanded.add(state)

        # If we've reached the goal, return how we got here
        if (problem.isGoalState(state)):
            return actions

        # For all of our neighbors and the actions to get there
        # Ordered by lowest cost
        # If we haven't visited it, add it to our stack
        # Stack will pop off the highest cost first
        for neighbor, action, cost in problem.getSuccessors(state):
            if neighbor not in expanded:
                moves.push((neighbor, actions + [action]))

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    # Create a queue for the moves and push the starting spot on
    moves = util.Queue()
    moves.push((problem.getStartState(), []))

    # Create a set for the nodes we've expanded
    expanded = set()

    # While we still have possible moves
    while not (moves.isEmpty()):
        # Get the best one
        state, actions = moves.pop()

        # If we've already been here, skip it
        if state in expanded:
            continue

        # If we haven't, add it 
        else:
            expanded.add(state)

        # If we've reached the goal, return how we got here
        if (problem.isGoalState(state)):
            return actions

        # For all of our neighbors and the actions to get there
        # Ordered by lowest cost
        # If we haven't visited it, add it to our queue
        # Queue will pop off the nearest neighbor first
        for neighbor, action, cost in problem.getSuccessors(state):
            if neighbor not in expanded:
                moves.push((neighbor, actions + [action]))

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    # Create a queue for the moves and push the starting spot on
    moves = util.PriorityQueue()
    moves.push((problem.getStartState(), []), 0)

    # Create a set for the nodes we've expanded
    expanded = set()

    # While we still have possible moves
    while not (moves.isEmpty()):
        # Get the best one
        state, actions = moves.pop()
        currentCost = problem.getCostOfActions(actions)

        # If we've already been here, skip it
        if state in expanded:
            continue

        # If we haven't, add it 
        else:
            expanded.add(state)

        # If we've reached the goal, return how we got here
        if (problem.isGoalState(state)):
            return actions

        # For all of our neighbors and the actions to get there
        # Ordered by lowest cost
        # If we haven't visited it, add it to our priority queue
        # Queue will pop off the lowest cost first
        for neighbor, action, cost in problem.getSuccessors(state):
            if neighbor not in expanded:
                moves.push((neighbor, actions + [action]), cost + currentCost)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    # Create a queue for the moves and push the starting spot on
    moves = util.PriorityQueue()
    moves.push((problem.getStartState(), []), 0)

    # Create a set for the nodes we've expanded
    expanded = set()

    # While we still have possible moves
    while not (moves.isEmpty()):
        # Get the best one
        state, actions = moves.pop()
        currentCost = problem.getCostOfActions(actions)

        # If we've already been here, skip it
        if state in expanded:
            continue

        # If we haven't, add it 
        else:
            expanded.add(state)

        # If we've reached the goal, return how we got here
        if (problem.isGoalState(state)):
            return actions

        # For all of our neighbors and the actions to get there
        # Ordered by lowest cost
        # If we haven't visited it, add it to our priority queue
        # Queue will pop off the lowest cost first
        # Cost is determined by distance and the value of the heuristic
        for neighbor, action, cost in problem.getSuccessors(state):
            if neighbor not in expanded:
                moves.push((neighbor, actions + [action]), cost + currentCost
                           + heuristic(neighbor, problem))


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
