'''
id, pw를 입력하세요:
 - 틀렸을 때: (3회) 3번 다 틀리면 최초 화면으로.
 - 맞으면: 로그인 성공! ~님 환영합니다.
'''
import AccountManager as am

def authN():
    for attempt in range(3):
        uid = input('ID 입력: ').strip()
        upw = input('PW 입력: ').strip()

        if uid in am.accounts and am.accounts[uid]['PW'] == upw:
            print(f'로그인 성공! {uid}님 환영합니다.')
            return True
        else:
            print('id 혹은 비밀번호가 일치하지 않습니다.')
    print('3회 이상 틀리셨습니다.')
    print('처음으로 돌아갑니다.')
    return False





# # print('-' * 30)

# # #아이디 찾기

# accounts = am.accounts

# def doubleAuth (email):
#     for account in account.value():
#         if email == [am.account.key]:
#             return account
#     return

# # accounts = {
#     # id : {
#     #     KEY_ID: id,
#     #     KEY_PW: pw,
#     #     KEY_EMAIL: email,
#     #     KEY_PHONE: phone
#     # }
#     # id2 : {
#     #     KEY_ID: id,
#     #     KEY_PW: pw,
#     #     KEY_EMAIL: email,
#     #     KEY_PHONE: phone
#     # }
# # }


# def findId (id, phone):
#     for info in accounts.values():

#         if info[am.KEY_ID] == id and info[am.KEY_PHONE] == phone:
#             print(f"아이디: {info[am.KEY_ID]}")

# #비밀번호 찾기
# def doubleAuth (email):
#     for account in account.value():
#         if email == [am.account.key]:
#             return account
#     return

# def findPw (id, phone):
#     for info in accounts.values():

#         if info[am.KEY_ID] == id and info[am.KEY_PHONE] == phone:
#             print(f"비밀번호: {info[am.KEY_PW]}")
        

# findId(id, phone)