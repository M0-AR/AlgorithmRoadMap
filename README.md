# AlgorithmRoadMap 🚀

[![NeetCode](https://img.shields.io/badge/Inspired%20by-NeetCode-blue?style=flat-square)](https://neetcode.io/)
[![Python](https://img.shields.io/badge/Language-Python-ffd43b?style=flat-square&logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

A comprehensive, curated repository for mastering Data Structures and Algorithms (DSA). Inspired by the legendary NeetCode roadmap, this project serves as a "Hero to Zero" guide for anyone looking to sharpen their technical problem-solving skills, from aspiring software engineers to seasoned professionals.

---

## 👔 Executive Summary (Business Perspective)

In the modern tech landscape, **computational efficiency** and **algorithmic thinking** are the cornerstones of high-performance engineering. This repository is more than just a collection of code; it is a testament to disciplined problem-solving and optimization.

### Why This Matters:
- **Optimization Mindset**: Every solution explores the trade-offs between Time and Space complexity, mirroring real-world resource management.
- **Scalability**: By mastering O(n) and O(log n) approaches, we ensure that our software can handle the growth from 1,000 to 1,000,000 users.
- **Standardization**: High-quality, readable Python implementations provide a blueprint for clean code and maintainable logic across engineering teams.

---

## 🛠 Technical Deep Dive

### Architectural Overview
The repository is organized into **18 specialized domains**, each targeting a core algorithmic pattern. This modularity allows for targeted learning and quick reference.

```text
.
├── 01Arrays&Hashing/      # Fundamentals of data storage and retrieval
├── 02TwoPointers/         # Efficient linear traversals
├── 03Stack/               # LIFO operations and parsing
├── 04BinarySearch/        # Logarithmic search patterns
├── 05SlidingWindow/       # Optimization in contiguous sequences
├── ...                    # And 13 more advanced categories
```

### Coding Standards
- **Complexity Analysis**: Most files include explicitly stated Time (T) and Space (S) complexities.
- **Dual-Implementation Strategy**: Where applicable, files contain both **Brute Force** and **Optimized** versions (e.g., `02TwoPointers/Medium_3Sum.py`).
- **Validated Logic**: Solutions are verified against industry-standard platforms like LeetCode.

---

## 🗺 Interactive Roadmap & Problem Inventory

Below is a detailed inventory of the problems solved, categorized by their respective domains.

| Category | Problem | Difficulty | Complexity (T/S) |
| :--- | :--- | :---: | :--- |
| **01. Arrays & Hashing** | Contains Duplicate | Easy | O(n) / O(n) |
| | Two Sum | Easy | O(n) / O(n) |
| | Valid Anagram | Easy | O(n) / O(n) |
| | Group Anagrams | Medium | O(m*n) / O(m*n) |
| | Product of Array Except Self | Medium | O(n) / O(1)* |
| | Top K Frequent Elements | Medium | O(n) / O(n) |
| **02. Two Pointers** | Valid Palindrome | Easy | O(n) / O(1) |
| | 3Sum | Medium | O(n²) / O(1) |
| | Two Sum II | Medium | O(n) / O(1) |
| **03. Stack** | Valid Parentheses | Easy | O(n) / O(n) |
| | Evaluate Reverse Polish Notation | Medium | O(n) / O(n) |
| | Generate Parentheses | Medium | O(2ⁿ) / O(n) |
| | Min Stack | Medium | O(1) / O(n) |
| **04. Binary Search** | Binary Search | Easy | O(log n) / O(1) |
| | Search a 2D Matrix | Medium | O(log m*n) / O(1) |
| **05. Sliding Window** | Best Time to Buy & Sell Stock | Easy | O(n) / O(1) |
| | Longest Substring Without Repeating | Medium | O(n) / O(n) |
| **06. Linked List** | Merge Two Sorted Lists | Easy | O(n+m) / O(1) |
| | Reverse Linked List | Easy | O(n) / O(1) |
| **07. Trees** | Balanced Binary Tree | Easy | O(n) / O(h) |
| | Diameter of Binary Tree | Easy | O(n) / O(h) |
| | Invert Binary Tree | Easy | O(n) / O(h) |
| | Maximum Depth of Binary Tree | Easy | O(n) / O(h) |
| **08. Tries** | Implement Prefix Tree | Medium | O(n) / O(n) |
| **09. Heap** | Kth Largest Element in Stream | Easy | O(log k) / O(k) |
| **10. Backtracking** | Combination Sum | Medium | O(2ᵗ/ᵐ) / O(t/m) |
| | Permutations | Medium | O(n!) / O(n!) |
| | Subsets | Medium | O(n*2ⁿ) / O(n) |
| **11. Intervals** | Insert Interval | Medium | O(n) / O(n) |
| | Merge Intervals | Medium | O(n log n) / O(n) |
| **12. Greedy** | Maximum Subarray | Easy | O(n) / O(1) |
| | Jump Game | Medium | O(n) / O(1) |
| **13. Graphs** | Number of Islands | Medium | O(n*m) / O(n*m) |
| **14. Adv. Graphs** | Reconstruct Itinerary | Hard | O(v²) / O(n) |
| **15. 1D DP** | Climbing Stairs | Easy | O(n) / O(1) |
| **16. 2D DP** | Unique Paths | Medium | O(n*m) / O(n) |
| **17. Bit Manipulation** | Single Number | Easy | O(n) / O(1) |
| **18. Math & Geo** | Rotate Image | Medium | O(n²) / O(1) |

*\*Complexity notes: O(1) space excludes the output array where applicable.*

---

## 🚀 How to Use This Repository

### Prerequisites
- Python 3.8+

### Running a Solution
Simply navigate to the directory and run the script using Python:
```bash
python3 "01Arrays&Hashing/Easy_TwoSum.py"
```

### Learning Strategy
1. **Understand the Problem**: Read the filename and the initial comments.
2. **Analyze the Brute Force**: Understand why a naive approach might fail in production.
3. **Study the Optimized Path**: Deep dive into the logic that reduces complexity.
4. **Reproduce**: Try to implement the solution without looking at the code.

---

## 📈 Philosophy: From Zero to Hero
This repository embodies the growth mindset. We start with fundamental **Arrays & Hashing**, building the intuition needed to tackle complex **Dynamic Programming** and **Advanced Graph** problems. It is a journey of continuous improvement, where we learn that there is no "perfect" code, only better trade-offs.

---
*Inspired by NeetCode. Crafted with passion for engineering excellence.*
