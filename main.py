import os
from FSM import FSM


def ReadFile(path: str):
    fsm = FSM()
    with open(path, 'r') as file:
        for line in file:
            fsm.send(line)

    for token in fsm.token_list:
        print("=>: ", token)


if __name__ == "__main__":
    path = "./inputs/"
    files = os.listdir(path)
    for file in files:
        ReadFile(os.path.join(path, file))
