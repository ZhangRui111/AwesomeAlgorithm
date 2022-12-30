"""
tag: 设计；有序集合；堆
855. 考场就座
https://leetcode.cn/problems/exam-room/
"""
import bisect


class ExamRoom0:
    """ 超时 """
    def __init__(self, n: int):
        self.n = n
        self.seats = [0] * n
        self.n_stus = 0

    def seat(self) -> int:
        if self.n_stus == 0:
            self.seats[0] = 1
            self.n_stus += 1
            return 0

        target = -1
        max_dis = 0
        for p in range(self.n):
            if self.seats[p] == 0:
                dis = self.min_max_dis(p)
                if dis > max_dis:
                    max_dis = dis
                    target = p
        self.seats[target] = 1
        self.n_stus += 1
        return target

    def leave(self, p: int) -> None:
        self.seats[p] = 0
        self.n_stus -= 1

    def min_max_dis(self, p: int) -> int:
        pre, post = p - 1, p + 1
        while pre > -1 and self.seats[pre] != 1:
            pre -= 1
        while post < self.n and self.seats[post] != 1:
            post += 1
        if pre >= 0 and post <= self.n - 1:
            return min(p - pre, post - p)
        elif pre >= 0:
            return p - pre
        else:
            return post - p


class ExamRoom1(object):
    def __init__(self, n: int):
        self.N = n
        self.students = []

    def seat(self):
        # Let's determine student, the position of the next
        # student to sit down.
        if not self.students:
            target = 0
        else:
            # dist is the distance to the closest student,
            # which is achieved by sitting in the position 'student'.
            # We start by considering the left-most seat.
            target, dist = 0, self.students[0]
            for i, s in enumerate(self.students):
                if i > 0:
                    prev = self.students[i - 1]
                    # For each pair of adjacent students in positions (prev, s),
                    # d is the distance to the closest student;
                    # achieved at position prev + d.
                    d = (s - prev) // 2
                    if d > dist:
                        target, dist = prev + d, d

            # Considering the right-most seat.
            d = self.N - 1 - self.students[-1]
            if d > dist:
                target = self.N - 1

        # Add the student to our sorted list of positions.
        bisect.insort(self.students, target)
        return target

    def leave(self, p):
        self.students.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)


