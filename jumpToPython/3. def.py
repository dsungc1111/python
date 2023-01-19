# 1. 함수 정의
# def add(a, b):
#     return a+b  # a,b는 매개변수, 함수에 입력으로 전달된 값


# c = add(5, 6)  # 인수는 함수를 호출할 때 전달하는 입력 값

# print(c)

# 2. 입력값 x 함수

# def say():
#     return 'hello'


# a = say()
# print(a)

# 3. 입력값이 여러개

# def add_many(*args):
#     result = 0
#     for i in args:
#         result = result + i
#     return result


# result = add_many(1, 2, 3, 4, 5)

# print(result)

# 4. 매개변수 추가

# def add_mul(choice, *args):
#     if choice == 'add':
#         result = 0
#         for i in args:
#             result = result + i
#     elif choice == 'mul':
#         result = 1
#         for i in args:
#             result = result*i
#     return result


# result1 = add_mul('add', 2, 3, 4, 5)
# result2 = add_mul('mul', 2, 3, 4, 5)


# 5. 키워드 매개변수 kwargs

# def print_kwargs(**kwargs):
#     print(kwargs)


# print_kwargs(a=1)


# 6. 람다함수

def add(a, b): return a+b


result = add(3, 4)
print(result)
