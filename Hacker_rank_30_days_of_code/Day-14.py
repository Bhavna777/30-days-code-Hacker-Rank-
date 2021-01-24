class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        diff = 0
        for i in range(len(self.__elements)):
            for j in range(len(self.__elements)):
                if (abs(self.__elements[j] - self.__elements[i]) > diff):
                    diff = abs(self.__elements[j] - self.__elements[i])
        self.maximumDifference = diff
                

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)