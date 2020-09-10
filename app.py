'''

FastSelfCheck(KR_SCHOOL) - Python
Copyright 2020 Dohyun Park(dhlife09) All Rights Reserved.

https://github.com/dhlife09

새로 통합된 자가진단 사이트(hcs.eduro.go.kr)에서 사용할 수 있습니다.

'''
##### ===============[ YOU_SHOULD_AGREE_TERMS ]=============== #####
#
# 본 프로그램은 파이썬-Selenium을 사용한 자가진단 사이트(hcs.eduro.go.kr) 단순화 프로그램 입니다.
# 프로그램을 사용하기 위해서는 해당 규칙을 읽고 동의하셔야 합니다.
#
# 반드시 코로나 19 증상이 있는 경우에는 본 프로그램을 사용하지 말고 직접 코로나19 자가진단에 참여해야 합니다.
# 또한 해당 프로그램의 사용으로 발생한 문제에 대해서는 책임지지 않습니다.
#
# 프로그램 사용 전, pip install -r requirements.txt 명령어를 통해 selenium 모듈을 설치해 주세요.
# Chrome 브라우저 85버전(chrome://version)이 설치되어 있어야 합니다.

agreeTerms = False  # 위 규칙을 읽고 동의하신다면, False 를 True 로 변경해 주세요.


##### ===============[ YOU_SHOULD_EDIT_HERE ]=============== #####

waitingTime = 1 # 서버의 응답을 기다리기 위한 시간입니다. 인터넷 상태 및 사용자 설정에 따라 조절해 주시면 됩니다. 굳이 변경할 필요는 없습니다. (Default: 1)

eduOffice = '시도명을_입력해주세요'    # 자가진단 사이트에 있는 시/도명을 입력해주세요.
eduOffLvl = '학교급을_입력해주세요'   # 학교급을 입력해주세요 (유치원/초등학교/중학교/고등학교/특수학교)
stdntName = '이름을_입력해주세요'    # 이름을 입력해주세요.
stdntBirt = '생년월일_6자리를_입력해주세요' # 입력 예시: 200909 -> 2020년 09월 09일
stdntSchn = '학교명을_정확히_입력해주세요'   # 학교명을 정확히 입력해주세요. 정확하게 입력하지 않을 경우 오류가 발생할 수 있습니다.
stdntPass = '자가진단_비밀번호_4자리를_입력해주세요' # hcs.eduro.go.kr 사이트에 로그인하는 비밀번호 4자리를 입력하세요. 반드시 비밀번호가 생성되어있어야 합니다.
showstdntPass = False    #콘솔창에서 비밀번호를 표시합니다. (Default: False)


##### ===============[ Option: Send Result to Mail ]=============== #####

useSMTPresult = False # 자가진단을 완료한 후 결과를 사용자에게 메일로 전달하는 옵션입니다. (Default: False)

senderEmailAddress = 'SMTP아이디를 입력하세요'      # SMTP 계정 아이디 입력
senderEmailPasswd = 'SMTP PW을 입력하세요'      # SMTP 계정 암호 입력
receiveEmailAddress = '수신할 주소를 입력하세요'         # 수신할 주소

smtpSVadd = 'smtp.gmail.com'    # SMTP 서버의 주소를 입력하세요 (Default: Gmail)
smtpSVport = 587    # SMTP 서버의 포트를 입력하세요 (Default: Gmail)


##### ===============[ DO_NOT_EDIT_HERE_ ]=============== #####
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time

def vError(WhyError):
    print('')
    print(' [자가진단] ' + WhyError + ' 설정 에러가 발생했습니다. hcs.eduro.go.kr 사이트에 있는 ' + WhyError + '의 정확한 값을 기입하시기 바랍니다.' )
    print(' [자가진단] 프로그램이 5초 뒤 종료됩니다.')
    time.sleep(5)
    exit()

print('''

 ##### ===============[ FastSelfCheck(KR_SCHOOL) by dhlife09 ]=============== #####
 
 Notes: 코로나19 증상이 있는 경우 반드시 직접 체크하시기 바랍니다. 해당 프로그램의 사용으로 발생한 문제는 책임지지 않습니다.
''')    

# 유효성 검사 시작
if agreeTerms == False:
    print('')
    print(' [자가진단] 약관에 동의하지 않으셨습니다. 약관에 동의 후 다시 실행해주세요.' )
    print(' [자가진단] 프로그램이 5초 뒤 종료됩니다.')
    time.sleep(5)
    exit()
if eduOffice == '서울특별시':
    eduOfficeCode = '01'
    print(' [자가진단] 시/도 설정: 서울특별시')
elif eduOffice == '부산광역시':
    eduOfficeCode = '02'
    print(' [자가진단] 시/도 설정: 부산광역시')
elif eduOffice == '대구광역시':
    eduOfficeCode = '03'
    print(' [자가진단] 시/도 설정: 대구광역시')
elif eduOffice == '인천광역시':
    eduOfficeCode = '04'
    print(' [자가진단] 시/도 설정: 인천광역시')
elif eduOffice == '광주광역시':
    eduOfficeCode = '05'
    print(' [자가진단] 시/도 설정: 광주광역시')
elif eduOffice == '대전광역시':
    eduOfficeCode = '06'
    print(' [자가진단] 시/도 설정: 대전광역시')
elif eduOffice == '울산광역시':
    eduOfficeCode = '07'
    print(' [자가진단] 시/도 설정: 울산광역시')
elif eduOffice == '세종특별자치시':
    eduOfficeCode = '08'
    print(' [자가진단] 시/도 설정: 세종특별자치시')
elif eduOffice == '경기도':
    eduOfficeCode = '10'
    print(' [자가진단] 시/도 설정: 경기도')
elif eduOffice == '강원도':
    eduOfficeCode = '11'
    print(' [자가진단] 시/도 설정: 강원도')
elif eduOffice == '충청북도':
    eduOfficeCode = '12'
    print(' [자가진단] 시/도 설정: 충청북도')
elif eduOffice == '충청남도':
    eduOfficeCode = '13'
    print(' [자가진단] 시/도 설정: 충청남도')
elif eduOffice == '전라북도':
    eduOfficeCode = '14'
    print(' [자가진단] 시/도 설정: 전라북도')
elif eduOffice == '전라남도':
    eduOfficeCode = '15'
    print(' [자가진단] 시/도 설정: 전라남도')
elif eduOffice == '경상북도':
    eduOfficeCode = '16'
    print(' [자가진단] 시/도 설정: 경상북도')
elif eduOffice == '경상남도':
    eduOfficeCode = '17'
    print(' [자가진단] 시/도 설정: 경상남도')
elif eduOffice == '제주특별자치도':
    eduOfficeCode = '18'
    print(' [자가진단] 시/도 설정: 제주특별자치도')
else:
    vError("시/도")   # 에러 발생 !

if eduOffLvl == '유치원':
    print(' [자가진단] 학교급 설정: 유치원')
    eduOffLvlCode = '1'
elif eduOffLvl == '초등학교':
    print(' [자가진단] 학교급 설정: 초등학교')
    eduOffLvlCode = '2'
elif eduOffLvl == '중학교':
    print(' [자가진단] 학교급 설정: 중학교')
    eduOffLvlCode = '3'
elif eduOffLvl == '고등학교':
    print(' [자가진단] 학교급 설정: 고등학교')
    eduOffLvlCode = '4'
elif eduOffLvl == '특수학교':
    print(' [자가진단] 학교급 설정: 특수학교')
    eduOffLvlCode = '5'
else:
    vError("학교급")   #에러 발생 !

if stdntName == '이름을_입력해주세요' or None:
    vError("이름")    #에러 발생 !
else:
    print(' [자가진단] 이름 설정: ' + stdntName)
    
if stdntBirt == '생년월일_6자리를_입력해주세요' or None:
    vError("생년월일(6자리)")    #에러 발생 !
else:
    print(' [자가진단] 생년월일(6자리) 설정: ' + stdntBirt)

if stdntSchn == '학교명을_정확히_입력해주세요' or None:
    vError("학교명")    #에러 발생 !
else:
    print(' [자가진단] 학교명 설정: ' + stdntSchn)

if stdntPass == '자가진단_비밀번호_4자리를_입력해주세요' or None:
    vError("비밀번호")    #에러 발생 !
else:
    if showstdntPass == True:
        print(' [자가진단] 비밀번호 설정: ' + stdntPass)
    elif showstdntPass == False:
        print(' [자가진단] 비밀번호 설정: ****')  # showstdntPass Options이 False인 경우, 표시하지 않음
    else:
        vError("showstdntPass 옵션(비밀번호 표시")  #에러 발생 !
        
if useSMTPresult == True:
    if senderEmailAddress != None and senderEmailPasswd != None and receiveEmailAddress != None:
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        from email.mime.base import MIMEBase
        from email import encoders
        from datetime import datetime
        print(' [자가진단] SMTP 메뉴가 활성화 되었습니다.')

        # 제목 입력
        subject = datetime.today().strftime("[자가진단] %Y-%m-%d %H:%M:%S " + stdntName + " 완료") 

        msg = MIMEMultipart()
        msg['From'] = senderEmailAddress
        msg['To'] = receiveEmailAddress
        msg['Subject'] = subject

        # 본문 내용 입력
        body = '\n' + stdntName + ' (' + stdntSchn + ''')
코로나19 자가진단(무증상)이 완료되었습니다.

코로나19 증상이 있는 경우에는 자가진단 홈페이지(https://hcs.eduro.go.kr)에서 수동으로 자가진단을 진행하시기 바라며, 본 프로그램에 대해 제작자는 책임을 지지 않습니다.



FastSelfCheck(KR_SCHOOL) by dhlife09(https://github.com/dhlife09)
    '''
        msg.attach(MIMEText(body,'plain'))
        text = msg.as_string()
        server = smtplib.SMTP(smtpSVadd, smtpSVport)
        server.starttls()
    else:
        vError('SMTP')



print(' [자가진단] 유효성 검사가 완료되었습니다. 자가진단(무증상)을 시작합니다.')

driver = webdriver.Chrome()
print('')
print(' [자가진단] Chrome Webdriver 로 실행됩니다.')
driver.get("https://hcs.eduro.go.kr/#/loginHome")   
print(' [자가진단] 자가진단 웹페이지가 열렸습니다.')
elem = driver.find_element_by_id("btnConfirm2") #자가진단 참여버튼
elem.click()
print(' [자가진단] 자가진단 참여버튼을 클릭합니다.')
elem = driver.find_element_by_xpath("//input[@class='input_text_common input_text_search']")    #학교검색
elem.click()
print(' [자가진단] 학교 데이터를 검색합니다.')
elem = driver.find_element_by_xpath("//select['data-v-f6ebec28 name id']/option[@value='" + eduOfficeCode + "']")  #시/도 설정 메뉴 * 반드시 코드 사용할 것 *
elem.click()
elem = driver.find_element_by_xpath("//select['data-v-f6ebec28']/option[@value='" + eduOffLvlCode + "']")  #학교급 설정 메뉴 * 반드시 코드 사용할 것 *
elem.click()
elem = driver.find_element_by_xpath("//input[@class='searchArea']")  #학교검색메뉴
elem.click()
elem.send_keys(stdntSchn)
elem.send_keys(Keys.ENTER)
time.sleep(waitingTime)
elem = driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul')
elem.click() #학교선택
elem = driver.find_element_by_class_name("layerFullBtn").click() #학교선택 버튼클릭(하단)
print(' [자가진단] 학교를 선택합니다.')
time.sleep(waitingTime)
print(' [자가진단] 신상 정보를 입력합니다.')
time.sleep(waitingTime)
elem = driver.find_element_by_xpath("//input[@class='input_text_common']")  #이름??
elem.click()
elem.send_keys(stdntName)
elem = driver.find_element_by_xpath("//input[@inputmode='numeric']")  #생년월일
elem.send_keys(stdntBirt)
elem = driver.find_element_by_xpath("//input[@id='btnConfirm']")  #신상정보제출
elem.click()
print(' [자가진단] 신상 정보 입력을 완료했습니다.')
time.sleep(waitingTime)
print(' [자가진단] 비밀번호를 통해 사용자 인증을 시도합니다.')
time.sleep(waitingTime)
elem = driver.find_element_by_xpath("//input[@class='input_text_common']")  #비밀번호입력폼
elem.send_keys(stdntPass)
elem = driver.find_element_by_xpath("//input[@id='btnConfirm']")  #비밀번호제출
elem.click()
print(' [자가진단] 비밀번호를 통해 사용자 인증을 완료했습니다.')
time.sleep(waitingTime)
print(' [자가진단] ' + stdntName + ' (' + stdntSchn + ') 자가진단(무증상)을 시작합니다.')

# 무증상 자가진단 시작

elem = driver.find_element_by_xpath("//*[@id='container']/div[2]/section[2]/div[2]/ul/li[1]/a/span[1]")  # 뭐였더라 ?
elem.click()
time.sleep(waitingTime)
elem = driver.find_element_by_xpath("//*[@id='container']/div[2]/div/div[2]/div[2]/dl[1]/dd/ul/li[1]/label")  # 무증상체크
elem.click()
elem = driver.find_element_by_xpath("//*[@id='container']/div[2]/div/div[2]/div[2]/dl[2]/dd/ul/li[1]/label")  # 무증상체크
elem.click()
elem = driver.find_element_by_xpath("//*[@id='container']/div[2]/div/div[2]/div[2]/dl[3]/dd/ul/li[1]/label")  # 무증상체크
elem.click()
elem = driver.find_element_by_xpath("//*[@id='container']/div[2]/div/div[2]/div[2]/dl[4]/dd/ul/li[1]/label")  # 무증상체크
elem.click()
elem = driver.find_element_by_xpath("//*[@id='container']/div[2]/div/div[2]/div[2]/dl[5]/dd/ul/li[1]/label")  # 무증상체크
elem.click()
elem = driver.find_element_by_xpath("//input[@id='btnConfirm']")  #학교검색메뉴
elem.click()

print(' [자가진단] ' + stdntName + ' (' + stdntSchn + ') 자가진단(무증상)을 완료했습니다.')
time.sleep(1)
print(' [자가진단] 브라우저를 종료합니다.')
driver.close()

if useSMTPresult == True:
    server.login(senderEmailAddress,senderEmailPasswd)
    server.sendmail(senderEmailAddress,receiveEmailAddress,text)
    server.quit()
    print(' [자가진단] ' + receiveEmailAddress + ' 메일 주소로 완료 메일을 발송했습니다.')
    
time.sleep(5)
