# Toy 프로젝트
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

KEY_ID = "ID"
KEY_PW = "PW"
KEY_EMAIL = "EMAIL"
KEY_PHONE = "PHONE"

DEBUG_MOD = True

accounts = {}


# ID 비교
def isExistsId(id):
    return id in accounts


# PW 비교
def isValidAccount(id, pw):
    if isExistsId(id):
        if pw == accounts[id][KEY_PW]:
            return True

    return False
    # 계정이 유효하면 return True
    # 계정이 유효하지 않으면 return False


def createAccount(id, pw, email, phone):
    accounts[id] = {
        KEY_ID: id,
        KEY_PW: pw,
        KEY_EMAIL: email,
        KEY_PHONE: phone
    }



if DEBUG_MOD:

    def createDummy():
        createAccount("parkjungho", "1", "parkjungho@gmail.com", "010-1111-1111")
        createAccount("Leeyoonho", "2", "yunho@kakao.com", "010-2222-2222")
        createAccount("LeeGyuchan", "3", "gyuchandasd@daum.net", "010-3333-3333")
        createAccount("KimTaeJoon", "4", "taejoon@naver.com", "010-4444-4444")
        createAccount("jangdongeun", "5", "dongeun@nate.com", "010-5555-5555")

    createDummy()
