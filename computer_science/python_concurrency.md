# 파이썬 메모리

파이썬에서는 GIL(Global Interpreter Lock)으로 인하여 멀티 쓰레딩을 해도 시간이 크게 단축되지 않는다. 이에 GIL에 대해 알아보고, GIL의 단점을 보완해주는 asyncio에 대해 알아보고자 한다.


# what is multi threading?

프로그램이 메모리에 올라오면 4가지 영역(Code, Data, Heap, Stack)을 할당받는다.

* TIP
- code 영역은 실행한 프로그램의 코드가 저장되는 메모리 영역을 의미한다.
- data 영역은 프로그램의 전역 변수와 static 변수가 저장되는 메모리 영역을 의미한다.
- heap 영역은 프로그래머가 직접 공간을 할당(malloc)/해제(free) 하는 메모리 영역을 의미한다.
- stack 영역은 함수 호출 시 생성되는 지역 변수와 매개 변수가 저장되는 임시 메모리 영역을 의미한다.

## Thread
thread는 한 process 내에서 실행되는 동작(기능 function)의 단위를 의미한다.

## Multi-Thread
Multi thread란 하나의 process가 동시에 여러개의 일을 수행할수 있도록 해주는 것입니다. 즉, 하나의 process에서(실행이 된 하나의 program에서) 여러 작업을 병렬로 처리하기 위해 multi thread를 사용
각 thread는 속해있는 process의 Stack 메모리를 제외한 나머지 memory 영역을 공유할 수 있다.
thread가 process내에서 "독립적인 기능을 실행”한다는 것은 "독립적으로 함수를 호출"함을 의미한다. 즉, Stack은 함수 고유의 지역변수와 매개 변수가 저장되는 영역임으로 공유되면 안 된다.

# python : GIL

## what is gil?

- 파이썬에 객체 접근의 안정성을 위해, 멀티 쓰레딩 환경에서 하나의 쓰레드만 실행하게 하는 방식

## why gil?
- 파이썬에서는 객체를 만든 뒤에 변수를 참조하게 한다.(Everything is object) 그리고 파이썬의 가비지 컬렉터는 reference count로 통해 메모리를 관리하고 있다.
- `x=7`로 선언한다면 힙 메모리에 `7 int`의 파이썬 객체를 동적으로 할당 한 뒤에, 스택 변수 x가 7을 참조하게 한다.
- 이 때 파이썬 메모리는 `7 int`의 reference count의 값을 증가시키고, 참조하지 않게 되면 값을 감소시킨다.
- 만약 r.f count가 0이 되면 해당 객체를 메모리에서 제거한다.
- 만약 여기에서 lock을 걸지 않는다면, 2개의 쓰레드가 동시에 접근하게 되어 객체를 삭제하게 할 수 있다.

* TIP
- JAVA에서는 `7 int`선언시 Stack영역에서 호출된다. 그리고 변수 선언 시 메모리 위치가 7이 저장된 곳을 가리킨다.

# asyncio
비동기 표준 라이브러리(python 3.4 -)
asyncio(Asynchronous I/O)는 비동기 프로그래밍을 위한 모듈이며 CPU 작업과 I/O를 병렬로 처리하게 해줍니다.

# Why use?
함수가 종료되지 않은 상태에서 메인 루틴의 코드를 실행한 뒤 다시 돌아와서 코루틴의 코드를 실행


> 파이썬 GIL 설명 : https://docs.python.org/3/c-api/init.html
> 참조(인도 아저씨 유튜브) : https://www.youtube.com/watch?v=arxWaw-E8QQ
> 참조(블로그) : https://leemoney93.tistory.com/25
> 인프런 lv4