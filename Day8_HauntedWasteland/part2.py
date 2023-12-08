import math

with open("./input.txt") as file:
    lr_inst, nodes = file.read().split("\n\n")
    lr_inst = [1 if lr == 'R' else 0 for lr in lr_inst]
    nodes = nodes.splitlines()
    nodes = dict(n.split(" = ") for n in nodes)
    for k, v in nodes.items():
        nodes[k] = v.strip('()').replace(' ', '').split(',')



def get_steps(start: str):
    current_node = nodes[start]
    n_steps = 1
    lr_idx = 0
    len_lr = len(lr_inst)
    while True:
        lr = lr_inst[lr_idx]
        lr_idx = (lr_idx + 1) % len_lr
        new_key = current_node[lr]
        if new_key[-1] == 'Z':
            break

        current_node = nodes[new_key]
        n_steps += 1

    return n_steps


# Every individual node would reach the end at (int) k * <needed steps>
# If path one would take 2 steps, and second path would take 4 steps, then
# in order to reach the end at both, we would need 4 steps.
# If second path reached it in 5 steps (first still at 2 steps), then we would need 10 steps,
# so we can use least common multiple to get the minimal one.
# That is of course if the end node points back to the start, which it seems it does.
print(f"Walking took {math.lcm(*(get_steps(k) for k in nodes if k[-1] == 'A'))} steps")
