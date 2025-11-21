
# Genetic Algorithm for Solving the 0-1 Knapsack Problem

## 🧬 What is a Genetic Algorithm?

A **Genetic Algorithm (GA)** is a powerful search and optimization technique inspired by the process of **natural selection** and **evolution** in biology. GAs are particularly useful for solving **complex problems** where traditional algorithms struggle due to the size of the solution space or non-linearity of constraints.

Genetic Algorithms simulate the survival of the fittest by evolving a population of solutions over time. The main components of a GA include:

- **Chromosomes**: Representations of potential solutions (e.g., bit strings).
- **Fitness Function**: Evaluates how "good" a solution is.
- **Selection**: Chooses which chromosomes will reproduce.
- **Crossover**: Combines parts of two chromosomes to create new offspring.
- **Mutation**: Randomly changes some genes in a chromosome to maintain diversity.
- **Evolution Loop**: Repeats the selection-crossover-mutation cycle over many generations.

---

## 🎯 Selection Methods in Genetic Algorithms

### 1. **Elitism**

**Elitism** is a selection strategy that ensures the **best-performing chromosomes** from the current generation are **directly carried forward** to the next generation.

#### 🔹 How Chromosomes Are Selected in Elitism:
- Evaluate the fitness of all chromosomes in the population.
- Select the **top N chromosomes** (usually 1 or 2) with the **highest fitness scores**.
- These elite chromosomes are preserved without any change and guaranteed to be included in the next generation.
- This guarantees that the quality of solutions **never degrades** from one generation to the next.

Elitism is often used in combination with other selection methods to ensure that the best solutions are not lost during crossover or mutation.

---

### 2. **Roulette Wheel Selection**

Also known as **fitness proportionate selection**, Roulette Wheel Selection is a **probabilistic method** where the probability of selecting a chromosome is **proportional to its fitness**.

#### 🔹 How Chromosomes Are Selected in Roulette Wheel:
- Calculate the **total fitness** of the population.
- Compute the **fitness ratio** of each chromosome (i.e., individual fitness divided by total fitness).
- Create a **cumulative probability distribution** (like a roulette wheel).
- Spin the "wheel" (generate a random number between 0 and 1).
- The chromosome whose segment contains the random number is selected.
- Repeat until the required number of chromosomes is selected.

This method gives **all chromosomes a chance to be selected**, but higher fitness chromosomes have a **higher probability**, balancing **exploration** and **exploitation** of the search space.

---

## 🎒 What is the 0-1 Knapsack Problem?

The **0-1 Knapsack Problem** is a classic problem in computer science and combinatorial optimization. The objective is to **maximize the total value** of selected items that fit within a **given weight capacity**.

### Problem Definition:
- You have a set of `n` items.
- Each item has:
  - A **value** (how useful or profitable it is),
  - A **weight** (how much space or load it takes).
- You have a **knapsack** that can carry a limited weight `W`.

The goal is to **select a subset of items** such that:
- The **total weight** does **not exceed** `W`.
- The **total value** is **maximized**.

In the **0-1** version, each item can either be **included (1)** or **excluded (0)** — you **cannot take a fraction** of an item.

---

## 🤖 How Genetic Algorithm Helps Solve the 0-1 Knapsack Problem

Traditional methods like brute-force search become impractical when the number of items grows large, as the number of possible combinations is \(2^n\). Genetic Algorithms provide a **more efficient, probabilistic approach** to finding **near-optimal solutions**.

### Genetic Algorithm Approach:
1. **Chromosome Representation**: Each chromosome is a binary string of length `n`, where `1` means the item is included and `0` means excluded.
2. **Fitness Function**: Calculates the **total value** of selected items. If the total weight exceeds the knapsack's capacity, the solution is either penalized or rejected.
3. **Initial Population**: Randomly generated solutions that respect the weight constraint.
4. **Selection**: Either Elitism or Roulette Wheel selection is used to choose parents for reproduction.
5. **Crossover**: Combines two parent chromosomes to create new offspring (e.g., by splitting and swapping halves).
6. **Mutation**: Randomly flips bits in the chromosome to introduce variability and avoid local optima.
7. **Evolution Loop**: Over many generations, the algorithm converges toward high-fitness solutions.

### Why Use GA for Knapsack?
- Efficiently searches a large space of possible solutions.
- Can be tuned to trade off between speed and accuracy.
- Can handle variations of the knapsack problem (e.g., multiple constraints, multi-objective).

---

## 📁 Files Overview

- `GeneticAlgorithm_Elitism.py`: Core implementation of the genetic algorithm with elitism and crossover/mutation logic.
- `GeneticAlgorithm_RouletteWheel.py`: Core implementation of the genetic algorithm with elitism and crossover/mutation logic.
- `test case for 0-1 knapsack problem.txt`: Input file defining the items and knapsack capacity.

---

## 🏁 How to Run

1. Create an input file in the following format:
    ```
    <number_of_items> <max_weight>
    <value1> <weight1>
    <value2> <weight2>
    ...
    ```

2. Run the main Python script:
    ```bash
    python GeneticAlgorithm_Elitism.py or GeneticAlgorithm_RouletteWheel.py
    ```

3. Output will display the fitness and weight of all chromosomes in the final population, and highlight the best solution found.

---

## ✅ Example Output

```
310 45
280 42
300 40
...

Best solution found:
Item worth 100 and weight 20
Item worth 150 and weight 10
Item worth 60 and weight 5

Fitness of best solution: 310
Weight of best solution: 35
```

---

## 📌 Final Notes

- Both **elitism** and **roulette-wheel selection** have their strengths. You can switch between them depending on the problem scale and your experimentation needs.
- The code is easily extensible to support different crossover methods and constraints.
