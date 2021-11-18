# Iterable 순회 가능한 객체

# 리스트
for n in [1,2,3,4,5]:
    print(n)

# 문자열
for n in "Hello World":
    print(n)

# dict
for n in {"이름": "지수", "나이": "26"}:
    print(n)

# set
for n in {1,2,3,4,5}:
    print(n)


# ------------------------------------------------------------------- #


# iterator

# iter()로 Iterable 객체의 iterator를 리턴
my_list = [1,2,3,4,5]
my_iter = iter(my_list)
print(my_iter) # <list_iterator object at 0x00000191049D09E8>

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
# print(next(my_iter)) # StopIteration


# ------------------------------------------------------------------- #


# iterator 생성
class MyCollection:
    def __init__(self):
        self.size = 10
        self.data = list(range(self.size))

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= self.size:
            raise StopIteration

        n = self.data[self.index]
        self.index += 1
        return n


coll = MyCollection()
for x in coll:
    print(x)
