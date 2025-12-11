# 🎄 Advent of Code 2025 — Day 11: *Reactor*  
Tracing every possible data path through a tangled network of devices.  

<img width="1417" height="824" alt="image" src="https://github.com/user-attachments/assets/1787b60e-9e19-4915-8d12-172c43ae4b1d" />


---

## 📌 Challenge Summary
You're given a directed graph of devices where data flows **forward only**.  
Your mission: analyze how many unique ways data can travel between key devices inside a reactor system.

---

### **Part 1**
You're positioned at device **`you`** and must determine how many unique paths eventually reach the main output **`out`**.

Your goal:  
Count *all* possible directed paths from **you → out**.

<img width="1420" height="768" alt="image" src="https://github.com/user-attachments/assets/93020506-f58a-4e58-8e53-5e6355a0b2b4" />

---

### **Part 2**
The Elves discovered the faulty path must include **both** critical devices:  
- `dac` (digital-to-analog converter)  
- `fft` (Fourier transform unit)

Your goal:  
Count all paths from **svr → out** that *must pass through* **both `dac` and `fft`**, in *any* order.

<img width="1421" height="681" alt="image" src="https://github.com/user-attachments/assets/dd851314-6210-46ab-bbc2-647f59fcd17e" />


---

## 🧪 Sample Example & Outputs

For the provided sample networks, valid paths include all direct graph-traversal routes that follow outbound connections only.

### **Example Results**
The sample diagrams show multiple paths between source and output, but only a subset satisfy the Part 2 condition of visiting both required nodes.

### **Example Sums**
- **Part 1 Sample Sum:** `5`  
- **Part 2 Sample Sum:** `2`  

---

## 🧠 Solution Outline

### ⚡ Strategy (Optimized for speed)
- Represent the device map as an adjacency list for **O(1)** traversal.  
- Use **DFS + memoization** to avoid recomputing paths in overlapping subgraphs.  
- For Part 2, track a compact **bitmask state** to mark whether `dac` and `fft` have been visited.  
- Time efficiency: **O(V + E)** for both parts.  
- Produces fast results even for large reactor networks.

---

## 🏁 Results (Based on My Actual Input)

| Part | Answer |
|------|--------|
| **1** | **696** |
| **2** | **473741288064360** |

---
