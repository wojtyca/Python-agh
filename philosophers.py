import threading
import time
import random

class DiningPhilosopher(threading.Thread):

    def __init__(self, philosopher_number, left_fork, right_fork):
        super().__init__()
        self.philosopher_number = philosopher_number  #philosopher index
        self.left_fork = left_fork                    #forks on left and right sides
        self.right_fork = right_fork

    def try_to_eat(self):
        self.left_fork.acquire()                      #locking the state
        self.right_fork.acquire()

        print(f"Philosopher no {self.philosopher_number} is eating\n")
        time.sleep(4)
        print(f"Philosopher no {self.philosopher_number} has stopped eating\n")

        self.left_fork.release()
        self.right_fork.release()

    def run(self):
        while True:
            print(f"Philosopher no {self.philosopher_number} is thinking\n")
            time.sleep(random.randint(1, 6))           #randomized "thinking" period
            self.try_to_eat()


if __name__ == '__main__':
    forks = [threading.Condition(threading.Lock()) for idx in range(5)]
    philosophers = [DiningPhilosopher(idx, forks[idx], forks[(idx + 1) % 5]) for idx in range(5)]

    for philo in philosophers:
        philo.start()
