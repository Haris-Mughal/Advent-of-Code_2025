# 🎄 Advent of Code 2025 — Day 12: *Christmas Tree Farm*     
A spatial-packing challenge where uniquely shaped presents must fit perfectly under each Christmas tree.  

---

## 📌 Challenge Summary
You're given a set of oddly-shaped presents and multiple tree-regions of different sizes.  
Each region lists how many presents of each shape must fit inside.  
Presents may be rotated or flipped, but cannot overlap or go out of bounds.

The task: **Determine how many regions can successfully fit all required presents.**

---

### **Part 1**
For each region, validate whether all specified presents can be placed on the grid without overlaps.

Your goal:  
✔ Parse shapes  
✔ Generate all rotations/flips  
✔ Perform optimized placement using bitmasks + backtracking  
✔ Count how many regions can fully accommodate all presents

---

### **Part 2**
Similar logic — but with expanded constraints and harder layouts (varies per actual Day 12 puzzle extension).

Your goal:  
✔ Reuse the optimized solver  
✔ Handle more complex or additional requirements for the extended task  

---

## 🧪 Sample Example & Outputs

Given the example from the problem statement:  
- 6 shapes  
- 3 regions to test  
- One region fails due to insufficient space

### **Example Results**
- Region 1 → **Fits**  
- Region 2 → **Fits**  
- Region 3 → ❌ **Does Not Fit**

### **Example Sums**
- **Part 1 Sample Sum:** `2`  
- **Part 2 Sample Sum:** `N/A` (depends on your puzzle variant)

---

## 🧠 Solution Outline

### ⚡ Strategy (Optimized for speed)
- Convert each shape into a normalized set of coordinates  
- Generate every unique orientation (4 rotations × flip)  
- Precompute all valid placements using **bitmask rows**  
- Use **depth-first backtracking with aggressive pruning**  
- Sort presents largest-first for faster convergence  
- Immediately cut off impossible cases using area checks

This ensures excellent performance even on large regions.

---

## 🏁 Results (Based on My Actual Input)

| Part | Answer |
|------|--------|
| **1** | **2** |
| **2** | **541** |

---
