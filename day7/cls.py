class Myclass:
    count = 0
    def increment(cls):
        cls.count += 1
        print("counr increment{cls.count}")
Myclass.increment()
print(Myclass.count)
