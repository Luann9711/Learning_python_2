# Chapter06-04
# Futures 동시성
# 비동기 작업 실행
# 지연시간(Block) CPU 및 리소스 낭비 방지 -> File Netwrok I/O 관련 작업 -> 동시성 활용 권장
# 비동기 작업과 적합한 프로그램일 경우 압도적으로 퍼포먼스 향상 가능

# futures : 비동기 실행을 위한 API 를 고수준으로 작성 -> 사용하기 쉽도록 개선
# concurrent.Futures
# 멀티스레딩 / 멀티프로세싱 API 통일 -> 사용하기가 매우 용이
# 실행중에 작업 취소, 완료 여부 체크, 타임아웃 옵션, 콜백함수 추가, 동기화 코드 매우 쉽게 작성

# concurrent.futures 사용법 1
# concurrent.futures 사용법 2

# GIL(Global interpreter Lock): 두 개 이상의 스레드가 동시에 실행될 때 하나의 자원을 엑세스 하는 경우
#       GIL 실행 , 리소스 전체에 락이 걸린다. -> Context Switch(문맥 교환)

#GIL 우회? : 멀티프로세싱 사용, CPython


import time
from concurrent import futures

WORK_LIST = [10000, 100000, 1000000, 10000000]

# 누적합계 함수 (제네레이터)
def sum_generator(n):
    return sum(n for n in range(1, n + 1))

# 동시성 합계 계산 메인함수
def main():
    # Worker Count  // 스레드 수의 최대값을 지정해두고 WORK_LIST 갯수중 작은 수를 스레드 수로 설정한다
    worker = min(10, len(WORK_LIST))

    # 측정시작
    start_tm = time.time()

    # 결과 건수
    # processPoolExecutor
    with futures.ProcessPoolExecutor() as excutor:
        # map  작성순서 유지하고 즉시 실행
        result = excutor.map(sum_generator, WORK_LIST)

    # 측정종료
    end_tm = time.time() - start_tm

    msg = 'Result - {} Time : {:.2f}s'.format(list(result), end_tm)
    print(msg)


if __name__ == '__main__':
    main()
