# 🎄 Advent of Code 2025 — Day 5: *Cafeteria*    
Fresh or spoiled? The Elves' holiday feast depends on it!  

<img width="1433" height="797" alt="Screenshot 2025-12-05 201136" src="https://github.com/user-attachments/assets/4da433ad-bb82-47a7-94c0-cab9a5ca8ae8" />

---

## 📌 Challenge Summary
You're given a list of *fresh ingredient ID ranges* followed by a list of *available ingredient IDs*.  
Your task is to determine freshness based on inclusive ranges — which can overlap, merge, or stretch unexpectedly.

---

### **Part 1**
The available ingredient IDs are checked one by one.  
If an ID falls inside **any** fresh range, it’s considered fresh.

**Your goal:**  
Count how many available ingredient IDs are fresh.

<img width="1398" height="643" alt="Screenshot 2025-12-05 201006" src="https://github.com/user-attachments/assets/996a3975-8be6-4568-8e3e-68593a2b79f9" />


---

### **Part 2**
The list of available IDs becomes irrelevant.  
Now you're asked a more global question:  
How many *total unique ID values* exist across all the fresh ranges?

**Your goal:**  
Merge all overlapping ranges and count every number they cover.

<img width="1404" height="650" alt="Screenshot 2025-12-05 201113" src="https://github.com/user-attachments/assets/3de11f97-778e-4acb-baff-77490a8cabde" />


---

## 🧪 Sample Example & Outputs

Given ranges like:

3-5
10-14
16-20
12-18


Available IDs:

1
5
8
11
17
32



### **Example Results**
- `1` → ❌ Spoiled  
- `5` → ✅ Fresh  
- `8` → ❌ Spoiled  
- `11` → ✅ Fresh  
- `17` → ✅ Fresh  
- `32` → ❌ Spoiled  

### **Example Sums**
- **Part 1 Sample Sum:** `3`  
- **Part 2 Sample Sum:** `14`  

---

## 🧠 Solution Outline

### ⚡ Strategy (Optimized for speed)
- Parse all ranges from input.  
- **Sort + merge** overlapping/adjacent intervals for efficiency.  
- **Part 1:**  
  - Binary-search each ingredient ID inside merged ranges.  
- **Part 2:**  
  - Simply sum `(end - start + 1)` for every merged interval.  

Both solutions run efficiently even for very large input files.

---

## 🏁 Results (Based on My Actual Input)

| Part | Answer |
|------|--------|
| **1** | **744** |
| **2** | **347468726696961** |

---
