from Agent import *


env = BlobEnv()
agent = DQNAgent()
agent.model = tf.keras.models.load_model("./models best/40Kepisodes_BEST_2x256____25.00max__-37.16avg_-407.00min__1604741142.model")



def play():
    episode = 0
    while True:
        print(episode)
        episode += 1
        # Reset environment and get initial state
        current_state = env.reset()

        cv2.waitKey(500)
        done = False
        while not done:
            action = np.argmax(agent.get_qs(current_state))

            new_state, reward, done = env.step(action)

            env.render()

            current_state = new_state

play()