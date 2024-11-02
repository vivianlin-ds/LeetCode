# Question: Implement RecentCounter class such that RecentCounter() initializes counter with zero recent requests and
# int ping(int t) adds new request at time t, where t represents some time in ms, and return number of requests that
# has happened in the past 3000 ms (including new request). Specifically, return number of requests that have
# happened in the inclusive range [t-3000, t]. Guaranteed that every call to ping uses strictly larger value of t than
# previous call.

class RecentCounter:
    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < (t - 3000):
            self.queue.pop(0)
        # print(len(self.queue))
        return len(self.queue)


def main():
    recent = RecentCounter()
    recent.ping(642)
    recent.ping(1849)
    recent.ping(4921)
    recent.ping(5936)
    recent.ping(5957)


if __name__ == '__main__':
    main()
