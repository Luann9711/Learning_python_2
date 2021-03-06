# Chapter06-05
# Futures 동시성
# 비동기 작업 실행
# 지연시간(Block) CPU 및 리소스 낭비 방지 -> (File)Network I/O 관련 작업 -> 동시성 활용 권장
# 비동기 작업과 적합한 프로그램일 경우 압도적으로 성능 향상

# futures : 비동기 실행을 위한 API를 고수준으로 작성 -> 사용하기 쉽도록 개선
# concurrent.Futures
# 1. 멀티스레딩/멀티프로세싱 API 통일 -> 매우 사용하기 쉬움
# 2. 실행중이 작업 취소, 완료 여부 체크, 타임아웃 옵션, 콜백추가, 동기화 코드 매우 쉽게 작성 -> Promise 개념

# 2가지 패턴 실습
# concurrent.futures map
# concurrent.futures wait, as_completed

# GIL : 두 개 이상의 스레드가 동시에 실행 될 때 하나의 자원을 엑세스 하는 경우 -> 문제점을 방지하기 위해
#       GIL 실행 , 리소스 전체에 락이 걸린다. -> Context Switch(문맥 교환)

# GIL : 멀티프로세싱 사용, CPython

import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait, as_completed

WORK_LIST = [1000, 10000, 100000, 1000000]


# 누적합계 함수 (제네레이터)
def sum_generator(n):
    return sum(n for n in range(1, n + 1))


# 동시성 합계 계산 메인함수
# wait
# as_completed
def main():
    # Worker Count  // 스레드 수의 최대값을 지정해두고 WORK_LIST 갯수중 작은 수를 스레드 수로 설정한다
    worker = min(10, len(WORK_LIST))

    # 측정시작
    start_tm = time.time()
    #Futures
    futures_list = []

    # 결과 건수
    # processPoolExecutor
    with ThreadPoolExecutor() as excutor:
        for work in WORK_LIST:
            # future 반환
            future = excutor.submit(sum_generator, work)
            # 스케줄링
            futures_list.append(future)
            # 스케쥴링 확인
            print('scheduled for {} : {}'.format(work, future))
            print()
        

        # wait 결과 출력
        # result = wait(futures_list, timeout=7)

        # # 성공
        # print('Completed task : ' + str(result.done))
        # # 실패 - 7초가 지난 작업은 실패 처리
        # print('Pending ones after waiting for 7 seconds : ' + str(result.not_done))

        # # 최종결과 값 출력
        # print([future.result() for future in result.done])

        # as_completed 결과 출력
        for future in as_completed(futures_list):
            result = future.result()
            done = future.done()
            cancelled = future.cancelled

            # future 결과 확인
            print('Future Result : {}, Done : {}'.format(result, done))
            print('Future cancelled : {}'.format(result, cancelled))



    # 측정종료
    end_tm = time.time() - start_tm

    msg = '\n Time : {:.2f}s'.format(end_tm)
    print(msg)


if __name__ == '__main__':
    main()
