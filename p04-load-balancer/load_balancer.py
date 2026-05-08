import random

class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.index = 0

    # ROUND ROBIN
    def round_robin(self):
        server = self.servers[self.index]
        self.index = (self.index + 1) % len(self.servers)
        return server

    # RANDOM
    def random_selection(self):
        return random.choice(self.servers)

    # HASHING
    def hashing(self, request_id):
        return self.servers[request_id % len(self.servers)]


def simulate_requests(lb, num_requests):
    for i in range(num_requests):
        print(f"\nRequest {i+1}")

        rr = lb.round_robin()
        print("Round Robin →", rr)

        rand = lb.random_selection()
        print("Random →", rand)

        hash_server = lb.hashing(i)
        print("Hashing →", hash_server)


# MAIN
if __name__ == "__main__":
    servers = ["Server A", "Server B", "Server C"]

    lb = LoadBalancer(servers)

    simulate_requests(lb, 7)
