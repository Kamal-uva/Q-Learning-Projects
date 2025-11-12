"""
Gridworld Q-Learning Example

This project implements Q-learning in a 4x4 grid environment. The agent learns 
to navigate from start to goal using reinforcement learning.
"""

import numpy as np

# Environment setup
grid_size = 4
n_states = grid_size * grid_size
n_actions = 4  # Up, Right, Down, Left
start_state = 0
goal_state = 15

# Q-learning parameters
learning_rate = 0.1
discount_factor = 0.9
exploration_rate = 0.1
episodes = 1000

# Initialize Q-table
Q = np.zeros((n_states, n_actions))

# Helper function: get next state based on action
def get_next_state(state, action):
    row, col = divmod(state, grid_size)
    
    if action == 0:  # Up
        row = max(0, row - 1)
    elif action == 1:  # Right
        col = min(grid_size - 1, col + 1)
    elif action == 2:  # Down
        row = min(grid_size - 1, row + 1)
    elif action == 3:  # Left
        col = max(0, col - 1)
    
    return row * grid_size + col

# Training loop
for _ in range(episodes):
    state = start_state
    while state != goal_state:
        # Epsilon-greedy action selection
        if np.random.rand() < exploration_rate:
            action = np.random.randint(n_actions)
        else:
            action = np.argmax(Q[state])
        
        next_state = get_next_state(state, action)
        reward = 1 if next_state == goal_state else -0.01
        Q[state, action] += learning_rate * (reward + discount_factor * np.max(Q[next_state]) - Q[state, action])
        state = next_state

# Extract optimal policy
actions_symbols = ['↑', '→', '↓', '←']
policy = np.array([actions_symbols[np.argmax(Q[s])] for s in range(n_states)]).reshape((grid_size, grid_size))

# Display results
print("Optimal Policy Grid:")
for row in range(grid_size):
    for col in range(grid_size):
        state = row * grid_size + col
        print('G' if state == goal_state else policy[row, col], end=' ')
    print()

# Test the learned policy
state = start_state
path = [state]
steps = 0
while state != goal_state and steps < 20:
    action = np.argmax(Q[state])
    state = get_next_state(state, action)
    path.append(state)
    steps += 1

print(f"\nPath taken from start to goal: {path}")
print(f"Steps to goal: {steps}")
