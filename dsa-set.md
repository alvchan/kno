# Set [dsa-set.md]

A data structure that contains only unique elements, i.e. it prohibits duplicate
values.

Reading and searching operations are equivalent to their array counterparts, as
they are stored in memory in the exact same way and will always require N t.c.
to find a random element. This means read is of O(1) t.c. and searches are
N t.c. because the only difference between sets and arrays is an initial search
to root out duplicate insertions.

I suspect that this additional pre-search in insertions will be mildly slower in
particular cases against arrays, and thus arrays are favorable if many inserts
occur regularly. Sets are still incredibly useful if uniqueness or convenience
of use is important over the small gains arrays have via insertion times. In
other words, it is nicer than having to manually sanitize arrays before use,
especially for large datasets.

As stated before, only insertions are affected by the differences of sets, as in
a search is required before each new insert. After conducting a search for
duplicates, it will add the element if it truly is an unique element. Searches
are conducted linearly, or with binary searches if it is sorted. Alternatively,
sets are also available using hashes and trees to optimize the uniqueness and
travel time for pre-sorted data, respectively.

---

## Akin
[Array](dsa-array.md)
