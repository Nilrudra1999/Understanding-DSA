# Intro to Queues and Stacks

Both Queues and Stacks are List like Abstract Data Types, which take an underlying list Data Structure and impose either a First-in-first-out behavior or a First-in-last-out behavior. Stacks impose the FILO behavior while Queues impose the FIFO behavior, on their underlying list Data Structures. In C++ these come in the form of Class-wrappers which wrap around the vector or some other list like ADT classes, to change their behavior in a certain way. All found in the C++ 17 and up STL library.

## Queues

Queues have the FIFO behvaior, much like a line-up of people, the first to go in is the first to go out. Some of the common operations and data members of a typical Queue class include the following:

Data members:
- List of default/given size
- capacity
- size/used up space
- front
- back

Operations:
- init function (default constructor)
- various getter functions for the data members
- enqueue() wherever "front" is
- dequeue() wherever "back" is
- front() a getter function to get front's value

All of these functions must have a O(1) runtime, except when the enqueue() function resizes.<br>
Then the runtime becomes O(n).

![queues_intro](https://github.com/user-attachments/assets/099cf5ca-212f-4462-98b6-9127d4710a29)

## Stacks

Stacks have the FILO behavior, much like a stack of plates, where if a plate is on top nothing can be accessed underneath that plate until it's taken off. Some of the common operations and data members of a typical Stack class include the following:

Data members:
- List of default/given size
- capacity
- used/size

Operations:
- init function (default constructor)
- various getter functions for the data members
- push() always pushes at the top "used"
- pop() always pops at the top "used"
- top() a function that gets the top's value

All of these functions must also have a O(1) runtime, except when the push() function resizes.<br>
Then the runtime becomes O(n). Since resizing means making a new array and moving the old contents into it.

![stacks_intro](https://github.com/user-attachments/assets/cf56cad2-2bc1-44de-a41d-42e326d56ab3)
