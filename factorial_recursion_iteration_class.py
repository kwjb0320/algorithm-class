#############################################################################
#  시스템 스택 호출과 재귀함수를 이용한 팩토리얼 계산 콘솔 인터렉티브 프로그램 
#  작성자: 홍길동
#  작성일: 2024-09-15
# 순환(recursion)과 반복(iteration)의 차이점 이해
#  - 반복문 기반과 재귀 기반의 팩토리얼 계산 함수 구현
#  - 유효성 검사 포함 (0 이상 정수 확인)
#  - 문자열 입력 → 정수 변환 → 유효성 검사 → 팩토리얼 계산까지 포함된 콘솔 프로그램 형태
#  - q 또는 quit 입력 시 종료
#############################################################################

def factorial_iter(n):
    # 반복문 기반 n! 계산
    result = 1
    for k in range(2, n + 1):
        result *= k
    return result

def factorial_rec(n):
    # 재귀 호출 기반 n! 계산
    if n == 0 or n == 1:
        return 1
    return n * factorial_rec(n - 1)

def main():
    while True:
        user_input = input("\n정수를 입력하세요 (q 또는 quit 입력 시 종료): ").strip().lower()
        
        if user_input in ('q', 'quit'):
            print("프로그램을 종료합니다.")
            break

        if not user_input.isdigit():
            print("⚠️ 0 이상의 정수를 입력해주세요.")
            continue

        n = int(user_input)
        
        print(f"\n입력값: {n}")
        print(f"반복문 기반: {factorial_iter(n)}")
        try:
            print(f"재귀 기반: {factorial_rec(n)}")
        except RecursionError:
            print("입력값이 너무 커서 재귀 계산은 불가능합니다.")

if __name__ == "__main__":
    main()
