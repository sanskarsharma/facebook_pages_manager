class MyCounter(object):
    dict = {"hi":"hello"}

    @classmethod
    def save(cls, delta={"bye":"bello"}):
        cls.count = delta

# >>> MyCounter.count
# 0
# >>> MyCounter.inc()
# >>> MyCounter.count
# 1
# >>> MyCounter.inc(5)
# >>> MyCounter.count
# 6