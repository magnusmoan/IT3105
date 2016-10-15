from agent import *
import matplotlib.pyplot as plt

### Parameters ###
episode_count = 15000
episode_length = 100
q = [{'s': 1.0, 'w': .5, 'n': .5, 'e': .5} for _ in xrange(16)]
eps = .1
learning_rate = .0915
discount_rate = .99

### Problem 1 ###
#random_lake_agent = Random_Agent("FrozenLake-v0")
#random_taxi_agent = Random_Agent("Taxi-v1")
#random_lake_agent.run_env(episode_length, episode_count)
#random_taxi_agent.run_env(episode_length, episode_count)


### Problem 2a ###
#lake_agent = Lake_Agent(q=q)
#lake_agent.run_env(episode_length, episode_count)


### Problem 2b ###
#greedy_lake_agent = Greedy_Lake_Agent(q=q)
#greedy_lake_agent.run_env(episode_length, episode_count)


### Problem 2c ###
#greedy_lake_agent = Greedy_Lake_Agent(q=q, eps=eps)
#greedy_lake_agent.run_env(episode_length, episode_count)


### Problem 3 ###
lake_agent = Greedy_Lake_Agent(learning_rate=learning_rate, eps=eps, discount_rate=discount_rate)
q, rewards = lake_agent.run_env_with_learning(episode_length, episode_count)
print q
print rewards[-1]
"""
improved_agent = Greedy_Lake_Agent(q=q, learning_rate=learning_rate, eps=0, discount_rate=discount_rate)
_, rewards = improved_agent.run_env_with_learning(1000, 100, True)
print rewards[-1]
plt.plot([i for i in range(1, 100+1)], rewards)
plt.axis([0, 100, 0, 1])
plt.show()
"""
