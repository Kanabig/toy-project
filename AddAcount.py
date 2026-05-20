import AccountManager as am


def createAccount():
    id = signUpCount()
    if id is None:
        return False

    pw = input('신규회원 PW입력: ')
    email = isValidEmail()
    phone = input('신규회원 Phone입력: ')
    addAccount(id, pw, email, phone)
    return True

def signUpCount():
    signUpCnt = 0
    while True:
        id = input('신규회원 ID입력: ')
        if isSameId(id):
            signUpCnt += 1
            print(f'ID 중복 초과까지 {signUpCnt}/3 입니다.')
            if signUpCnt >= 3:
                print('ID 중복 3회 초과로 메뉴로 돌아갑니다.')
                return None
            continue
        return id

def isValidEmail():
    email = input('신규회원 Email입력: ')
    while True:
        if '@' not in email:
            print('입력한 Email주소가 형식에 맞지 않습니다.')
            email = input('신규회원 Email입력: ')
        else:
            return email

def isSameId(id):
    if id in am.accounts:
        print('중복된 ID입니다. 다시 입력하세요.')
        return True
    return False
    
def addAccount(id, pw, email, phone):
    am.accounts[id] = {
        'pw': pw,
        'email': email,
        'phone':phone
    }
    print(f'{id}님 회원가입 되었습니다.')




'''
아이디 찾기o, 비밀번호 찾기o, 계정 삭제하기x

accounts = am.accounts

def twiceAuthenication(email, phone):
    for account in accounts.values():
        if email == account[am.KEY_EMAIL] and phone == account[am.KEY_PHONE]:
            return account
    return None

def findId(email, phone):
    account = twiceAuthenication(email, phone)
    if account:
        print(f'찾은 ID: {account[am.KEY_ID]}')
        return
    print('가입된 ID가 없습니다.')

def findPw(id, email, phone):
    if am.isExistsId(id):
        account = twiceAuthenication(email, phone)
        if account and account[am.KEY_ID] == id:
            print(f'찾은 PW: {account[am.KEY_PW]}')
            return
    print('PW를 찾지 못했습니다.')

findId('parkjungho20@gmail.com', '010-5520-0547')
findPw('parkjungho', 'parkjungho20@gmail.com', '010-5520-0547')
'''

