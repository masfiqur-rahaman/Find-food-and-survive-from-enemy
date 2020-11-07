# Find-food-and-survive-from-enemy

Blue square: Agent<br>
Green square:  Food<br>
Red square: Enemy<br>

In this app, a "Blue" agent has to survive from a "Red" enemy and fetch the desired "Green" food. I have used Deep Reinforcement Learning to train the agent to achieve this goal.

It takes a total of 40,000 episodes to train the agent. However, in some cases you may see agent falls in the hand of enemy or agent may be stuck in corners. Maybe, I have to train more to achieve better accuracy.

##This project contains the following files/folders:
1. requirements.txt: import these (pip install) packages before train/play.
2. environment.yml: import these (conda create) packages before train/play.
3. Train.py: Run this to start training
5. Play.py: Run this to play the agent.
6. Agent.py: Contains the agent class
7. Blob.py: Contains the blob (Red, Green, Blue blobs) class
8. Blob_environment.py: Contains the environment class
9. code_testing.py: (Not related to project. You may delete this)
10. Modified_Tensorboard.py: Modified tensorboard to track the progress of training
11. /models best: Contains the best models after training
12. /logs: contains training metrics (you can visualize them using tensorboard)

