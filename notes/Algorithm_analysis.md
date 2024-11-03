# Intro to DSA and Algorithm Analysis

Before performing asymptotic analysis its critical to understand the basic components and how they all fit together.<br>
Components such as:
- Growth Rate
- Upper and Lower Bounds
- Time Complexity
- Resources
- Asymptotic Analysis
- Algorithms
- Data Structures

### A general definition of this topics can be as follows:

```
Asymptotic analysis is a mathematical notation used to state the upper and lower bounds of an algorithm, commonly expressed as $T(n)$. Where $T(n)$ can represent the avg growth rate that measures the increase in resource consumption as the input data size increases. Upper bound can be expressed as $T(n) \leq c\cdot f(n)$ for all values of $n \geq n_0$ where (c) constant's value doesn't matter but is always equivalent to (n).
```

![time-complexity-examples](https://github.com/user-attachments/assets/10eecc16-be0f-4c63-8463-ba0b3a29ac90)

## Some Definitions

### Data Structures:

A way of organizing and storing data in a computer such that it can be accessed and used efficiently from memory, ideally in O(1) time.

### Algorithms: 

A finite sequence of steps used to solve a problem, usually when provided an input to generate the output/solution.

### Resources: 

A resource is something finite, that is available to a computer and used by it to process informations. In DSA time and memory are resources most commonly used.

### Growth Rate: 

The metric used to mathematically represent the amount of resource consumption as the size of data increases. Thus, growth rate can be expressed as a mathematical expression or a graph.

### Asymptotic Notation: 

Formal mathematical notation used to state the upper and lower bounds of a function. Where each function $f(n)$ can be drawn on a graph and the notation represents either the upper or lower bounds of each function $f(n)$

### Upper and Lower Bounds: 

A measurement that represents an approximation where upper bound means the largest possible range of values and lower bound means the lowest possible range of values.

### Algorithms Analysis: 

A way of measuring the growth rate of an algorithm as data sizes increase.

### Big-O Notation:

An asymptotic notation that represents the upper bound of growth rate for a function $f(n)$ for any/all values of (n) representing the size of data. Formally expressed as $T(n) \leq c\cdot f(n)$ for all values of (n) and (c) where $n \geq n_0$

### Time Complexity: 

Represents the increase in time consumption as the size of data increases, normally calculated by counting the number of operations a function takes to complete as the size of data (n) is passed to it. Part of asymptotic analysis.

### Space Complexity: 

Represents the increase in memory consumption as the size of data increases, calculated by counting the amount of memory each operation of a function takes to complete as the size of data (n) is passed to it. Also part of asymptotic analysis.

## General Steps to Performing Algorithm Analysis

- Step 0: add some code
- Step 1: establish mathematical variables & functions
- Step 2: counting the operations
- Step 3: establish expression T(n)
- Step 4: simplify the expression
- Step 5: state the result (T(n) is O(something))
