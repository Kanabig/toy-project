# test case 4. 회원 정보 출력
# 최초 화면에서 회원 정보 출력.
# id, pw를 입력하세요:
#  - 틀렸을 때: 존재하지 않는 회원입니다. (5회)
#  - 맞았을 때:
#     1. 자기 계정 정보 목차랑 같이 출력
#     2. 어떤 정보 수정할건지 선택
#     3. 선택한 정보 새로 받아야함.
#     4. 데이터베이스 수정
#     5. 출력 완료.








import AccountManager as am
import PrintAllAccount as pa
from AccountManager import isValidAccount

am.accounts["parkjungho"] = {
    am.KEY_ID: "parkjungho", am.KEY_PW: "1", 
    am.KEY_EMAIL: "parkjungho@gmail.com", am.KEY_PHONE: "010-1111-1111"
}
am.accounts["Leeyoonho"] = {
    am.KEY_ID: "Leeyoonho", am.KEY_PW: "2", 
    am.KEY_EMAIL: "yunho@kakao.com", am.KEY_PHONE: "010-2222-2222"
}

accounts = am.accounts


CHANGE_PASS = 1
CHANGE_EMAIL = 2
CHANGE_NUM = 3

MENU_UPDATE = 1
MENU_EXIT = 2





def LoginMersin():
    stopStack = 0

    while True:
        userInputID = input('아이디를 입력하세요')
        userInputPW = input('비밀번호를 입력하세요')

        if am.isValidAccount(userInputID,userInputPW):
            print('로그인 성공')
            print("-" * 30)
            print('---- 개인정보 출력 ----')
            print("-" * 30)
            print(f'ID: {accounts[userInputID][am.KEY_ID]}')
            print(f'PW: {accounts[userInputID][am.KEY_PW]}')
            print(f'EMAIL: {accounts[userInputID][am.KEY_EMAIL]}')
            print(f'PHONENUMBER: {accounts[userInputID][am.KEY_PHONE]}')
            print("-" * 30)
        
            changeInfo = int(input('1.회원정보 수정       2.종료'))

            if changeInfo == MENU_UPDATE:
                print('어떤 정보를 수정 하시겠습니까?')
                choose = int(input('1.비밀번호      2.이메일        3.전화번호'))

                target_key = ""

                if choose == CHANGE_PASS:
                    newPw = input('새로운 비밀번호를 입력하세요')
                    accounts[userInputID][am.KEY_PW] = newPw   
                    target_key = am.KEY_PW

                elif choose == CHANGE_EMAIL:
                    newEmail = input('새로운 이메일을 입력하세요')
                    accounts[userInputID][am.KEY_EMAIL] = newEmail
                    target_key = am.KEY_EMAIL

                elif choose == CHANGE_NUM:
                    newNumber = input('새로운 번호를 입력하세요')
                    accounts[userInputID][am.KEY_PHONE] = newNumber
                    target_key = am.KEY_PHONE

                else:
                    print('잘못된 번호입니다.')
                    
                
                print(f'수정 완료 된 {target_key}: {accounts[userInputID][target_key]}')
               
                return True
            
            elif changeInfo == MENU_EXIT:
                print('프로그램을 종료합니다.')
                return True
        else:
            print('존재하지 않는 회원입니다.')
            stopStack += 1
            if stopStack >= 5:
                print('비밀번호 5회 이상 틀리셨습니다')
                print('시스템을 종료합니다')
                return False

LoginMersin()
    
