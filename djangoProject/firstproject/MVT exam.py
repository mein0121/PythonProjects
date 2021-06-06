# 나눗셈 함수
# 두개의 값을 받아서 나눈다음에 결과를 올림(ceil)해서 출력
import math
def divide(num1, num2):
    #파라미터값 변환/검증
    # 변환(num1, num2를 int(정수)로 변환)
    num1, num2 = int(num1), int(num2)
    # num2가 0인지 확인 -> 0 일 경우 예외 발생 ==> 파라미터 검증
    if num2 == 0:
        raise Exception("0으로 나눌수 없습니다.")
    # 나누고 올림 작업 - business logic (DB=>Model)
    result = num1/num2
    result = math.ceil(result)

    # 결과 출력
    print("="*50)
    print("나누기 결과는 올림해서 정수로 출력합니다.")
    print("결과 : {}".format(result))
    print("=" * 50)


def validator(num1, num2):
    #파라미터값 변환/검증
    #변환(num1,num2를 int(정수)로 변환)
    num1, num2 = int(num1), int(num2)
    # num2가 0인지 확인 -> 0 일 경우 예외 발생 ==> 파라미터 검증
    if num2 == 0:
        raise Exception("0으로 나눌수 없습니다.")
    return num1, num2

def Model(num1, num2):
    # 나누고 올림 작업 - business logic (DB=>Model)
    result = num1 / num2
    result = math.ceil(result)
    return result

def Template(result):
    # 결과 출력
    print("="*50)
    print("나누기 결과는 올림해서 정수로 출력합니다.")
    print("결과 : {}".format(result))
    print("=" * 50)

def divideView(num1, num2):
    num1, num2 = validator(num1, num2)
    result = Model(num1,num2)
    Template(result)