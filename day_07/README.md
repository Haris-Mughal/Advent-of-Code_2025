# 🎄 Advent of Code 2025 — Day 7: *Laboratories*  
🧪 Tachyon beams, splitters, and quantum timelines — a strange day in the teleporter hub.

<img width="1437" height="795" alt="image" src="https://github.com/user-attachments/assets/a5e7c2a4-0b29-47c0-92e2-ab2d3cf2fc58" />

---
  
## 📌 Challenge Summary
You’re trapped inside a malfunctioning **teleporter lab**. A tachyon beam enters a manifold from the top and travels downward. The grid contains splitters `(^)` that stop the beam and **create new beams** either to the left and right.
Your job: analyze how many times beams split — and later, how many quantum timelines result.

---

### **Part 1**
A classical **tachyon manifold**.
A single beam moves downward. Whenever it hits a splitter:
- The current beam stops.
- Two new beams spawn left & right.
- Overlapping beams merge into one (they do not multiply).

Your goal:  
➡️ **Count how many total beam splits occur until all beams leave the manifold.**

<img width="1421" height="646" alt="image" src="https://github.com/user-attachments/assets/b00a98e6-e66d-4288-8af6-ef626a232d1a" />


---

### **Part 2**
The *quantum* version of the manifold.
Here, a single tachyon particle takes **both paths** each time it hits a splitter.
- Every splitter doubles the number of active timelines.
- Timelines never merge.
- A timeline ends once it moves off the grid.

Your goal:  
➡️ **Count how many distinct timelines exist after exploring every possible path.**

---

## 🧪 Sample Example & Outputs

A small example grid is provided in the puzzle showing beams splitting repeatedly.

### **Example Results**
- Beams split **21 times** in Part 1.
- Quantum branching produces **40 timelines** in Part 2.

### **Example Sums**
- **Part 1 Sample Sum:** `21`  
- **Part 2 Sample Sum:** `40`

---

## 🧠 Solution Outline

### ⚡ Strategy (Optimized for speed)
#### Part 1
- Track active beam columns using a set (to avoid duplicates).
- Move row-by-row downward.
- On encountering `^`, increment split count and add left/right beams.
- Continue until every beam exits the grid. 

#### Part 2
- Maintain a dictionary: `column → count of timelines`.
- When hitting a splitter:
    - Each **timeline duplicates** left and right.
- Sum all timelines that eventually exit the manifold.
- Efficient `O(R × C)` approach with minimal memory.

---

## 🏁 Results (Based on My Actual Input)

| Part | Answer |
|------|--------|
| **1** | **1660** |
| **2** | **305999729392659** |

---
