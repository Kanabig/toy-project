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
from AccountManager import isValidAccount


accounts = am.accounts
flag = True




def LoginMersin():
    stopSteck = 0
    while flag:
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
            print(f'PHONENUMBER: {accounts[userInputID][am.KEY_PHONENUMBER]}')
            
            return True
        else:
            print('존재하지 않는 회원입니다.')
            stopSteck += 1
            if stopSteck >= 5:
                print('비밀번호 5회 이상 틀리셨습니다')
                print('시스템을 종료합니다')
                return False

LoginMersin()
    
        
        
    
