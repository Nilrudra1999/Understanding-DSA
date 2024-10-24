# Intro to The Open Addressing Technique of Linear Probing

Opening addressing as a system is distinct from closed addressing because, where closed addressing allows multiple records to be stored at the same array index, open addressing doesn't allow that and opties to find the next available address given a hash_index which is occupied.

The process of finding "the next available address" comes in many forms.<br>
The simplest of which is Linear probing where, given index n, index (n+1) is checked until an open index is found.