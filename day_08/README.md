# 🎄 Advent of Code 2025 — Day 8: *Playground*    
Exploring 3D junction boxes and connecting them efficiently.  
---

## 📌 Challenge Summary
You're given a list of 3D points representing junction boxes.  
Part 1 asks for the product of the sizes of the three largest connected clusters.  
Part 2 requires finding the last pair of boxes to connect all into a single circuit and multiplying their X coordinates.  

---

### **Part 1**
Compute connected components by linking the K closest pairs of points.  

Your goal:  
Determine the sizes of the largest three components and return their product.  

---

### **Part 2**
Continue connecting closest unconnected pairs until all boxes are part of one circuit.  

Your goal:  
Find the last pair connected and return the product of their X coordinates.  

---

## 🧪 Sample Example & Outputs

Given points (sample):  

0,0,0
1,1,1
3,3,3

- Connect closest pairs
- Track component sizes
- Find last connected pair for full circuit

### **Example Results**
- Part 1 clusters: `[2, 1, 1]` → Product: `2`  
- Part 2 last connected pair: `(1, 2)` → X product: `3`  

### **Example Sums**
- **Part 1 Sample Sum:** `2`   
- **Part 2 Sample Sum:** `3` 

---

## 🧠 Solution Outline

### ⚡ Strategy (Optimized for speed)
- **Part 1:** Use a max-heap to track the K smallest pairwise distances and merge clusters using DSU (Disjoint Set Union).  
- **Part 2:** Sort all pairs by distance; iterate and union until one component remains, tracking the last pair merged.  
- Efficient use of DSU ensures fast component size updates and minimal recomputation.  

---

## 🏁 Results (Based on My Actual Input)

| Part | Answer |
|------|--------|
| **1** | **62186** | 
| **2** | **8420405530** | 

---
