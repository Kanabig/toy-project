"""
처음 프로그램이 실행하면, 다음과 같은 메뉴를 출력한다
메뉴: 1.회원가입   2.로그인   3.특정 회원정보 출력   4.모든 회원정보 출력   99.종료
'1.회원가입'을 선택하면, 회원ID, 회원Email, 회원Phone 정보를 입력받아 회원가입을 진행한다
'2.로그인'을 선택하면, 회원ID, 회원PW를 입력받아 로그인 '성공'또는 '실패'를 출력한다
'3.특정 회원정보 출력'을 선택하면, 회원ID와 회원PW를 입력받아 일치하는 회원정보를 모두 출력한다
'4.모든 회원정보 출력'을 선택하면, 가입되어있는 모든 회원정보를 출력한다
'99.종료'를 선택하면, 프로그램을 종료한다

이후에, 특정 회원의 회원ID와 회원PW를 입력받아 인증되면 회원정보를 수정하는 기능을 구현할 것
"""

"""
가입하는 사람 입장에서

test case 1. 회원가입
최초 화면에 회원가입 옵션 선택.
id를 입력하세요 :
 - id가 중복된 아이디야 -> 다시 입력하세요 (3회)
 - id가 기존에 없던 아이디야 -> 회원가입
회원가입 -> pw, email, phone 입력하세요: 
데이터베이스에 저장.
화면출력 회원가입 완료.

test case 2. 로그인
최초 화면에서 로그인 옵션 선택.
id, pw를 입력하세요:
 - 틀렸을 때: (3회) 3번 다 틀리면 최초 화면으로.
 - 맞으면: 로그인 성공! ~님 환영합니다.
 
test case 3. 회원 정보 수정
최초 화면에서 회원정보 수정 선택.
id, pw 입력하세요:
 - 틀렸을 때: (3)

test case 4. 회원 정보 출력
최초 화면에서 회원 정보 출력.
id, pw를 입력하세요:
 - 틀렸을 때: 존재하지 않는 회원입니다. (5회)
 - 맞았을 때:
    1. 자기 계정 정보 목차랑 같이 출력
    2. 어떤 정보 수정할건지 선택
    3. 선택한 정보 새로 받아야함.
    4. 데이터베이스 수정
    5. 출력 완료.

test case 5. 전체 정보 출력

-----------------------

test case 6. 아이디 찾기 
test case 7. 비번 찾기
test case 8. 삭제

"""

import AccountManager
import AddAcount
import Login
import PrintAllAccount
import PrintAccount
import UpdateAccountInfo

SIGN_UP = "1"
SIGN_IN = "2"
UPDATE_USER = "3"
PRINT_USER = "4"
PRINT_ALL_USER = "5"
EXIT = "99"

LOOP_COUNT = 3


def display():
    print(
        "1. 회원가입 | 2. 로그인 | 3. 회원 정보 수정 | 4. 특정 회원 정보 출력 | 5. 모든 회원정보 출력 | 99. 종료"
    )


isRunning = True

while isRunning:
    display()
    selected = input("옵션을 선택하세요: ")

    if SIGN_UP == selected:
        AddAcount.addAccount()

    elif SIGN_IN == selected:
        Login.authN()

    elif UPDATE_USER == selected:
        UpdateAccountInfo.LoginMersin()

    elif PRINT_USER == selected:
        PrintAccount.printAccount()            

    elif PRINT_ALL_USER == selected:
        PrintAllAccount.startLoop()

    elif EXIT == selected:
        isRunning = False
        continue

    else:
        print("정상적인 옵션을 선택해주세요.")

    