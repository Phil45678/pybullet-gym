import gym
import pybulletgym  # register PyBullet enviroments with open ai gym
import time

env = gym.make('InvertedPendulumMuJoCoEnv-v0')

# env = gym.make('CartPole-v0')
#env.monitor.start('/tmp/cartpole-experiment-1', force=True)
env.render(mode = 'human')
observation = env.reset()

for t in range(1000):
    print(observation)
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    time.sleep(1/60)
    if done:
        print("Episode finished after {} timesteps".format(t+1))
        break