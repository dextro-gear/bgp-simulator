from autonomous_system import autonomous_system


def optimize(systems):
    for asys in systems:
        asys.reset()

    for _ in range(len(systems) - 1):
        for asys in systems:
            for other_as in asys.neighbours.keys():
                asys.update(other_as)
