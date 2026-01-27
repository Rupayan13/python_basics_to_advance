class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def description(cls):
        print("This is a utility class for math operations.")


print(MathUtils.add(5, 10))
MathUtils.description()
