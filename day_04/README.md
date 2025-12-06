# 🎄 Advent of Code 2025 — Day 4: *Printing Department*  
Help the Elves optimize forklift access to paper rolls in a large grid, maximizing how many rolls they can remove.

<img width="1403" height="715" alt="Screenshot 2025-12-04 101353" src="https://github.com/user-attachments/assets/319b5033-92bb-4fbc-86db-47126b14203f" />

---

## 📌 Challenge Summary
- Determine which paper rolls (`@`) are accessible based on adjacent rolls.
- Simulate cascading removal where each accessible roll may open access to more rolls.

### **Part 1**
Count the number of rolls a forklift can initially access (fewer than 4 adjacent rolls).  

Your goal:  
Identify accessible rolls for immediate removal.

<img width="1403" height="735" alt="Screenshot 2025-12-04 101133" src="https://github.com/user-attachments/assets/bf102ad2-f01f-4241-9d2e-9ead2654697d" />


---

### **Part 2**
Simulate repeated removal of accessible rolls until no more rolls can be accessed.  

Your goal:  
Calculate the total rolls that can be removed through cascading forklift actions.

<img width="1428" height="643" alt="Screenshot 2025-12-04 101253" src="https://github.com/user-attachments/assets/a8f0c24b-4d13-481f-a55f-33726f945e8c" />

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
