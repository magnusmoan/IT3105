import gym

env = gym.make('FrozenLake-v0')
env.reset()

for episode in range(100):
    print "New episode!"
    observation = env.reset()
    for _ in range(40):
        env.render()
        action = env.action_space.sample()

        # NOTE: The step direction does not always equal the direction of the action.
        observation, reward, done, info = env.step(action)
        if done:
            print reward
            if reward > 0:
                raw_input()
            break
