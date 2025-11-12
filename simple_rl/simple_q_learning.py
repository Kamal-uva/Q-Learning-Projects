"""
Simple Q-Learning Example: Start-Candy-Fire Environment

This is a mini reinforcement learning project demonstrating basic Q-learning 
with a small discrete environment.
"""

import random

# Environment definition
states = ["start", "candy", "fire"]
actions = ["left", "right"]

# Initialize Q-table
Q = {s: {a: 0 for a in actions} for s in states}

# Reward and transition mapping
rewards = {
    ("start", "right"): ("candy", 1),
    ("start", "left"): ("fire", -1),
    ("candy", "left"): ("start", 0),
    ("fire", "right"): ("start", 0),
}

# Q-learning parameters
alpha = 0.5   # learning rate
gamma = 0.5   # discount factor
episodes = 200

# Training loop
for _ in range(episodes):
    state = "start"
    for _ in range(5):
        action = random.choice(actions)
        next_state, reward = rewards.get((state, action), (state, 0))
        best_next = max(Q[next_state].values())
        Q[state][action] += alpha * (reward + gamma * best_next - Q[state][action])
        state = next_state
        reward -= 0.1  # small penalty to prefer shorter paths

# Display results
print("Q-Table after learning:")
for s in Q:
    print(f"{s}: {Q[s]}")
