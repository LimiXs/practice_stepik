# https://stepik.org/lesson/701988/step/10?unit=702089

class Clock:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds


class DeltaClock:
    def __init__(self, clock1: Clock, clock2: Clock):
        self.clock1 = clock1
        self.clock2 = clock2

    def __len__(self):
        diff = self.clock1.get_time() - self.clock2.get_time()
        return diff if diff > 0 else 0

    def __str__(self):
        d = self.__len__()
        h = d // 3600
        m = d % 3600 // 60
        s = d % 3600 % 60
        return f"{h:02}: {m:02}: {s:02}"


dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt)  # 01: 30: 00
len_dt = len(dt)  # 5400
