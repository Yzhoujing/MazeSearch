"""
    Enter your details below:
    
    Name:Zhoujing Yang
    Student ID:u6490332
    Email:u6490332@anu.edu.au
"""

from typing import List

from game_engine.util import raise_not_defined
from search_problems import SearchProblem
from frontiers import Queue
from search_strategies import SearchNode
def solve(problem: SearchProblem) -> List[str]:
    """See 2_implementation_notes.md for more details.
        
        Your search algorithms needs to return a list of actions that reaches the
        goal from the start state in the given problem. The elements of this list
        need to be one or more references to the attributes NORTH, SOUTH, EAST and
        WEST of the class Directions.
        
        (problem: SearchProblem) -> List[str]
        """
    #get the initial postion and set frontiers
    s0 = problem.get_initial_state()
    frontiers=Queue()
    explored=set()
    #initiate the frontier by the start point
    a=SearchNode(s0)
    frontiers.push(a)
    #expand the frontiers
    while not frontiers.is_empty():
        #our goal is to
        cur=frontiers.pop()
        if problem.goal_test(cur.state):
            route=[]
            while cur.parent!=None:
                route.append(cur.action)
                cur=cur.parent
            return route[::-1]
        else:
            explored.add(cur.state)
            for successor,action, cost in problem.get_successors(cur.state):
                b=SearchNode(successor,action,cur.path_cost+cost,cur)
                if successor not in explored:
                    frontiers.push(b)



