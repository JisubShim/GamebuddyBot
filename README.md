# Game Buddy Bot

## 프로젝트 개발자🧑‍💻
| 학과         | 학번     | 이름   |
| ------------ | -------- | ----- |
| 컴퓨터공학과 | 20101252 | 심지섭 |

- 개인 프로젝트로 진행

## 프롤로그🎬
서울 어느 대학교 기숙사에서, 게임에 열정을 가진 젊은 개발자가 살고 있었습니다. 이 개발자는 매일 게임 속 세계에서 친구들과 함께하는 시간을 손꼽아 기다렸습니다. 그러나 그들은 항상 게임을 선택하는 것에 큰 어려움을 겪었습니다. 어떤 게임을 할지, 어떤 전략을 쓸지에 대한 끊임없는 토론이 이어졌죠.

어느때와 다름없이 그의 노트북 화면 앞에 앉아 있던 어느 날 밤, 그는 갑자기 영감을 받았습니다. **'우리가 함께 즐길 게임을 결정하는 데 도움을 줄 수 있는 봇을 만들면 어떨까?'**   
그리고 그는 혼잣말처럼 중얼거렸습니다.
    
### "이왕이면 친구처럼..!"    
그 순간, 그의 머릿속에는 코드와 알고리즘, 인터페이스의 이미지가 스쳐 지나갔습니다.


## 프로젝트 설명📚
- **GameBuddy (게임 친구)**   
    - 친구들과 게임을 플레이할 때 유용한 기능을 모아놓은 디스코드 봇 입니다.   
지금까지는 항상 게임을 하면서 항상 사다리타기, 투표 등등 게임에 필요한 기능들을 번거롭게 찾아가면서 했겠지만, 이제는 디스코드에서 명령어 하나로 바로 만날 수 있습니다!   
뿐만 아니라 게임 추천, 대화 기능이 있어 여러 게이머들의 게임 친구가 되어줄 것입니다.

- **이런 분께 GameBuddyBot을 추천합니다!**
    - 매번 사다리타기, 투표 등등 검색하기 귀찮으신 분!
    - 게임 친구가 많아서 팀을 자주나누고, 투표를 자주 하시는 분!
    - 디스코드 서버가 허전해서 서버에 초대할 친구를 찾으시는 분!
    - 매번 할인게임과 신규게임의 정보를 간단히 얻고 싶으신 분!
    - 게임 친구가 없어서 외로우신 분!
    - 딱딱한 말투의 봇에 질리신 분!

#### **GameBuddy가 도와드리겠습니다😆**   
<img src="https://drive.google.com/uc?id=1j0EFLE3MKqKgtwfllLbj5GwetKofquZC"/>   

*GameBuddyBot의 대표이미지*   

## 프로젝트 실행 방법📌

### **초대 링크로 실행**   
- 본인 서버에 아래 링크를 통해 봇을 초대할 수 있습니다.
- [초대 링크](https://discord.com/api/oauth2/authorize?client_id=1177902716387852381&permissions=8&scope=bot)
- '서버에 추가' 에서 봇을 추가하려는 서버를 선택 후 계속하기  
![1](https://github.com/JisubShim/GamebuddyBot/assets/118372554/219f743a-3254-45d0-9cb5-553c519b5311)   

- '관리자'에 체크하고, 승인 누르기   
![캡처](https://github.com/JisubShim/GamebuddyBot/assets/118372554/77c08a31-b5aa-4bfc-80fb-656a78ae580d)   
**꼭! 봇이 관리자 권한을 사용할 수 있게 해주어야합니다!**
<br>

- 마지막으로 원하는 서버에 초대되었는지 확인하기   
![등장](https://github.com/JisubShim/GamebuddyBot/assets/118372554/531d03f3-686d-4b5e-8d48-cda9b74b9b1f)   
*초대 되었을 때 메세지*
<br>

**GameBuddyBot은 24시간 호스팅되고 있습니다.**   
**하지만 혹시라도 오프라인이라면 아래 방법으로 실행해주십시오.**   
### **소스코드로 봇 실행 방법**   
1. git clone 하여 로컬 레포지토리로 들여온다.
2. token.txt 파일을 main.py와 같은 위치에 넣는다.
(git에는 보안상의 이유로 token.txt 파일이 없습니다. -> eclass 제출란에는 첨부했습니다.)
3. main.py를 실행한다.
<br>

**호스팅 중에 소스코드로도 실행하면 디스코드 봇이 중복 대답하므로, 이미 온라인이라면 소스코드로 실행하는 것은 권장하지 않습니다.**   

## 구현 기능🕹️
1. **명령어 설명** : GameBuddy와 소통하기 위한 명령어를 설명해줍니다.   
![!도움](https://github.com/JisubShim/GamebuddyBot/assets/118372554/d8596d98-369e-4207-a3d5-76ce2c0cde19)   
<br>

2. **인사하기** : GameBuddy와 인사합니다.   
![!안녕](https://github.com/JisubShim/GamebuddyBot/assets/118372554/c50c37d5-6c55-4754-8e6d-ffb68ccf835d)
<br>

3. **사다리타기** : 게임 순서나 역할(포지션) 등을 결정하기 위해 무작위로 사다리타기를 진행합니다.   
![!사다리타기](https://github.com/JisubShim/GamebuddyBot/assets/118372554/f18e6a1d-c181-418d-ba49-1c065167d682)
<br>

4. **투표** : 어떤 게임을 할지, 어떤 규칙을 적용할지 등 사용자들이 투표할 수 있습니다.     
![!투표](https://github.com/JisubShim/GamebuddyBot/assets/118372554/8287baab-fd99-44ea-bb1f-170ee8c93697)
<br>

6. **랜덤 선택** : 여러가지 중 하나를 무작위로 선택해줍니다.   
![!랜덤](https://github.com/JisubShim/GamebuddyBot/assets/118372554/28bceb33-2073-443c-9f7c-86eadd4a6ad4)
<br>

7. **대화하기** : GameBuddyBot과 대화합니다. (openAI assistant API 사용)   
![!대화](https://github.com/JisubShim/GamebuddyBot/assets/118372554/b65284d1-a56d-47bf-9015-9c597d69a9b3)   
<br>

8. **기억초기화** : GameBuddyBot이 지금까지 한 대화 내용을 잊어버립니다.   
![!기억초기화](https://github.com/JisubShim/GamebuddyBot/assets/118372554/8cf5a47f-03ae-4489-a220-cdfdc90ed6eb)
<br>

9. **신규 게임 추천(STEAM)** : STEAM의 신규 게임 중 10개를 보여줍니다.   
![ezgif com-video-to-gif](https://github.com/JisubShim/GamebuddyBot/assets/118372554/fd5417fa-282c-449c-9960-6785a27ca7ca)
<br>

10. **할인 게임 추천(STEAM)** : STEAM의 할인 게임 중 10개를 보여줍니다.   
![ezgif com-video-to-gif (1)](https://github.com/JisubShim/GamebuddyBot/assets/118372554/afdc28e7-f431-4185-ba51-7370b0c15a45)
<br>

- 이렇게 '!명령어' 혹은 '!명령어 ~~~~~'의 형태로 입력하면 GameBuddy가 응답합니다.


## 기타 정보 & TMI🧾
- 개발 언어 : Python 3.12.0

- discord API와 openAI assistant API를 사용하여 제작되었습니다.

- 개발(대화)에 사용된 ai 모델은 gpt-3.5-turbo-1106 입니다.

- GameBuddyBot은 repl.it과 UptimeRobot에 의해 배포되어 24시간 구동되고 있습니다.
- *~~원래는 HEROKU에서 배포했으나, 유료로 전환되어 여러가지 호스팅 방법을 찾던 중 repl.it을 사용하게 되었습니다.~~*

- GameBuddyBot의 대표이미지는 친구(백OO)가 직접 제작 및 제공해주었습니다.

- ~~딱딱한 형식의 README보다는 조금 더 편안한 분위기로 작성하려고 했습니다.~~


## 참고 자료📖

> [유튜브 : 섹시베이비](https://www.youtube.com/@user-mh7ib3xc9c)   
>>투표, 사다리타기, 랜덤 선택 기능을 구현하는데 참고했습니다.

> [유튜브 : 프로그래머 김플 스튜디오](https://www.youtube.com/watch?v=kKhWkG5Di5s)   
>>OpenAI Assistants API 사용법을 배우고, 구현에 참고했습니다.

> [네이버 블로그 : 코코블루](https://blog.naver.com/PostView.naver?blogId=6116949&logNo=221949748751&redirect=Dlog&widgetTypeCall=true&directAccess=false)   
>>GameBuddyBot이 서버에 들어왔을 때 수행 될 이벤트를 구현하기 위해 코드를 거의 동일하게 적용했습니다.

> [velog : seulki971227](https://velog.io/@seulki971227/%ED%8C%8C%EC%9D%B4%EC%8D%AC%ED%81%AC%EB%A1%A4%EB%A7%81-%EC%8A%A4%ED%8C%80%ED%99%88%ED%8E%98%EC%9D%B4%EC%A7%80-%ED%81%AC%EB%A1%A4%EB%A7%811)   
>>스팀 홈페이지 크롤링을 할 때 많은 도움이 되었고, 참고하였습니다.

> [GitHub Gist : ihoneymon/how-to-write-by-markdown.md](https://gist.github.com/ihoneymon/652be052a0727ad59601)   
>>README 파일 작성에 참고 하였습니다.

> [GitHub : NyaNyak/discord-beebot](https://github.com/NyaNyak/discord-beebot)   
>> GameBuddyBot의 아이디어를 생각해내는데 많은 도움이 되었습니다. 또 코코블루 블로그 정보도 얻을 수 있었습니다. 

- **디스코드 서버 "[Korean Discord Dictionary (KDD)](https://discord.com/invite/korean-discord-dictionary-kdd-642630345967271946)"의 BOT:개발강의로 공부하고 개발한 프로젝트입니다.**



## 프로젝트를 하며 얻은 것😃
- 파이썬 개발 경험
- Discord Bot API, OpenAI Assistants API의 사용법 학습 및 적용
- 웹 크롤링 학습 및 적용
- github 사용 경험
- **스스로 고민하며, 기획부터 개발 그리고 마무리까지 한 경험**


## 에필로그🎬
그렇게 GameBuddyBot은 많은 게이머들에게 기쁨과 동료애를 선사하며, 그들의 게임 경험을 풍요롭게 만들었습니다. 이 봇은 단순한 디스코드 봇을 넘어서, 게임을 사랑하는 모든 이들에게 영원한 친구로 남게 되었습니다!   
   
#### 감사합니다!😆

*오류 및 버그 수정 문의 : jisub5322@naver.com*