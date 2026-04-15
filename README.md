# 🧠 Map Coloring using Constraint Satisfaction Problem (CSP)
### 🔬 Mini Research Project | Backtracking Algorithm Analysis

🚀 This project analyzes the Map Coloring Problem using CSP and evaluates the performance of the Backtracking algorithm.

---

## 📌 Abstract
This project models the Map Coloring Problem as a Constraint Satisfaction Problem (CSP) and solves it using Backtracking. The study focuses on analyzing time complexity, space complexity, completeness, and optimality, along with comparing it to Forward Checking.

---

## 🎯 Problem Statement
Assign colors to regions such that:
- No two adjacent regions share the same color
- All constraints are satisfied

---

## 🧩 CSP Representation

- **Variables** → Regions (WA, NT, SA, Q, NSW, V, T)  
- **Domains** → {Red, Green, Blue}  
- **Constraints** → Adjacent regions cannot have same color  

---

## ⚙️ Algorithm: Backtracking

Backtracking is a recursive search algorithm that:
- Assigns colors step-by-step
- Checks constraints
- Backtracks when constraints are violated

---

## 💻 Implementation

```python
import time

graph = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

colors = ['Red', 'Green', 'Blue']
result = {}

def is_valid(region, color):
    for neighbor in graph[region]:
        if neighbor in result and result[neighbor] == color:
            return False
    return True

def backtrack():
    if len(result) == len(graph):
        return True

    for region in graph:
        if region not in result:
            for color in colors:
                if is_valid(region, color):
                    result[region] = color
                    if backtrack():
                        return True
                    del result[region]
            return False

start = time.time()

if backtrack():
    print("Solution Found:")
    for region in result:
        print(region, "→", result[region])
else:
    print("No solution exists")

end = time.time()

print("Execution Time:", end - start, "seconds")
```

⸻

📊 Output
Solution Found:
WA → Red
NT → Green
SA → Blue
Q → Red
NSW → Green
V → Red
T → Red

Execution Time: ~0.001 sec

⸻

📈 Performance Analysis

⏱ Time Complexity

O(dⁿ)
	•	d = number of colors
	•	n = number of regions

👉 Exponential growth → inefficient for large inputs

⸻

💾 Space Complexity

O(n)
	•	Stores assignments
	•	Uses recursion stack

⸻

✅ Completeness

✔ Guaranteed to find solution if it exists

⸻

❌ Optimality

✖ Does not guarantee minimum colors

⸻

⚖️ Comparison with Forward Checking
Feature         Backtracking        Forward Checking
Speed           Slow                Faster
Efficiency      Low                 High
Pruning         None                Early

⸻

📊 Complexity Growth
Regions (n)     States (3^n)
3               27
5               243
7               2187

⸻

🧠 Key Insights
	•	Backtracking explores entire search space
	•	Performance degrades exponentially
	•	Constraint pruning improves efficiency

⸻

🚀 Future Improvements
	•	Forward Checking
	•	MRV Heuristic
	•	Degree Heuristic
	•	Constraint Propagation

⸻

📄 Project Report
https://drive.google.com/file/d/1lYqyrpB7Gyf-6vAOshZeuoKIBRJRxZyZ/view?usp=sharing


