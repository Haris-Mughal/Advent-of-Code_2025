# 🎄 Advent of Code 2025 — Day 4: *Printing Department*  
Help the Elves optimize forklift access to paper rolls in a large grid, maximizing how many rolls they can remove.
---

## 📌 Challenge Summary
- Determine which paper rolls (`@`) are accessible based on adjacent rolls.
- Simulate cascading removal where each accessible roll may open access to more rolls.

### **Part 1**
Count the number of rolls a forklift can initially access (fewer than 4 adjacent rolls).  

Your goal:  
Identify accessible rolls for immediate removal.

---

### **Part 2**
Simulate repeated removal of accessible rolls until no more rolls can be accessed.  

Your goal:  
Calculate the total rolls that can be removed through cascading forklift actions.

---

## 🧪 Sample Example & Outputs

Initial grid (10×10):

..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.


After part 1 removal:

..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.


### **Example Results**
- Part 1: 13 rolls accessible initially  
- Part 2: 43 rolls removed in total after cascading

### **Example Sums**
- **Part 1 Sample Sum:** `13`  
- **Part 2 Sample Sum:** `43`  

---

## 🧠 Solution Outline

### ⚡ Strategy (Optimized for speed)
- Precompute number of adjacent rolls for every cell.
- Use a BFS-like queue to process removable rolls.
- Remove rolls and update neighbors dynamically to find newly accessible rolls.
- Stop when no further rolls are removable.
- **Time Complexity:** O(R×C), **Space Complexity:** O(R×C)

---

## 🏁 Results (Based on My Actual Input)

| Part | Answer |
|------|--------|
| **1** | **1551** | 
| **2** | **9784** | 

---
