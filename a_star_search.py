"""
    Enter your details below:

    Name:Zhoujing Yang
    Student ID:u6490332
    Email:u6490332@anu.edu.au
"""

from typing import Callable, List

from game_engine.util import raise_not_defined
from search_problems import SearchProblem
from frontiers import PriorityQueue
from search_strategies import SearchNode

def solve(problem: SearchProblem, heuristic: Callable) -> List[str]:
    """See 2_implementation_notes.md for more details.

    Your search algorithms needs to return a list of actions that reaches the
    goal from the start state in the given problem. The elements of this list
    need to be one or more references to the attributes NORTH, SOUTH, EAST and
    WEST of the class Directions.
    """
    # set:store the node already explored
    explored = set()
    # set:store the node wait for evaluate
    frontiers=PriorityQueue()
    #initial node
    s0 = problem.get_initial_state()
    a=SearchNode(s0)
    #initialize the dictionary to store f_cost with key "node"
    f_cost={}
    f_cost[s0]=heuristic(s0,problem)
    # import priorityqueque to record frontiers and ordered by f_cost, A* search always find the smallest f_cost in the frontiers
    frontiers.push(a,f_cost[s0])
    while not frontiers.is_empty():
        cur_key= frontiers.pop()
        #if goal then return the actions
        if problem.goal_test(cur_key.state):
            return route(cur_key)
        explored.add(cur_key.state)
        for successor,action, cost in problem.get_successors(cur_key.state):
            b=SearchNode(successor,action,cur_key.path_cost+cost,cur_key)
            #if in the explored, it means return back, so ignore it
            if successor in explored:
                continue
            f_cost[successor]=b.path_cost+heuristic(successor,problem)
            frontiers.push(b,f_cost[successor])
def route(Node):
    """
    from target node get the route from start node to it
    SearchNode -> List
    """
    node=Node
    rout=[]
    while node.parent!=None:
        rout.append(node.action)
        node=node.parent
    return rout[::-1]