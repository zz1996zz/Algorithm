import collections
from typing import List


class MyStack: # 큐로 스택 구현하기

    def __init__(self):
        self.q = collections.deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        # 큐는 선입선출이기때문에 최근에 들어온것들의 앞에 값들을 다 뒤로 보내줘야한다.
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


