# 🎄 Advent of Code 2025 — Day 3: *Lobby*   
Activate batteries from each bank to form the largest possible joltage while preserving their order.

<img width="1394" height="829" alt="Screenshot 2025-12-03 205332" src="https://github.com/user-attachments/assets/bc49fc9d-8d1c-4789-aa88-5ad167035cdf" />

---

## 📌 Challenge Summary
You’re given multiple battery banks, each represented as a string of digits (1–9).  
Your task is to activate a fixed number of batteries from each bank — in order — to form the **largest possible joltage**.

---

### **Part 1**
You must choose **exactly 2 batteries** from each bank.

Your goal:  
➡️ Form the **largest 2-digit number** by selecting digits while keeping the original order.

<img width="1392" height="685" alt="Screenshot 2025-12-03 205058" src="https://github.com/user-attachments/assets/9cc53788-8c5d-4720-b85d-a19a80a9793d" />


---

### **Part 2**
You must choose **exactly 12 batteries** from each bank.

Your goal:  
➡️ Form the **largest 12-digit number** using an optimized ordered subsequence.

<img width="1388" height="688" alt="Screenshot 2025-12-03 205219" src="https://github.com/user-attachments/assets/0e2382e8-b7c3-4a5e-a8e9-1571a7b320a0" />


---

## 🧪 Sample Example & Outputs

### **Sample Input**
987654321111111
811111111111119
234234234234278
818181911112111



### **Example Results**
- From `987654321111111`  
  - Part 1 → `98`  
  - Part 2 → `987654321111`  

- From `811111111111119`  
  - Part 1 → `89`  
  - Part 2 → `811111111119`  

- From `234234234234278`  
  - Part 1 → `78`  
  - Part 2 → `434234234278`  

- From `818181911112111`  
  - Part 1 → `92`  
  - Part 2 → `888911112111`  

### **Example Sums**
- **Part 1 Sample Sum:** `357`  
- **Part 2 Sample Sum:** `3121910778619`  

---

## 🧠 Solution Outline

### ⚡ Strategy (Optimized for speed)

#### Part 1 (Linear Time)
- Track the best “tens digit” seen so far  
- Combine it with each next digit to form the largest possible 2-digit number  
- O(n) time per bank, minimal memory  

#### Part 2 (Greedy Monotonic Stack)
- Classic “maximum subsequence of length K” problem  
- Build a stack and:
  - Pop smaller digits when future digits can make a larger number  
  - Ensure enough remaining digits exist to reach 12  
- Take the first 12 digits from the resulting stack  
- O(n) per bank, highly optimized for large inputs  

---

## 🏁 Results (Based on My Actual Input)

| Part | Answer |
|------|--------|
| **1** | **17408** |
| **2** | **172740584266849** |

---
