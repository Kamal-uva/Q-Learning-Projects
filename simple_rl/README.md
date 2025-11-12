# Simple Q-Learning Example: Start–Candy–Fire

This mini project demonstrates the basics of **Q-learning** in a tiny discrete environment with only three states and two actions.

---

## Environment Overview
- **States:** `start`, `candy`, `fire`  
- **Actions:** `left`, `right`  
- The agent starts at `start` and learns to reach `candy` (reward = +1) while avoiding `fire` (reward = –1).

---

## Key Features
- Implements a simple **Q-learning algorithm** from scratch.  
- Uses **reward shaping** (small penalties) to encourage shorter paths.  
- Prints a learned **Q-table** showing how the agent values each state–action pair.

---

## Run the Project
```bash
python simple_q_learning.py
