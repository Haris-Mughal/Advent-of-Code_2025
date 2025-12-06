# 🎄 Advent of Code 2025 — Day 6: *Trash Compactor*  
Cephalopod-style math… but written in the weirdest possible layout.  

<img width="1405" height="790" alt="image" src="https://github.com/user-attachments/assets/ca074e85-ba6c-4201-a857-4207df4774fe" />


---
  
## 📌 Challenge Summary
You're given a horizontal worksheet where each **problem is arranged vertically**, numbers stacked on top of each other, and the **operator at the bottom**.  
Problems are separated by a **blank column**.  
Part 2 flips everything: numbers must be read **column-wise**, top → bottom, right → left.

---

### **Part 1**
The worksheet arranges each problem vertically.  
Each problem contains:
- Several numbers (top → bottom)  
- A single operator (`+` or `*`) at the bottom  
- Problems separated by a full blank column  

Your goal:  
➡️ **Extract each problem, perform the operation, and sum all problem results.**

<img width="1412" height="675" alt="image" src="https://github.com/user-attachments/assets/a1acd055-0656-4af3-a327-c588c63a2028" />


---

### **Part 2**
The cephalopods reveal the twist — their math is read **right-to-left**, and each number is given **one digit per row, aligned in its own column**.

Each problem block now:
- Contains multiple **columns**, each representing **one number**  
- Operator still in the bottom row  
- Numbers formed by reading **top → bottom** within each column  

Your goal:  
➡️ **Build numbers column-wise, compute each problem, and sum all answers.**

<img width="1412" height="675" alt="image" src="https://github.com/user-attachments/assets/371debee-977f-4e3d-aa32-909af1a35126" />

---

## 🧪 Sample Example & Outputs

Using the sample worksheet provided in the puzzle, the problems resolve into different expressions depending on the part.

### **Example Results**
- Part 1: Typical vertical math  
- Part 2: Cephalopod column-math  

### **Example Sums**
- **Part 1 Sample Sum:** `4277556`  
- **Part 2 Sample Sum:** `3263827`

---

## 🧠 Solution Outline

### ⚡ Strategy (Optimized for speed)
- Read the worksheet into a uniform grid  
- Scan **column by column** to detect problem blocks  
- For each block:
  - **Part 1:** Build numbers row-wise  
  - **Part 2:** Build numbers column-wise  
- Detect operator from bottom row  
- Use `sum()` or `math.prod()` for fast operations  
- Accumulate grand total in a single pass → **O(R × C)** time  

---

## 🏁 Results (Based on My Actual Input)

| Part | Answer |
|------|--------|
| **1** | **5335495999141** |
| **2** | **10142723156431** |

---
