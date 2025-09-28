import time
import sys

def factorial_iter(n):  # 반복문
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_rec(n):  # 재귀
    if n == 0 or n == 1:
        return 1
    return n * factorial_rec(n - 1)

def run_with_time(func, n):
    start_time = time.time()
    result = func(n)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return result, elapsed_time

def run_test_cases():
    test_cases = [0, 1, 5, 10, 20, 50, 100]
    print("\n[테스트 데이터 실행]")
    for n in test_cases:
        print(f"\n>> n = {n}")
        iter_result, iter_time = run_with_time(factorial_iter, n)
        rec_result, rec_time = run_with_time(factorial_rec, n)
        print(f"[반복] {n}! = {iter_result}")
        print(f"[반복] 시간: {iter_time:.7f}초")
        print(f"[재귀] {n}! = {rec_result}")
        print(f"[재귀] 시간: {rec_time:.7f}초")

while True:
    print("============ Factorial Tester =============")
    print("1: 반복법으로 n! 계산")
    print("2: 재귀로 n! 계산")
    print("3: 두 방식 모두 계산 후 결과/ 시간 비교")
    print("4: 준비된 테스트 데이터 일괄 실행")
    print("q: 종료")
    print("---------------------------------------------------")
    method = input("선택:").strip()

    if method == 'q':
        print("프로그램을 종료")
        break

    elif method in ['1', '2', '3']:
        try:
            num = int(input("n값(정수, 0 이상)을 입력하세요: "))
            if num < 0:
                print("0 이상 정수를 입력하세요")
                continue
        except ValueError:
            print("유효한 정수를 입력하세요")
            continue

        if method == '1':
            iter_result, iter_time = run_with_time(factorial_iter, num)
            print(f"[반복] {num}! = {iter_result}")

        elif method == '2':
            try:
                rec_result, rec_time = run_with_time(factorial_rec, num)
                print(f"[재귀] {num}! = {rec_result}")
            except RecursionError:
                print("재귀 깊이 초과 오류")

        elif method == '3':
            iter_result, iter_time = run_with_time(factorial_iter, num)
            print(f"[반복] {num}! = {iter_result}")
            print(f"[반복] 시간: {iter_time:.7f}초")
            try:
                rec_result, rec_time = run_with_time(factorial_rec, num)
                print(f"[재귀] {num}! = {rec_result}")
                print(f"[재귀] 시간: {rec_time:.7f}초")
            except RecursionError:
                print("재귀 깊이 초과 오류 ")

    elif method == '4':
        run_test_cases()

    else:
        print("잘못된 입력 1, 2, 3, 4 또는 q를 입력")
