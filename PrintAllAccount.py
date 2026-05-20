"""
생각나는 기능
test case1: 페이지로 보기
test case2: 이름순 정렬
test case3: 특정 이메일 주소로 정렬
"""

# AccountManager가 너무 길어서 별명 지어주기.
import AccountManager as am

# AccountManager에서 글로별 변수(레퍼런스 타입) accounts 가져오기
accounts = am.accounts

DEBUG_MOD = False


# --- 내가 맞은 기능
def printAll():
    for account in accounts.values():
        print("-" * 30)
        print(f"ID{":":>4} {account[am.KEY_ID]}")
        print(f"PW{":":>4} {account[am.KEY_PW]}")
        print(f"EMAIL: {account[am.KEY_EMAIL]}")
        print(f"PHONE: {account[am.KEY_PHONE]}")
        print("-" * 30)


def startLoop():
    printAll()


# --- 숙제
def phoneAuthentication(phone):
    for account in accounts.values():
        if phone == account[am.KEY_PHONE]:
            return account

    return None


def findId(phone):
    account = phoneAuthentication(phone)

    if account:
        print(f"찾은 아이디: {account[am.KEY_ID]}")
        return

    print("가입된 아이디가 없습니다.")


def findPw(id, phone):
    if am.isExistsId(id):
        account = phoneAuthentication(phone)
        if account:
            print(f"찾은 비번: {account[am.KEY_PW]}")
            return

    print("비밀번호를 찾지 못했습니다.")


# --- 테스트용 코드
if DEBUG_MOD:

    def createAccount(id, pw, email, phone):
        accounts[id] = {
            am.KEY_ID: id,
            am.KEY_PW: pw,
            am.KEY_EMAIL: email,
            am.KEY_PHONE: phone,
        }

    def createDummy():
        createAccount("parkjungho", "1", "parkjungho@gmail.com", "010-1111-1111")
        createAccount("Leeyoonho", "2", "yunho@kakao.com", "010-2222-2222")
        createAccount("LeeGyuchan", "3", "gyuchandasd@daum.net", "010-3333-3333")
        createAccount("KimTaeJoon", "4", "taejoon@naver.com", "010-4444-4444")
        createAccount("jangdongeun", "5", "dongeun@nate.com", "010-5555-5555")

    # 이 파일이 main으로 실행되었을 때 True
    # main으로 실행: 이 파일(PrintAllAcount)이 ctrl+F5로 직접 실행되었을 때.
    if __name__ == "__main__":
        # Print 테스트
        createDummy()
        printAll()

        # findId 테스트
        findId("010-4444-4444")
        findId("1")

        print("-" * 30)

        # --- findPw 테스트
        findPw("Leeyoonho", "010-2222-2222")
        findPw("1", "010-2222-2222")
        findPw("Leeyoonho", "1")
