<div align="center"><img src="https://image.rocketpunch.com/company/79452/beeorobotigseukoria_logo_1591678224.png?s=400x400&t=inside" alt="erd"/></div>

# 목차

- [Bearrobotics 기업과제](#Bearrobotics_기업과제)
- [과제 해석](#과제-해석)
- [구현 요구사항](#구현-요구사항)
- [구현](#구현)


## 과제 해석
Insert Card => PIN number => Select Account => See Balance/Deposit/Withdraw
위 부문을 통해서 atm기에 카드를 넣고 핀번호(비밀번호)를 입력했을 때 카드와 연결되어 있는 계좌의 잔액 조회 및 입출금 기능을 구현 하는 것으로 이해하였습니다.


## 구현 요구사항
- [x] atm 기에 카드를 넣기 전 계좌를 생성해야 한다고 이해하였습니다.
    - 계좌 등록, 조회, 삭제 api 작성


- [x] 계좌를 만든 후 해당 카드를 특정 계좌에 연결해야 한다고 이해하였습니다.
    - 카드 등록, 조회, 삭제 api 작성

## 구현

### 기술 스택
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/> <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=white"/> <img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=SQLite&logoColor=white"/> <img src="https://img.shields.io/badge/PyCharm-000000?style=flat-square&logo=PyCharm&logoColor=white"/> <img src="https://img.shields.io/badge/VSCode-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=white"/>

### 개발 기간
- 2022.06.16 - 2022.06.17

> ### ERD
![my_project](https://user-images.githubusercontent.com/67543838/174279374-c3886f4c-2fa6-48d1-ad6f-aac404f29450.png)


### Step to run
```
$ python -m venv venv
$ source venv/Scripts/activate
$ python install -r requirements.txt
$ python manage.py runserver
```


### 인증 테스트 방법
- [x] http://127.0.0.1:8000/api/accounts/ 
  - 해당 주소에서 계좌 생성하기 -> POST 버튼만 누르면 계좌를 생성할 수 있습니다.
 
  ![image](https://user-images.githubusercontent.com/67543838/174281897-b4dd07db-c908-49ca-b649-410ca117d895.png)
  ![image](https://user-images.githubusercontent.com/67543838/174294348-a21f702a-4671-4010-88f0-b079dccba116.png)


- [x] http://127.0.0.1:8000/api/cards/
  - 해당 주소로 가서 카드 생성하기 -> 카드 생성시에는 계좌번호를 입력해야 하는 특성상 입력 포맷이 존재합니다.
- [x] 카드 생성시 입력 형태 
  - { "account_number": "11111111111111", "pin_number": "000000"}
  - 계좌번호는 생성한 14자리 문자열 형태, 핀번호는 6자리를 문자열 형태로 넣어 카드를 생성합니다.
  
  ![image](https://user-images.githubusercontent.com/67543838/174294905-4c56f2a6-ec59-4d86-8877-65ed2eccf8f0.png)
  ![image](https://user-images.githubusercontent.com/67543838/174295000-52fa31c1-3c58-4874-9a0a-609c92c46426.png)


- [x] 잔액 조회 및 입출금 테스트
  - 테스트 파일은 루트 디렉토리에 있는 atm.py에서 테스트 하실 수 있습니다. 
  - 계좌 및 카드 개설 후 잔액은 0에서 테스트가 진행됩니다. 
- [x] 잔액 조회 및 입출금 테스트
  - current_balance(card_number, pin_number)
    인자로 생성했던 카드 번호와 핀번호를 입력하면 현재 계좌의 잔액을 return 합니다.
    
    current_balance(1050109435305481, "000000") // 현재 잔액은 0입니다.
    
  - deposit(card_number, pin_number, price)
    인자로 카드번호, 핀번호, 입금금액을 입력하면 계좌에 입금 됩니다.
    
    deposit(1050109435305481, "000000", 10000) // 금액: 10000이 입금되었습니다. 현재 잔액은 10000입니다.
    
  - withdraw(card_number, pin_number, price)
    인자로 카드번호, 핀번호, 출금 금액을 입력하면 계좌에서 출금 됩니다.
    
    withdraw(1050109435305481, "000000", 10000) // 금액: 10000이 인출 되었습니다. 현재 잔액은 0입니다.
    
    
    
