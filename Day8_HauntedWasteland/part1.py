
with open("./input.txt") as file:
    lr_inst, nodes = file.read().split("\n\n")
    lr_inst = [1 if lr == 'R' else 0 for lr in lr_inst]
    nodes = nodes.splitlines()
    nodes = dict(n.split(" = ") for n in nodes)
    for k, v in nodes.items():
        nodes[k] = v.strip('()').replace(' ', '').split(',')


current_node = nodes['AAA']
n_steps = 1
lr_idx = 0
len_lr = len(lr_inst)
while True:
    lr = lr_inst[lr_idx]
    lr_idx = (lr_idx + 1) % len_lr
    new_key = current_node[lr]
    if new_key == 'ZZZ':
        break

    current_node = nodes[new_key]
    n_steps += 1


print(f"Walking took {n_steps} steps")
