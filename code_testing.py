eps = 1
eps_dec = 0.99975

episode = 0
while True:
    episode += 1
    eps = eps * eps_dec
    print(episode, eps)
    if eps < 0.001:
        break