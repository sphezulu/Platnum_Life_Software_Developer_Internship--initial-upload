class TestMath:

    def test_add(x, y):
        return x + y

    def test_subtract(x, y):
        return x - y

    def test_milutiply(x, y):
        return x * y

x = 10
y = 10
math = TestMath()
print(math.test_add(x,y), math.test_milutiply(x,y), math.test_subtract(x,y))