![header](https://capsule-render.vercel.app/api?type=waving&color=auto&height=200&section=header&text=Game%20Buddy%20Bot&fontSize=32)
======================
## 프로젝트 개발자
| 학과         | 학번     | 이름   |
| ------------ | -------- | ----- |
| 컴퓨터공학과 | 20101252 | 심지섭 |

- 개인 프로젝트로 진행

## 프로젝트 설명
친구들과 게임을 플레이할 때 유용한 기능을 모아놓은 디스코드 봇 입니다.   
항상 게임을 하면서 항상 사다리타기, 투표 등등 게임에 필요한 기능들을 번거롭게 찾아가면서 했나요?   
이제는 디스코드에서 명령어 하나로 바로 만나보세요!   

**이런 분께 GameBuddyBot을 추천해요!**
- 매번 사다리타기, 투표 등등 검색하기 귀찮으신 분!
- 게임 친구가 많아서 팀을 자주나누고, 투표를 자주 하시는 분!
- 디스코드 서버가 허전해서 서버에 초대할 친구를 찾으시는 분!
- 게임 친구가 없어서 외로우신 분!
- 딱딱한 말투의 봇에 질리신 분!

**제가 도와드리겠습니다**   
<img src="https://drive.google.com/uc?id=1j0EFLE3MKqKgtwfllLbj5GwetKofquZC"/>

## 프로젝트 실행 방법

**소스코드로 봇 실행**
1. git clone 하여 로컬 레포지토리로 들여온다.
2. token.txt 파일을 main.py와 같은 위치에 넣는다.
(token.txt는 과제 제출란에 첨부했습니다.)
3. main.py를 실행한다.

**초대 링크로 실행**
- 본인 서버에 아래 링크를 통해 봇을 초대할 수 있습니다.
- [초대 링크](https://discord.com/api/oauth2/authorize?client_id=1177902716387852381&permissions=8&scope=bot)
- '서버에 추가' 에서 봇을 추가하려는 서버를 선택 후 계속하기
- 승인!   
**꼭! 봇이 관리자 권한을 사용할 수 있게 해주어야합니다!**

*GameBuddyBot은 repl.it과 UptimeRobot에 의해 배포되어 24시간 구동되고 있습니다.*   
**혹시 오프라인이라면 소스코드로 봇을 실행해주세요.**   
**두 방법 전부 실행이 안된다면 jisub5322@naver.com으로 연락 주시기 바랍니다.**   

## 구현 기능
1. **명령어 설명** : GameBuddyBot의 기능을 사용하기 위한 명령어를 설명해줍니다.
2. **인사하기** : GameBuddyBot과 인사합니다.
3. **사다리타기** : 게임 순서나 역할(포지션) 등을 결정하기 위해 무작위로 사다리타기를 진행합니다.
4. **투표** : 어떤 게임을 할지, 어떤 규칙을 적용할지 등 사용자들이 투표할 수 있습니다.
6. **랜덤 선택** : 여러가지 중 하나를 무작위로 선택해줍니다.
7. **대화하기** : GameBuddyBot과 대화합니다. (openAI assistant API 사용)
8. **기억초기화** : GameBuddyBot이 지금까지 한 대화 내용을 잊어버립니다.
9. **신규 게임 추천(STEAM)** : STEAM의 신규 게임 중 10개를 보여줍니다.
10. **할인 게임 추천(STEAM)** : STEAM의 할인 게임 중 10개를 보여줍니다.

- '!명령어' 혹은 '!명령어 ~~~~~'의 형태로 입력하면 GameBuddyBot이 응답합니다.

## 기타 정보
> discord API와 openAI assistant API를 사용하여 제작되었습니다.

> 개발에 사용된 ai 모델은 gpt-3.5-turbo-1106 입니다.

> GameBuddyBot은 repl.it과 UptimeRobot에 의해 배포되어 24시간 구동되고 있습니다.

## 참고 자료
- [유튜브 : 섹시베이비](https://www.youtube.com/@user-mh7ib3xc9c)   
'''
투표, 사다리타기, 랜덤 선택 기능을 구현하는데 참고했습니다.
'''
- [유튜브 : 프로그래머 김플 스튜디오](https://www.youtube.com/watch?v=kKhWkG5Di5s)   
'''
OpenAI Assistants API 사용법을 배우고, 구현에 참고했습니다.
'''
- [네이버 블로그 : 코코블루](https://blog.naver.com/PostView.naver?blogId=6116949&logNo=221949748751&redirect=Dlog&widgetTypeCall=true&directAccess=false)   
'''
서버에 멤버가 들어왔을 때와 나갔을 때 수행 될 이벤트를 구현하기 위해 코드를 거의 동일하게 적용했습니다.
'''
- [velog : seulki971227](https://velog.io/@seulki971227/%ED%8C%8C%EC%9D%B4%EC%8D%AC%ED%81%AC%EB%A1%A4%EB%A7%81-%EC%8A%A4%ED%8C%80%ED%99%88%ED%8E%98%EC%9D%B4%EC%A7%80-%ED%81%AC%EB%A1%A4%EB%A7%811)   
'''
스팀 홈페이지 크롤링을 할 때 많은 도움이 되었고, 참고하였습니다.
'''
- [GitHub Gist : ihoneymon/how-to-write-by-markdown.md](https://gist.github.com/ihoneymon/652be052a0727ad59601)   
'''
README 파일 작성에 참고 하였습니다.
'''
- [GitHub : NyaNyak/discord-beebot](https://github.com/NyaNyak/discord-beebot)   
'''
README 파일 작성 방식을 참고했고, 아이디어를 생각해내는데 도움이 되었습니다.
'''
- **디스코드 서버 "Korean Discord Dictionary (KDD)"의 BOT:개발강의로 공부하고 개발한 프로젝트입니다.**

## 프로젝트를 하며 얻은 것
- 파이썬 개발 경험
- Discord Bot API, OpenAI Assistants API의 사용법 학습 및 적용
- 웹 크롤링 학습 및 적용
- github 사용 경험

감사합니다.