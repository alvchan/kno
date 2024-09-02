# Sort [dsa-sort.md]

Sorting is the operation of ordering an array, such that its elements are placed
in ascending order. There is plenty of variety in sorting algorithms, but we
will focus on the simpler sorts and progress up to Quicksort, after we've
identified the strengths and weaknesses of the other popular sorts.

Bubble Sort is part of a class of dumb, but intuitive ways to sort called
"simple sorts". It is performed by traversing an array and checking the order
between the current and the next element, then swapping if out of order. Repeat
until the array is completely sorted or a traversal from start to finish
requires no swaps. These "passthrough" traversals force each element to "bubble"
up to where they should be, hence the name.

Generally, the comparisons made will be the sum of the range [1..N-1], and swaps
may vary. Consequently, if the array starts in descending order, the # of
comparisons and swaps made will both be the above sum (S). Graphing this
relation of elements (N) vs Bubble Sort steps spits out a growth that
approximates N<sup>2</sup> steps for every element, so it has an efficiency of
O(N<sup>2</sup>). It is for this reason we avoid Bubble Sort, since quadratic
growth does not scale well and easily loses any relevant efficiency. Let's look
for a better option.

Selection Sort is a simple, but fast(er) alternative to Bubble Sort. It works by
tracking the next non-correct index and traverses to find the smallest element,
then swapping with the index from earlier. This can be performed with a nested
for loop, one to iterate the index, the other searches for the next smallest
(starting from index+1).

Since the inner loop starts later for each outer loop iteration, the total
comparisons mirror Bubble Sort's calculation. However, only one swap is made
each passthrough, resulting in only half the required steps to sort. Since
Bubble Sort takes N<sup>2</sup> steps, Selection Sort takes N<sup>2</sup>/2
steps. Technically, it would still be O(N<sup>2</sup>) - as we drop the constant
- but it's faster than Bubble, despite the equivalence of its Big O notation.
  So, things can be faster based on Big O and sometimes not, neat! But, can we
go any faster?

Even faster - to get into linear time - falls to best and average case
optimizations in Insertion Sort. Ehh, well not exactly linear, anyway. This sort
takes N<sup>2</sup> at its worst, N<sup>2</sup>/2 on an average day, and N steps
in the best case. We use the assumption of normal distribution to our advantage,
so in most cases we get Selection Sort speeds, sometimes faster, and sometimes
just as bad as Bubble.

To implement it: start at index 1, remove and place into a temporary variable,
traverse backwards, shift passed elements right, and place beside next smallest.

Analyzing Insertion's Big O leads to N-1 insertions, N-1 removals (both are done
each pass), comparisons and shifts are both N<sup>2</sup>/2. Adding leads to
N<sup>2</sup> + 2N - 2 steps, further simplification leads to O(N<sup>2</sup>
+ N), where it translates to just O(N<sup>2</sup>) due to N<sup>2</sup>'s
  significance in the polynomial. In plain English, Insertion for mostly sorted,
Selection for mostly reversed, and either in a random or unknown dataset.

---

## Akin


