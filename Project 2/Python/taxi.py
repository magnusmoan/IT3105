import gym

env = gym.make('Taxi-v1')
env.reset()

for episode in range(100):
    print "New episode!"
    observation = env.reset()
    for _ in range(40):
        env.render()
        raw_input()
        action = env.action_space.sample()
        print action

        # NOTE: The step direction does not always equal the direction of the action.
        observation, reward, done, info = env.step(action)
        if done:
            print reward
            raw_input()
            break
