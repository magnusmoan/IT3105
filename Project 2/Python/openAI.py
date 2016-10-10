import gym

#   Implements random policy 
def run_taxi(N):
	env = gym.make("Taxi-v1")
	observation = env.reset()
	for _ in range(N):
		env.render()
		action = env.action_space.sample()
		observation, reward, done, info = env.step(action)

#   Implements random policy 
def run_frozen_lake(N):
	env = gym.make("FrozenLake-v0")
	observation = env.reset()
	for _ in range(N):
		env.render()
		action = env.action_space.sample()
		observation,reward, done, info = env.step(action)

#run_taxi(10)
run_frozen_lake(10)
