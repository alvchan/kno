# Big O [dsa-bigo.md]

Big O is a consistent and concise way to quantify an algorithm's efficiency.
Algorithm and data structure analysis often revolve around the use of Big O due
to its easy to understand growth via mathematical curves. One could accurately
say that Big O answers the question of "How does the number of steps grow, with
respect to the data?" What it measures is often referred to as "efficiency", or
space and time complexity.

This method achieves consistency by counting the number of possible steps taken
in each possible case of the algorithm, expressed as O(N), where N is some
number of steps taken. Note that consistency here is meant as working properly,
for a variable number of elements or steps involved (think universal
quantifiers; for all x, there is a real x<sup>2</sup> for each).

We express Big O with the notation "O(f)", where f is whatever function an
algorithm's complexity may lie in. A few examples may be O(N) for linear t.c.,
O(1) for constant t.c., O(N<sup>2</sup>) for quadratic, etc.. This notation is
pronounced as "Oh of N" or "Oh of 1", depending on what type of function you
have.

In Big O, we never keep any extraneous values (such as coefficients and bases),
and we keep the function in its base form. For example, log<sub>2</sub>N of
a binary search is written simply as O(logN). We do this because we only really
care about how the function grows, with respect to other types of functions
(e.g.  linear, quadratic, factorial, etc.), i.e. in the "shape" of a graph. To
expand, we might be interested in properties such as a logarithm grows quickly
early on, but slows down and flattens out its curve (meaning it's efficient in
large quantities).

To calculate a function's Big O complexity, count the number of elements or
iterations a particular data structure or algorithm would be required to scrub
through. Remember, we want it in the form of some variable (like N), not some
number like "5 iterations". So, a single for loop typically translates into
O(N), and a nested double for loop is O(N<sup>2</sup>). If there is no iterative
component, chances are that it has constant complexity.

For constant complexity, as in O(1) cases, it really just means that it takes
one step to finish, despite the number of elements available. In other words, it
takes a constant amount of time (always one step) to complete its task.

To analyze complexity, we often refer to the list of common complexities or plot
them out to see the differing curves. Some common complexities every CS student
should be familiar with are O(N) (linear), O(N<sup>2</sup>) (quadratic), O(1)
(constant), O(N!) (factorial), O(X<sup>N</sup>) (exponential) and O(logN)
(logarithmic). They all get their names from their mathematical properties of
their curves. For example, linear is meant as linear growth, as it is a diagonal
line crawling up some constant Y for every X.

It is worth noting that complexity in Big O is measured to its "worst case",
meaning if a linear search occurs on a list of N elements, then on a bad day our
element may be the last, as in an O(N) search. It would not make sense to say
_all_ linear searches have constant t.c. because one of them found its target at
the first index.

---

## Akin
