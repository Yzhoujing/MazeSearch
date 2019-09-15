"""
    Enter your details below:
    
    Name:Zhoujing Yang
    Student ID:u6490332
    Email:u6490332@anu.edu.au
    """

from typing import List

from game_engine.util import raise_not_defined
from search_problems import SearchProblem
from frontiers import Stack
from search_strategies import SearchNode
def solve(problem: SearchProblem) -> List[str]:
    """See 2_implementation_notes.md for more details.
        
        Your search algorithms needs to return a list of actions that reaches the
        goal from the start state in the given problem. The elements of this list
        need to be one or more references to the attributes NORTH, SOUTH, EAST and
        WEST of the class Directions.
        """
    depth=0
    while True :
        result=dls(problem,depth)
        depth+=1
        if result!=None:
            return result
        print("current lower band is",depth)

def dls(problem,limit):
    # *** YOUR CODE HERE ***
    frontiers=Stack()
    s0 = problem.get_initial_state()
    #initiate the frontier by the start point
    #state,action,cost,parent,depth
    a=SearchNode(s0)
    frontiers.push(a)

    while not frontiers.is_empty():
        cur=frontiers.pop()
        #goal_test
        if problem.goal_test(cur.state):
            return route(cur)
        if cur.depth!=limit:
            #add frontiers
            for successor,action, cost in problem.get_successors(cur.state):
                b=SearchNode(successor,action,cur.path_cost+cost,cur,cur.depth+1)
                if valid_node(b):
                    frontiers.push(b)
def valid_node(Node):
    """
    check if the expanded node is explored, if not explored, then it is valid,return True
    <SearchNode> -> bool
    """
    node=Node
    while node.depth!=0:
        if Node.state==node.parent.state:
            return False
        node=node.parent
    return True
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
