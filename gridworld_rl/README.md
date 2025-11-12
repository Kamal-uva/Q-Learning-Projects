
---

## **gridworld_rl/README.md**
```markdown
# Gridworld Q-Learning Project

This project implements **Q-learning** in a 4×4 gridworld where an agent learns to navigate from the start (top-left) to the goal (bottom-right).

---

## Environment Overview
- **Grid Size:** 4×4 (16 states)
- **Actions:** Up, Right, Down, Left  
- **Start State:** Top-left corner (0)  
- **Goal State:** Bottom-right corner (15)

---

## Key Features
- Implements **epsilon-greedy exploration** and **discounted rewards**.  
- Learns an **optimal policy** mapping each grid cell to the best action.  
- Displays the learned **policy grid** and **path from start to goal**.  
- Optional **visualization** animates the agent’s movement in the terminal.

---

## Run the Project
```bash
python gridworld_q_learning.py

---

## Example Output
Optimal Policy Grid:
→ → ↓ ↓
↑ → ↓ ↓
↑ → ↓ ↓
↑ → ↓ G

Path taken from start to goal: [0, 1, 2, 3, 7, 11, 15]
Steps to goal: 6
