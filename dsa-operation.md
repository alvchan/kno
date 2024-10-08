# Basic Operations [dsa-operation.md]

Data structures always have the following 4 universal operations to interact
with its data. They are:
	1. Read - a lookup for a known index
	2. Search - find index from given element
	3. Insert - add element to the structure
	4. Delete - remove element from structure

These four tend to have differing speeds and Big O notations across varying
types of data structures. For example, an array is fast at read operations and
slow at insertions, while a linked list is slow at reads and fast at inserts.

Speed of such operations are typically measured in terms of # of steps, not real
time, since it can vary based on CPU load, hardware differences, job/input
differences, &c.

---
