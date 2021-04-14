
from pybulletgym.envs.roboschool.envs.pendulum.inverted_double_pendulum_env import InvertedDoublePendulumBulletEnv

import pybullet as p 


if __name__ == "__main__":


    print("Start")

    physicsClient = p.connect(p.GUI)

    # Initializing the environment 
    pend_env = InvertedDoublePendulumBulletEnv() 

    pend_env.create_single_player_scene(p)

    #pend_env.camera_adjust()

    