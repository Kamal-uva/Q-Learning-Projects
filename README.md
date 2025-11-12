# Q-Learning Mini Projects

This repository contains two small, self-contained **Reinforcement Learning (RL)** projects built to demonstrate the fundamentals of **Q-Learning**, one of the most widely used algorithms for teaching agents to make decisions through experience.  
Both examples are minimal yet illustrative — designed for learning, experimentation, and portfolio display.

---

## Project 1: Simple Q-Learning

**File:** `simple_rl/simple_q_learning.py`

A minimal environment with three states — `start`, `candy`, and `fire` — and two possible actions (`left`, `right`).  
The goal is for the agent to learn that moving **right from the start** leads to the “candy” reward (+1) while moving **left** leads to “fire” (–1).

### Key Concepts
- Basic Q-table initialization and updates  
- Reward shaping (penalizing long paths)  
- Learning rate (α) and discount factor (γ) tuning  
- Simple environment modeling  

### How It Works
Each episode starts in the `start` state.  
The agent randomly chooses actions, receives rewards, and updates its Q-table using the formula:


After several episodes, the agent learns to consistently choose the optimal action (right toward candy).

---

## Project 2: GridWorld Q-Learning

**File:** `gridworld_rl/gridworld_q_learning.py`

A classic **GridWorld** setup where the agent starts in the **top-left corner (state 0)** and learns to reach the **bottom-right goal (state 15)** on a 4×4 grid.  
The environment uses small negative rewards (–0.01) for movement and a positive reward (+1) for reaching the goal.

### Key Concepts
- 2D state-space navigation  
- Epsilon-greedy exploration strategy  
- Reward-based policy optimization  
- Learned policy visualization using arrows (`↑`, `→`, `↓`, `←`)  

### How It Works
The agent starts at state 0 and repeatedly explores random paths.  
Over time, it learns which actions lead to the goal fastest by maximizing cumulative rewards.  
The resulting Q-table is converted into a visual policy grid showing the best move for each cell.

---

## How to Run Locally

Clone the repository:
```bash
git clone https://github.com/<your-username>/Q-Learning-Mini-Projects.git
cd Q-Learning-Mini-Projects

Run either project:
python3 simple_rl/simple_q_learning.py 
python3 gridworld_rl/gridworld_q_learning.py

You’ll see printed output of:
The final Q-table
The optimal policy (best action per state)
The path the agent takes to reach its goal

Requirements:

Python 3.9+
Dependencies:
numpy (for GridWorld)
Built-in libraries: random
Install required packages:
pip install numpy
