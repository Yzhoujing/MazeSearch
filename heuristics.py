# heuristics.py
# ----------------
# COMP3620/6320 Artificial Intelligence
# The Australian National University
# For full attributions, see attributions.txt on Wattle at the end of the course

"""
    Enter your details below:
    
    Name:Zhoujing Yang
    Student ID:u6490332
    Email:u6490332@anu.edu.au
"""
""" This class contains heuristics which are used for the search procedures that
    you write in search_strategies.py.

    The first part of the file contains heuristics to be used with the algorithms
    that you will write in search_strategies.py.

    In the second part you will write a heuristic for Q4 to be used with a
    MultiplePositionSearchProblem.
"""

from typing import Tuple

from search_problems import (MultiplePositionSearchProblem,
                             PositionSearchProblem)
from frontiers import PriorityQueue




Position = Tuple[int, int]
YellowBirds = Tuple[Position]
State = Tuple[Position, YellowBirds]

# -------------------------------------------------------------------------------
# A set of heuristics which are used with a PositionSearchProblem
# You do not need to modify any of these.
# -------------------------------------------------------------------------------


def null_heuristic(pos: Position, problem: PositionSearchProblem) -> int:
    """The null heuristic. It is fast but uninformative. It always returns 0"""

    return 0


def manhattan_heuristic(pos: Position, problem: PositionSearchProblem) -> int:
    """The Manhattan distance heuristic for a PositionSearchProblem."""

    return abs(pos[0] - problem.goal_pos[0]) + abs(pos[1] - problem.goal_pos[1])


def euclidean_heuristic(pos: Position, problem: PositionSearchProblem) -> float:
    """The Euclidean distance heuristic for a PositionSearchProblem"""

    return ((pos[0] - problem.goal_pos[0]) ** 2 + (pos[1] - problem.goal_pos[1]) ** 2) ** 0.5


# Abbreviations
null = null_heuristic
manhattan = manhattan_heuristic
euclidean = euclidean_heuristic

# -------------------------------------------------------------------------------
# You have to implement the following heuristics for Q4 of the assignment.
# It is used with a MultiplePositionSearchProblem
# -------------------------------------------------------------------------------

# You can make helper functions here, if you need them


def bird_counting_heuristic(state: State,
                            problem: MultiplePositionSearchProblem) -> float:
    """
<state,problem>  ->  float
"""
    position, yellow_birds = state
    heuristic_value = 0
    heuristic_value=len(yellow_birds)
    return heuristic_value


bch = bird_counting_heuristic


def every_bird_heuristic(state: State,
                         problem: MultiplePositionSearchProblem) -> float:
    """
<state,problem>  ->  float
"""
    position, yellow_birds = state
    heuristic_value = 0
    #dictionary of all the distance of any two points in the map
    dis=problem.distance
    #convert tuple to list，then we can remove bird after making a move
    yellow_bird_list=list(yellow_birds)
    bird_box=PriorityQueue()
    #add all the distances of birds in the priority queue and each time pop up the bird with minimum value
    while len(yellow_bird_list)!=0:
        for pos in yellow_bird_list:
            new_pos=(position,pos)
            if new_pos in dis.keys():
                bird_box.push(new_pos,dis[new_pos])
        pos=bird_box.pop()
        # increase the heuristic value
        heuristic_value+=dis[pos]
        position=pos[1]
        if position in yellow_bird_list:
            yellow_bird_list.remove(position)
    return heuristic_value


every_bird = every_bird_heuristic
