class Frontier:
    nodes_popped = 0
    nodes_expanded = 0
    nodes_generated = 0
    max_fringe_size = 0

    def __init__(self):
        self.queue = []

    def add(self, node):
        Frontier.nodes_generated += 1
        if len(self.queue) == 0:
            self.queue.append(node)
        else:
            for i in range(len(self.queue)):
                if node < self.queue[i]:
                    self.queue.insert(i, node)
                    break
            else:
                self.queue.append(node)

        if len(self.queue) > Frontier.max_fringe_size:
            Frontier.max_fringe_size = len(self.queue)

    def pop(self):
        Frontier.nodes_popped += 1
        return self.queue.pop(0)

    def __len__(self):
        return len(self.queue)

    def __contains__(self, node):
        return node in self.queue
