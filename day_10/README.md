# 🎄 Advent of Code 2025 — Day 10: *Factory*    
Machines, buttons, and joltage counters — optimize to get them running with minimal presses.
---

## 📌 Challenge Summary
Each machine has indicator lights and buttons. Buttons toggle lights or increase joltage counters.  
- Part 1: Turn indicator lights on/off to match the diagram.  
- Part 2: Increase joltage counters to match required levels.  
Goal: Minimize total button presses for all machines.

### **Part 1**
Lights are initially off. Each button toggles specific lights.  
Your goal: Press buttons the fewest times so that all machine lights match the target diagrams.

---

### **Part 2**
Counters start at zero. Each button increases certain counters by 1.  
Your goal: Press buttons the fewest times so all counters reach their specified joltage targets.

---

## 🧪 Sample Example & Outputs

Input:
```
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
```


### **Example Results**
- Part 1: `7` button presses  
- Part 2: `33` button presses

### **Example Sums**
- **Part 1 Sample Sum:** `7`   
- **Part 2 Sample Sum:** `33` 

---

## 🧠 Solution Outline

### ⚡ Strategy (Optimized for speed)
- **Part 1:** BFS/DFS over button combinations, prune repeated or impossible states.  
- **Part 2:** Model as integer linear system; use BFS with memoization to find minimal presses.  
- **Key optimizations:**  
  - Avoid redundant computations with seen states.  
  - Prune states exceeding target counters.  
  - Explore states in increasing press order to guarantee minimal total presses by using z3.

---

## 🏁 Results (Based on My Actual Input)

| Part | Answer |
|------|--------|
| **1** | **502** | 
| **2** | **21467** | 

---
