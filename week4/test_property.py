class A:
    def __init__(self):
        self.x = 1

    def __getattr__(self, y):
        print("you called", y)
        return self.x


a = A()
print(a.name)
