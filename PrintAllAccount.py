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

PRINT_ALL = "1"
PRINT_PAGE = "2"
EXIT_LOOP = "3"

PAGE_PRINT_COUNT = 3


def printAccount(account):
    print("-" * 30)
    print(f"ID{":":>4} {account[am.KEY_ID]}")
    print(f"PW{":":>4} {account[am.KEY_PW]}")
    print(f"EMAIL: {account[am.KEY_EMAIL]}")
    print(f"PHONE: {account[am.KEY_PHONE]}")
    print("-" * 30)


# --- 내가 맞은 기능
def printAll():
    for account in accounts.values():
        printAccount(account)


def printPage():

    onPrinting = True

    accountList = list(accounts.values())
    print(accountList)
    indexOffset = 0
    index = 0
    currentPage = 0

    while onPrinting:
        while index < indexOffset + PAGE_PRINT_COUNT:

            if index >= len(accountList):
                onPrinting = False
                break

            printAccount(accountList[index])
            index += 1

        indexOffset += PAGE_PRINT_COUNT
        index = indexOffset
        currentPage += 1

        print("-" * 30, f"page: {currentPage}")
        input("계속하려면 아무 키나 입력하세요.")


def printDisplay():
    print("1. 전체 보기 | 2. 페이지로 보기 | 3. 처음 화면으로 돌아가기")


def startLoop():
    onSelecting = True

    while onSelecting:
        printDisplay()
        selected = input("옵션을 선택하세요: ")

        if PRINT_ALL == selected:
            printAll()

        elif PRINT_PAGE == selected:
            printPage()

        elif EXIT_LOOP == selected:
            onSelecting = False

        else:
            print("정상적인 옵션을 선택해주세요.")


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
    # 이 파일이 main으로 실행되었을 때 True
    # main으로 실행: 이 파일(PrintAllAcount)이 ctrl+F5로 직접 실행되었을 때.
    if __name__ == "__main__":
        # Print 테스트
        am.createDummy()

        printAll()

        # Print Page 테스트
        printPage()

        # findId 테스트
        findId("010-4444-4444")
        findId("1")

        print("-" * 30)

        # --- findPw 테스트
        findPw("Leeyoonho", "010-2222-2222")
        findPw("1", "010-2222-2222")
        findPw("Leeyoonho", "1")
