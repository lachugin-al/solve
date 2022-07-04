# Абсолюные значения
# Скоуп

class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here

    def computeDifference(self):
        maximum = 0
        n = len(self.__elements)
        for i in range(0, n - 1, 1):
            for j in range(i + 1, n, 1):
                abs_diff = abs(self.__elements[i] - self.__elements[j])  # absolute
                if abs_diff > maximum:
                    maximum = abs_diff

        self.maximumDifference = maximum


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]
d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
