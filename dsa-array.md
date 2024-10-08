# Array [dsa-array.md]

The most basic structure available in computer science, serving as a container
or list of N elements placed side-by-side (contiguously). They are often of
a uniform type (homogenous) to make length calculations easier due to the
singular typing of elements.

Elements in an array are accessed via an "index" that identifies where some data
lives relative to the start of an array. It is worth noting that the index
number starts at 0 (zero-indexing) which reflects how computers access indices
of an array, that is via pointer arithmetic or "offsets" (addr. of array + index
is the precise address of the element itself).

As a result of having index-based reading, reads are of constant time complexity
(1 t.c.) and are often very fast (due to hardware native arithmetic operations).
Conversely, searching is a slow operation that requires walking/iterating
through to check every element in a linear search (N t.c.), or a binary search
(logN t.c.) if given a sorted array.

Inserting additional elements is also a tricky business when dealing with
arrays. Often times, arrays are made to be oversized (and later properly
resized) or dynamically resized as demand for more space arrives. This leads to
wasted space from overusing memory and/or wasted compute time from repeated
resize operations. Additionally, insertion in the middle of the array requires
N t.c. to shuffle over enough spaces to fit the new elements, where N is the
number of elements from the desired index to the end.

Deletion suffers from the same problems as insertions, just as inserting
requires dynamic resizing to grow, we need it here to dynamically shrink or risk
keeping a lot of unused space in our array.

What the above dynamic allocation and resizing is doing at essence is finding
new space to contain its new size and reallocs itself in its entirety (aka
copies every element). So, if an array with length N is resized to N+1, N+1
space in memory is searched for and N elements are copied from the original to
the new slot (roughly N t.c.).

Arrays tend to get use when it does not need to resize often, or at all, and is
quite favorable when read/access operations are littered all over.

---

## Akin

[Basic Operations](dsa-operation.md)
