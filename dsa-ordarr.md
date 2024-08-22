# Ordered Array [dsa-ordarr.md]

An ordered array is just what you think it is - an array that is _in order_,
meaning it remains sorted despite the operations we may apply. It takes into
account where the new element would fit in the array's order and insert at that
index, rather than at the end. As a result, it must first conduct a search to
find that particular spot in the order to add a new element to, which is the
major disadvantage of using ordered arrays.

A neat difference between regular arrays and ordered arrays is the ability to
use binary searches instead of linear searches. Unordered arrays were not able
to do so because they were not sorted yet, but here we do have pre-sorting.

Binary search is a fairly big game changer if there is a large array which
requires a search, like ever. That's because it has a time complexity of
O(logN), which grows far slower than the linear O(N). The slower growth is
because of how binary searches halve their search material each iteration, which
reduces the number of operations and iterations required.

The resulting searches upon each insert does in fact make the ordered variant
less efficient than the ordinary kind, but it makes up for it via the
aforementioned superpower of binary search.

---

## Akin
[Array](dsa-array.md)
[Searching](dsa-search.md)
