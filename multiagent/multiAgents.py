# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        extraScore = 0
        tempScore = 0
        "*** YOUR CODE HERE ***"
        if successorGameState.isWin():
            return 100000
        
        for ghostState in newGhostStates:
            distance = manhattanDistance(ghostState.getPosition(), newPos)
            # If the ghost is far away we won't try and eat it, but we really want to if its close
            if ghostState.scaredTimer != 0 and distance < ghostState.scaredTimer:
                tempScore += (100 * 2**(1/distance))
            if ghostState.scaredTimer == 0 and distance < 2:
                tempScore-= 1000
                
        extraScore += tempScore
        # Reward eating power-up pellets if a ghost is nearby
        if ((newPos in currentGameState.getCapsules()) and (distance < 20)):
            extraScore += 100

        minDistance = float("inf")
        foodList = newFood.asList()
        for food in foodList:
            distance = manhattanDistance(food, newPos)
            if (distance < minDistance):
                minDistance = distance

        # We lose points for having food nearby that we could eat
        extraScore -= 5 * minDistance
        # There's almost no scenario we want to not be moving
        if action == "Stop":
            extraScore -= 100
        # Reward eating food
        oldFood = currentGameState.getFood()
        oldFoodList = oldFood.asList()
        if len(oldFoodList) > len(foodList):
            extraScore += 100
            
        return extraScore + successorGameState.getScore()

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        bestScore = -float("inf")
        bestAction = Directions.STOP

        # For all the moves we can make, find the maximum move out of the
        # minimum options forced upon us
        for action in gameState.getLegalActions(0):
            score = bestScore
            newState = gameState.generateSuccessor(0, action)
            bestScore = max(bestScore, self.minValue(newState, 1, 1))

            if (bestScore > score):
                bestAction = action

        return bestAction

    # Minimum Function
    def minValue(self,state, agentIndex, depth):
        # The ghosts will maximize their movements against us
        if agentIndex == state.getNumAgents():
            return self.maxValue(state, 0, depth + 1)
        score = float("inf")
        # Create a min layer for each ghost per max layer
        for action in state.getLegalActions(agentIndex):
            newState = state.generateSuccessor(agentIndex, action)
            score = min(score, self.minValue(newState, agentIndex + 1, depth))

        # If we have no options, just return the regular score
        if score != float("inf"):
            return score
        else:
            return self.evaluationFunction(state)

    # Maximum Function
    def maxValue(self,state, agentIndex, depth):
        # If we have already explored all the depths, return the score
        if depth > self.depth:
            return self.evaluationFunction(state)
        score = -float("inf")
        # Get the maximum value of all the minimum options
        for action in state.getLegalActions(agentIndex):
            newState = state.generateSuccessor(agentIndex, action)
            score = max(score, self.minValue(newState, agentIndex + 1, depth))

        # If we have no options, just return the regular score
        if score != -float("inf"):
            return score
        else:
            return self.evaluationFunction(state)
    
class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        # Same as Minimax but add in the pseudo code provided for Alpha-Beta Pruning
        bestScore = -float("inf")
        a = -float("inf")
        b = float("inf")
        bestAction = Directions.STOP

        for action in gameState.getLegalActions(0):
            newState = gameState.generateSuccessor(0, action)
            bestScore = max(bestScore, self.minValue(newState, 1, 1, a,b))

            # If our score is greater than our best option, that is our best move
            if (bestScore > a):
                bestAction = action
            # Update our best option
            a = max(bestScore, a)
        return bestAction

    # Minimum Function with pruning
    def minValue(self,state, agentIndex, depth, a, b):
        if agentIndex == state.getNumAgents():
            return self.maxValue(state, 0, depth + 1, a, b)
        score = float("inf")
        for action in state.getLegalActions(agentIndex):
            newState = state.generateSuccessor(agentIndex, action)
            score = min(score, self.minValue(newState, agentIndex + 1, depth, a, b))

            # Implement pseudo-code for Alpha-Beta Pruning
            if score < a:
                return score
            b = min(b, score)
        # If we have no options, just return the regular score
        if score != float("inf"):
            return score
        else:
            return self.evaluationFunction(state)


    def maxValue(self,state, agentIndex, depth, a, b):
        if depth > self.depth:
            return self.evaluationFunction(state)
        score = -float("inf")
        for action in state.getLegalActions(agentIndex):
            newState = state.generateSuccessor(agentIndex, action)
            score = max(score, self.minValue(newState, agentIndex + 1, depth, a, b))

            # Implement pseudo-code for Alpha-Beta Pruning 
            if score > b:
                return score
            a = max(a, score)
        # If we have no options, just return the regular score
        if score != -float("inf"):
            return score
        else:
            return self.evaluationFunction(state)

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

