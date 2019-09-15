# minimax_agent.py
# --------------
# COMP3620/6320 Artificial Intelligence
# The Australian National University
# For full attributions, see attributions.txt on Wattle at the end of the course

"""
    Enter your details below:

    Name: Zhoujing Yang
    Student ID:u6490332
    Email:u6490332@anu.edu.au
"""

from typing import Tuple

from agents import Agent
from game_engine.actions import Directions
from search_problems import AdversarialSearchProblem
from math import *
Position = Tuple[int, int]
Positions = Tuple[Position]
State = Tuple[int, Position, Position, Positions, float, float]


class MinimaxAgent(Agent):
    """ The agent you will implement to compete with the black bird to try and
        save as many yellow birds as possible. """

    def __init__(self, max_player, depth="2"):
        """ Make a new Adversarial agent with the optional depth argument.
        """
        self.max_player = max_player
        self.depth = int(depth)

        #python3 red_bird.py -p MinimaxAgent -l adv_search_layouts/testAdversarial.lay -a depth=12 -b GreedyBlackBirdAgent -q
        #python3 red_bird.py -p MinimaxAgent -l adv_search_layouts/smallAdversarial.lay -a depth=2 -b GreedyBlackBirdAgent -q
        #python3 red_bird.py -p MinimaxAgent -l adv_search_layouts/aiAdversarial.lay -a depth=10 -b GreedyBlackBirdAgent -q
        #python3 red_bird.py -p MinimaxAgent -l adv_search_layouts/anuAdversarial.lay -a depth=8 -b GreedyBlackBirdAgent -q
        #python3 red_bird.py -p MinimaxAgent -l adv_search_layouts/mazeAdversarial.lay -a depth=10 -b GreedyBlackBirdAgent -q
        #python3 red_bird.py -p MinimaxAgent -l adv_search_layouts/smallDenseAdversarial.lay -a depth=6 -b GreedyBlackBirdAgent -q
        #python3 red_bird.py -p MinimaxAgent -l adv_search_layouts/aiDenseAdversarial.lay -a depth=6 -b GreedyBlackBirdAgent -q
        #python3 red_bird.py -p MinimaxAgent -l adv_search_layouts/anuDenseAdversarial.lay -a depth=6 -b GreedyBlackBirdAgent -q
        #python3 red_bird.py -p MinimaxAgent -l adv_search_layouts/mazeDenseAdversarial.lay -a depth=6 -b GreedyBlackBirdAgent -q
    def evaluation(self, problem: AdversarialSearchProblem, state: State) -> float:
        """
            (MinimaxAgent, AdversarialSearchProblem,
                (int, (int, int), (int, int), ((int, int)), number, number))
                    -> number
        """
        # use the average distance between red_bird with every yellow_birds to measure the score
        # the large distance  which means the ability to get bird is weak then reduce the overall score.
        player, red_pos, black_pos, yellow_birds, score, yb_score = state
        r_dis=0
        for bird in yellow_birds:
            #tuple consists of position bird and yellow bird
            red_po=(red_pos,bird)
            r_dis+=problem.distance[red_po]
            #distance between red_bird and black_bird
        b_dis=problem.distance[red_pos,black_pos]
        # prevent denominator to be 0
        if len(yellow_birds)>0:
            r_dis=r_dis/len(yellow_birds)
            #if the average distance between red bird and yellow bird is greater than the distance 
            #between red_bird with black_bird ,then deduct it from score because it has greater influence 
            if r_dis>=b_dis:
                return score-r_dis
            #the greater the distance between red_bird and black_bird is, the more risky the red_bird would be
            #so add it to score. it is to avoid face with black_bird
            return score+b_dis


    def maximize(self, problem: AdversarialSearchProblem, state: State,
                 current_depth: int, alpha=float('-inf'), beta=float('inf')) -> Tuple[float, str]:
        """ This method should return a pair (max_utility, max_action).
            The alpha and beta parameters can be ignored if you are
            implementing minimax without alpha-beta pruning.
        """
        v=float("-inf")
        #terminal test
        if problem.terminal_test(state):
            return (problem.utility(state),Directions.STOP)
        #if meet cutoff,return current evaluation
        if current_depth==self.depth:
            return (self.evaluation(problem,state),Directions.STOP)
        #call minimize function
        for successor,action, cost in problem.get_successors(state):
            new=self.minimize(problem,successor,current_depth+1,alpha,beta)
            if new > v:
                act=action
                v=new
            # alpha-beta pruning
            if v >= beta:
                alpha=max(alpha,v)
                return (v,act)
        return (v,act)
            
        
    def minimize(self, problem: AdversarialSearchProblem, state: State,
                 current_depth: int, alpha=float('-inf'), beta=float('inf')) -> float:
        """ This function should just return the minimum utility.
            The alpha and beta parameters can be ignored if you are
            implementing minimax without alpha-beta pruning.
        """
        v=float("inf")
        for successor,action, cost in problem.get_successors(state):
            new=self.maximize(problem,successor,current_depth+1,alpha,beta)[0]
            v=min(v,new)
            #alpha-beta pruning
            if v>=alpha:
                beta=max(beta,v)
                return v
        return v 
        

    def get_action(self, game_state):
        """ This method is called by the system to solicit an action from
            MinimaxAgent. It is passed in a State object.

            Like with all of the other search problems, we have abstracted
            away the details of the game state by producing a SearchProblem.
            You will use the states of this AdversarialSearchProblem to
            implement your minimax procedure. The details you need to know
            are explained at the top of this file.
        """
        # We tell the search problem what the current state is and which player
        # is the maximizing player (i.e. who's turn it is now).
        problem = AdversarialSearchProblem(game_state, self.max_player)
        state = problem.get_initial_state()
        utility, max_action = self.maximize(problem, state, 0)
        print("At Root: Utility:", utility, "Action:",
              max_action, "Expanded:", problem._expanded)
        return max_action
