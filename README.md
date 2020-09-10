# FastSelfCheck

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

본 프로그램은 파이썬-Selenium을 사용한 자가진단 사이트(hcs.eduro.go.kr) 자동화(무증상완료) 프로그램 입니다.

Chrome v85 기반으로 제작되었으며, 자가진단 완료 후 자동으로 창을 닫고 사용자에게 자가진단 완료 알림 메일을 보낼 수 있습니다. (메일전송 기능은 38번 째 줄 설정 필요)

- [Chrome 설치하기](https://www.google.com/intl/ko/chrome/)
- [Chrome Driver 다운로드(기본: 85.0.4183.87 내장)](https://chromedriver.chromium.org/downloads)
- [설치되어있는 Chrome 버전 확인하기(Chromium 브라우저일 경우에만 작동 - chrome://version )](chrome://version)

프로그램을 사용하기 위해서는 규칙을 읽고 동의하셔야 합니다.

**반드시 코로나 19 증상이 있는 경우에는 본 프로그램을 사용하지 말고 직접 코로나19 자가진단에 참여해야 합니다.**

해당 프로그램은 빠르게 만들어져 예외 처리가 되어있지 않습니다. 비밀번호 설정이 되어있지 않거나(사전에 먼저 비밀번호를 설정하셔야 합니다.), 너무 빨라서(app.py 파일의 27번 째 줄을 1보다 큰 값으로 올려보세요.) 오류가 날 수 있습니다. 또한, 해당 프로그램의 사용으로 발생한 문제에 대해서는 책임지지 않습니다.

## How to Install?
1. 먼저 해당 Repository 를 내려받으세요.
2. pip install -r requirements.txt 명령어를 통해 selenium 모듈을 설치해 주세요.
3. app.py 파일의 11번 째 줄 부터 규칙을 읽고 동의해주세요.
4. 25번째 줄부터 개인 정보를 입력해주세요. (정확히 입력해야 합니다.)
5. 메일 알림 기능을 사용하는 경우 38번 째 줄부터 SMTP 설정을 해주세요. (사용하지 않으시는 경우, 건너뛰시면 됩니다.)

## How to Use?
1. 아래의 내용으로 배치 파일(.bat)을 만들어 주세요. ( app.py는 자가진단 프로그램의 이름으로 설정해 주시고, 여러명의 자가진단을 진행하는 경우에는 app.py 파일을 복사해서 이름만 다르게 설정하고 배치 파일에 추가해 주면 됩니다.

	#1명만 자가진단하는 경우 예시:
	
    @echo off
    python app.py
    exit

	#2명 이상의 자가진단 하는 경우 예시:

    @echo off
    python app.py
    exit

2. 배치파일을 실행하면 자가진단이 완료됩니다.

