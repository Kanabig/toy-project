#특정 인원 출력
#일단은 아이디랑 비번 입력 -> 맞으면 회원 정보 출력
#혹시 실패시 출력 실패

import AccountManager     # 아이디 비번을 찾기를 위한 기본틀 넣기

LOOP_COUNT = 3        # 일단 3회 까지만 생각중


def printAccount():         # 회원출력 함수 적용

    count = 0                  # 기본값 0을 넣었음

    while count < LOOP_COUNT:    # 일단 최대 3회로 했지만 바뀔수도 있음

        id = input("회원 ID 입력: ")
        pw = input("회원 PW 입력: ")

        if AccountManager.isValidAccount(id, pw):

            print("\n로그인 성공! 회원 정보를 출력합니다.\n")

            user = AccountManager.accounts[id]

            print("\n===== 회원 정보 =====")
            print(f"ID : {user[AccountManager.KEY_ID]}")
            print(f"Email : {user[AccountManager.KEY_EMAIL]}")
            print(f"Phone : {user[AccountManager.KEY_PHONE]}")
            print("=====================\n")

            return           # 출력하면 끝나게 하려고 넣음

        else:
            count += 1                 # 기본값 0에 실패시 올라갈예정
            print(f"존재하지 않는 회원입니다. ({count}/{LOOP_COUNT})")

    print("계정 3회 실패하셨습니다. 메인메뉴로 이동합니다. ")