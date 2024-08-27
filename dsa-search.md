# Search [dsa-search.md]

Search operations are almost always invaluable resources, as they are required
to perform any kind of random access reads or to verify an element's uniqueness.
As previously mentioned, duplicate checking is one of the main jobs of a search
and optimizing this will be pivotal for ordered arrays and sets. There are two
big searches that often appear, those being linear and binary search.

Linear Search is a type of search that always works, but taking O(N) t.c. as
a consequence. It is easy to implement and is typically what many programmers
automatically default to when trying to quickly hack something together. It is
performed by simply scanning through elements of a data structure from start to
finish, and checking if any of them are the desired target element.

Binary Search is the other kind of search, but unlike linear search, works only
if the given array (or other structure) is pre-sorted. However, if this
constraint is dealt with, then the programmer gets a worst case Big O of O(logN)
t.c., which is far better in scenarios where there is a large data set or where
it may scale/grow.

Binary search requires a pre-sorted struct because its sorting mechanism is
reliant on disposing of whole ranges of invalid element by playing this game of
"higher or lower". It is quite obvious that it would be nonsensical to play this
comparison game or dispose of ranges of elements if the given struct was not
sorted. More specifically, binary search is completed by taking an upper and
lower bound where we would search + the midpoint between the two, and checking
where the target is in comparison to our midpoint. We would then move either of
our bounds and our midpoint, based on if the target was above or below the
original midpoint. This operation allows us to split our struct into halves
every iteration, allowing a 100 element array to be cornered within
7 iterations, rather than the typical 100 steps.

The logarithmic t.c. of binary search is a result of its halving nature, which
the intuitive feel for its reasoning is hard to explain, so I will instead prove
mathematically. What it really boils down to is finding 1 element by halving the
set's length (N) by 2 times the number of iterations (x). In an equation, it
would be: 1 = N/2^x, translating to x = logN/log2 = log2(N). 

Example code implementations of both are linked below, under 'Akin'.

---

## Akin

[Linear Search Ex](linear_search.py)
[Binary Search Ex](binary_search.py)
