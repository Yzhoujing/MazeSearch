# Question 3: A\* Search

## _An Informed Search Algorithm_ (20 Marks)

### What We Expect You To Do

Implement the A\* search algorithm inside the `solve()` function in
[`a_star_search.py`](../a_star_search.py).

Your A\* search will use the heuristic contained in the `heuristic` argument
passed to the `solve()` function in [`a_star_search.py`](../a_star_search.py).
The heuristics take a state and return an estimate of the cost to reach the
goal from that state. The heuristics are defined in
[heuristics.py](../heuristics.py) and for the simple navigation search problem
we include three heuristics:

- The null heuristic, i.e. `h(s) = 0` for every state `s`,
- the Manhattan distance heuristic, `h(s) = |x(s) - x(G)| + |y(s) - y(G)|`,
  where `x()` and `y()` are the coordinates of the given state `s` or goal
  state `G`,
- and the Euclidean distance heuristic,
  `h(s) = sqrt( |x(s) - x(G)|^2 + |y(s) - y(G)|^2 )`.

Your implementation of A\* needs to have **all** of the following properties:

1. It implements graph search rather than tree search.
2. It returns a **valid** sequence of actions. That is, all moves are legal and
   the sequence of moves leads from the initial state to the goal.
3. The sequence of actions has the **optimal length** when using an admissible
   heuristic (such as the _Manhattan Distance_ and the _Euclidean Distance_
   heuristic)
4. It visits states in the **right** order. That is, it expands nodes with
   smaller f-values first.
5. Your implementation is not substantially slower than our solution over the
   maps `anuSearch`, `aiSearch` and `mazeSearch`.
6. When given an admissible heuristic (which is not necessarily consistent),
   your A\* search must return an optimal solution.

The times and costs of optimal solutions with our implementation on the three
maps mentioned above are:

| Problem    | Cost | Expanded Manhattan | Time w. Manhattan (secs) | Expanded Euclidean | Time w. Euclidean (secs) |
| ---------- | ---- | ------------------ | ------------------------ | ------------------ | ------------------------ |
| anuSearch  | 45   | 222                | 0.0065                   | 200                | 0.0075                   |
| aiSearch   | 26   | 59                 | 0.0019                   | 89                 | 0.0030                   |
| mazeSearch | 68   | 221                | 0.0066                   | 226                | 0.0064                   |

The times above have been averaged over several runs. The measurements were
taken using Anaconda Python 3.6.3 on a 2014 MacBook Pro (2.8 GHz Intel Core
i7). Depending on the implementation, your number of expanded nodes might
differ from the above.

You can test your implementation with the commands:

```
python3 red_bird.py -l search_layouts/anuSearch.lay -p SearchAgent -a fn=astar,heuristic=manhattan
python3 red_bird.py -l search_layouts/aiSearch.lay -p SearchAgent -a fn=astar,heuristic=manhattan
python3 red_bird.py -l search_layouts/mazeSearch.lay -p SearchAgent -a fn=astar,heuristic=manhattan
```

Alternatively, if you're using Mac or Linux, you can run these shortcuts:

```sh
./test.sh astar anuSearch manhattan
./test.sh astar aiSearch manhattan
./test.sh astar mazeSearch manhattan
```

Replace `manhattan` with `euclidean` to change the heuristic.

### Hints

1. A* **expands** first the nodes on the frontier with *minimum f-value\*.
2. In [frontiers.py](../frontiers.py) you will find a number of data structures
   readily available for you to use.
3. Be sure to avoid generating a path to the same state more than once.
4. When you need to find the heuristic value of a state, the usage of the
   heuristic will typically be of the form `heuristic_value = heuristic(state, problem)`.

### Finding Nodes on the Frontier

One thing that might surprise you when using the frontier data structures is
that in Python, a function can be the parameter of another function! For
example, this is how `find` is implemented in a queue:

```python
def find(self, f: Callable[[T], bool]) -> Optional[T]:
    """ Return some item n from the queue such that f(n) is True.
        Return None if there is no such item. Note that the parameter `f`
        is a function. This method can be slow since in the worst case, we
        need to scan through the entire queue.
    """
    for elem in self.contents:
        if f(elem):
            return elem
    return None
```

Here the parameter `f` is a function that takes an item and return either True
or False. As an example, suppose we have a bunch of fruits and vegetables in
our frontier, and we want to find the first item that contains "bananas". Here's
one way to do it:

```python
from frontiers import Stack
my_frontier = Stack()

# Push three items to the frontier. Each item is a list of words
my_frontier.push(["apples", "are", "delicious", "but", "bruise", "easily"])
my_frontier.push(["bananas", "taste", "awful", "and", "are", "bent"])
my_frontier.push(["carrots", "are", "orange", "and", "are", "not", "fruit"])

# Get the item that contains the word "bananas"
def get_bananana(fruit_info):
    return fruit_info[0] == "bananas"

item = my_frontier.find(get_bananana)
# item should now be: ["bananas", "taste", "awful", "and", "are", "bent"]

# What if I want to find "pears"?
def get_pears(fruit_info):
    return fruit_info[0] == "pears"

item = my_frontier.find(get_pears)
# item should be None
```

Finally we can save two lines of code by using lambda expressions to define
`get_bananana`. The following code is equivalent:

```python
item = my_frontier.find(lambda fruit_info: fruit_info[0] == "bananas")
```

### What to Submit

You need to include in your submission the file `a_star_search.py` with your
implementation of A\*. Please, remember to fill in your details in the comments
at the start of the file.

Once you've finished, you can move to the [next section](6_heuristics.md) or go
back to the [index](README.md).
