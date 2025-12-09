# 🎄 Advent of Code 2025 — Day 9: *Rope Bridge Tiles*  
Maximizing rectangles on a red & green tile grid.  
---

## 📌 Challenge Summary
You are given a series of red tiles connected by green tiles forming a closed loop.  
Your task is to find the largest rectangle using only red and green tiles, with two red tiles at opposite corners.  

### **Part 1**
Count how many tiles are covered by the loop of red and green tiles.  

Your goal:  
Identify all red and green tiles to compute coverage.  

---

### **Part 2**
Find the largest rectangle with **red tiles at opposite corners** and only including red or green tiles.  

Your goal:  
Determine the maximum area of any rectangle that fits entirely inside the allowed tiles.  

---

## 🧪 Sample Example & Outputs

Example tiles:  

..............
.......#XXX#..
.......XXXXX..
..#XXXX#XXXX..
..XXXXXXXXXX..
..#XXXXXX#XX..
.........XXX..
.........#X#..
..............


### **Example Results**
- Largest rectangle area (Part 2): `24`  

### **Example Sums**
- **Part 1 Sample Sum:** `X`   
- **Part 2 Sample Sum:** `24`  

---

## 🧠 Solution Outline

### ⚡ Strategy (Optimized for speed)
- Store red tile coordinates.  
- Connect edges with green tiles.  
- Use **row-wise intervals** to represent allowed tiles (red + green + interior).  
- Check each pair of red tiles as opposite corners.  
- Validate rectangle coverage using intervals, avoiding massive grids.  
- Update maximum area efficiently.  

This approach handles large inputs efficiently without creating huge 2D arrays.  

---

## 🏁 Results (Based on My Actual Input)

| Part | Answer |
|------|--------|
| **1** | **4781546175** | 
| **2** | **1573359081** | 

---
