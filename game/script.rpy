﻿# 게임에서 사용할 캐릭터를 정의합니다.
define m1 = Character('이우주') #남주1 연하 이우주
define m2 = Character('배진혁') #남주2 동갑 배진혁
define m3 = Character('지승현') #남주3 연상 지승현

define rightCharacter = Position(xalign = 0.8, yalign = 0.3)

image background_wish = "moon.jpg"
image background_room =im.FactorScale("room.jpg", 2)
image background_happyEnding = "happyending.jpg"

image background1_1 = "bg_Uju/cafeteria.jpg"
image background1_2 = "bg_Uju/playground.jpg"
image background1_3 = "bg_Uju/toSchool.jpg"

image background2_1 = "bg_Jinhyeok/playground.jpg"
image background2_2 = "bg_Jinhyeok/hallway.jpg"
image background2_3 = "bg_Jinhyeok/healthRoom.jpg"

image background3_1 = "bg_Seounghyeon/library.jpg"
image background3_2 = "bg_Seounghyeon/graduation.jpg"
image background3_3 = "bg_Seounghyeon/itshow.jpg"

image fairy = im.FactorScale("character/fairy.png",0.4)

image boy1 : 
    im.FactorScale("character/Uju/Uju_normal.png",0.5)
    yalign 0.0
image boy2 :
    im.FactorScale("character/Jinhyeok/Jinhyeok_normal.png",0.5)
    yalign 0.0
image boy3 :
    im.FactorScale("character/Seounghyeon/Seounghyeon_normal.png",0.5)
    yalign 0.0

image boy1 2 :
    im.FactorScale("character/Uju/Uju_letDown.png",0.5)
    yalign 0.0
image boy1 3 :
    im.FactorScale("character/Uju/Uju_unsmile.png",0.5)
    yalign 0.0
image boy1 4 :
    im.FactorScale("character/Uju/Uju_unsmile2.png",0.5)
    yalign 0.0
image boy1 5 :
    im.FactorScale("character/Uju/Uju_smile.png",0.5)
    yalign 0.0
image boy1 6 :
    im.FactorScale("character/Uju/Uju_smile2.png",0.5)
    yalign 0.0

image boy2 2 :
    im.FactorScale("character/Jinhyeok/Jinhyeok_letDown.png",0.5)
    yalign 0.0
image boy2 3 :
    im.FactorScale("character/Jinhyeok/Jinhyeok_worry.png",0.5)
    yalign 0.0
image boy2 4 :
    im.FactorScale("character/Jinhyeok/Jinhyeok_shy.png",0.5)
    yalign 0.0

image boy3 2 :
    im.FactorScale("character/Seounghyeon/Seounghyeon_shy.png",0.5)
    yalign 0.0
image boy3 3 :
    im.FactorScale("character/Seounghyeon/Seounghyeon_panic.png",0.5)
    yalign 0.0

image boy3 4 :
    im.FactorScale("character/Seounghyeon/Seounghyeon_fw_nm.png",0.5)
    yalign 0.0
image boy3 5 :
    im.FactorScale("character/Seounghyeon/Seounghyeon_fw.png",0.5)
    yalign 0.0
    


define player_name = "플레이어이름"
define p = Character("player_name",dynamic = True,color="#0B6121")
##Character 일때 player_name은 변수랑 같아야함.

# 여기에서부터 게임이 시작합니다.
label start:
    play music "audio/달.mp3" fadein 3.0
    $player_name = renpy.input("이름을 지정해주세요. 내 이름은")##화면에 내 이름은 나오고 다음칸에 입력받는 칸이 나온다.
    p "내 이름은 [player_name]"##p는 위에 선언한 캐릭터고, 대화창에 변수값을 나오게 할려면 [변수명]으로 사용한다.

    scene background_wish
    
    p "달님, 올해는 꼭 모태솔로에서 탈출하게 해주세요..." with fade
    stop music fadeout 3.0
    scene background_room
    play music "audio/아침.mp3" fadein 2.0
    play sound "audio/sound/알람.mp3"
    "아침 7시 알람이 시끄럽게 울린다." with vpunch
    stop sound fadeout 2.0
    play sound "audio/sound/바람.mp3"
    show fairy at rightCharacter
    "???" "[player_name]!"  with zoomin
    "???" "이것이 네 이름이 맞느냐?"
    p "누... 누구세요? 토끼가 말을 하네... 내가 잠이 덜 깼나?"
    "???" "어허! 무엄하도다!"
    "???" "나로 말할 것 같으면..."
    "치치" "네 놈의 소원을 이뤄주러 친히 인간계에 당도한\n 달의 요정 치치님이시다!"
    "치치" "내 너를 위해 아주 괜찮은 인간 남자 세 명을 엄선해 놨느리라!"
    p "아니, 저... 혹시 이거 상황극인가요?"
    "치치" "예끼 이 놈!!!\n 아직도 정신을 못 차린게냐!" with hpunch
    "치치" "흥... 하는 말과 행동이 괘씸하나, 내 너의 소원은 이루어 줘야 하니 한 번은 넘어가 주겠노라."
    "치치" "자, 세 명의 인간 남자 중 마음에 드는 한 명을 선택해 보거라!\n 그 자가 너의 애인이 될 것이니라."
    stop sound
    play music "audio/선택.mp3" fadein 2.0
    label choice:
    menu :
        "남자를 고르라니... 에잇, 모르겠다!"
        "이우주":
            stop music
            play sound "audio/sound/뾰로롱.mp3"
            scene background1_3
            show boy1
            "아이돌 연습생 연하남 이우주를 선택했습니다."
            play sound "audio/등굣길.mp3" fadein 2.0
            hide boy1
            show boy1 5 with dissolve
            m1 "누나 안녕?ㅎㅎ"
            p "(응? ...누구지? 조금 당황스럽네...)"
            
            show boy1 4 with dissolve
            m1 "어...? 누나! 저 기억 안 나요?" with zoomin

            jump start1

        "배진혁":
            stop music
            play sound "audio/sound/뾰로롱.mp3"
            scene background2_1
            show boy2
            "같은 반 축구부 배진혁을 선택했습니다." 

            jump start2

        "지승현":
            stop music
            play sound "audio/sound/뾰로롱.mp3"
            scene background3_1
            show boy3
            "전교1등 선배 지승현을 선택했습니다."

            jump start3

        
#이우주

label start1:
    play music "audio/등굣길.mp3" fadein 2.0
    "뭐라고 대답해야하지..."
    menu:
        "글쎄... 잘 모르겠는데?":
            jump ending1
        "아, 당연히 기억하지!":
            jump love1

label love1:
    play music "audio/등굣길.mp3" fadein 2.0
    play sound "audio/sound/심장소리.wav"loop
    "두근두근..."
    show boy1 5 with dissolve
    stop sound

    m1 "누나가 중학교 졸업한 이후로 처음 보네요!"

    "귀엽기만 했던 중학교 후배가 아이돌 연습생이 되어 돌아왔다"

    m1 "아... 벌써 도착했네. 점심 시간에 찾아갈테니까 그 때 봐요 누나!"
    hide boy1 5
    scene background1_1
    play music "audio/급식실.mp3"
    "-점심시간(급식실)-"

label cafeteria:
    play music "audio/급식실.mp3"
    show boy1 6 with dissolve
    "우주가 정말 아이돌 연습생이긴 한가보다..."
    "같이 밥을 먹으니 아이들의 이목이 쏠리기 시작한다."

menu:
    "역시 불편한데..."

    "그래도 그냥 참고 먹는다.":

        jump ending2
    
    "부담스러우니 먼저 간다고 말한다.":

        jump love2

label love2:
    play music "audio/급식실.mp3"
    "아... 더 이상 못 참겠어!"
    show boy1 4 with dissolve
    p "우주야 미안, 나 먼저 가볼게! 마저 먹고 나와."
    "나는 그대로 자리를 박차고 나왔다."
    m1 "아... 누나! 같이 가요!"
    hide boy1 4
    scene background1_2
    play music "audio/운동장.mp3"
    "-운동장-"
label playground:
    play music "audio/운동장.mp3"
    show boy1 3 with dissolve

    m1 "누나... 저 사실...."

    menu:
        "갑자기 진지해졌네... 무슨 일이지?"

        "아... 미안. 나 바쁜 일이 있어서 먼저 갈게 천천히 와.":

            jump ending3

        "응? 무슨 할 말이라도 있어?":

            jump love3
        
    label love3:
        play music "audio/운동장.mp3"
        show boy1 6 with dissolve
        m1 "저.. "

        "???"
        show boy1 5 with dissolve
        play sound "audio/sound/심장소리.wav"
        "(심장이 쿵쾅대기 시작한다.)" with vpunch
        
        m1 "중학생 때부터 쭉 누나만을 좋아했어요...! 제가 어떤 모습이어도, 누나는 절 진심으로 사랑해 주실 거 같다는 느낌이 들어요."

        label goback:
        play music "audio/운동장.mp3"
        play sound "audio/sound/심장소리.wav"
        show boy1 6 with dissolve
        m1 "저랑... 사귀어 주세요...!!"with vpunch

        menu:
            "이건... 너무 갑작스러운데!? 어쩌지..."

            "그래, 나도 사실... 널 좋아했어. 우리 사귀자.":
            
                jump love4

            "저... 우주야 미안... 난 지금이 좋아.":
                stop sound
                jump ending4

label love4:
    scene background_happyEnding
    stop sound 
    play music "audio/해피엔딩.mp3" fadein 1.0
    show boy1 with dissolve
    "이럴수가... 오늘부터 1일!!"
    "이렇게 귀여운 남자친구가 생기다니!"
    "{b}Happy Ending{/b}."

    menu:
        "역시 연하는 내 취향이 아니야! 다른 사람을 만나보겠어!":
            jump choice
        "다른 남자는 필요하지 않아. 이대로 끝낼래요!":
            return

label ending1:

    "내가 대답을 잘 한 게 맞을까?"
    show boy1 2 with dissolve
    m1 "누나... 너무해요!!"
    stop music
    play music "audio/badEnding.mp3" fadein 1.0
    "{b}
    다시 잘 생각 해 봐!!\n
    Bad Ending{/b}."  with hpunch
    stop music

    menu:
        "이전으로 돌아갈래요!":
            jump start1
        "다른 사람을 만나러 갈래요!":
            jump choice
        "아니요, 그냥 이대로 끝낼게요!":
            return

label ending2:
    "참아보려 하지만..."
    "표정관리가 되지 않는다...!"
    show boy1 2 with dissolve
    m1 "저... 누나? 표정이 왜 그래요? 혹시... 저랑 있는 게 부담스러우신 거에요?"
    stop music
    play music "audio/badEnding.mp3" fadein 1.0
    "의도치 않게 상처를 줘버렸잖아..."
    "{b}Bad Ending{/b}." with hpunch
    stop music
    menu:
        "이전으로 돌아갈래요!":
            jump cafeteria
        "다른 사람을 만나러 갈래요!":
            jump choice
        "아니요, 그냥 이대로 끝낼게요!":
            return

label ending3:
    show boy1 2 with dissolve
    "꽤 진지해 보였는데 이야기도 들어주지 않다니 너무하네!"
    stop music
    play music "audio/badEnding.mp3" fadein 1.0
    "{b}Bad Ending{/b}." with hpunch
    stop music
    menu:
        "이전으로 돌아갈래요!":
            jump  playground
        "다른 사람을 만나러 갈래요!":
            jump choice
        "아니요, 그냥 이대로 끝낼게요!":
            return

label ending4:
    show boy1 2 with dissolve
    "다 왔는데 이런... 눈치 좀 챙겨 [player_name]!!!"
    stop music
    play music "audio/badEnding.mp3" fadein 1.0
    "{b}Bad Ending{/b}." with hpunch
    stop music
    menu:
        "이전으로 돌아갈래요!":
            jump goback
        "다른 사람을 만나러 갈래요!":
            jump choice
        "아니요, 그냥 이대로 끝낼게요!":
            return


# 배진혁

label start2:
    play music "audio/운동장.mp3" fadein 1.0
    hide boy2
    p "아 오늘 체육 있었지..." with fade

    "짝피구...? 내 짝은 누구지?"
    show boy2 with dissolve
    "어, 배진혁...?" 

label jin_love1:
    hide boy2 with fade
    p "아야!" with vpunch
    "발목을 삐었나..."
    show boy2 3 with dissolve
    m2 "하, 야 살살 던지라고 했지!" 
    m2 "[player_name], 너 괜찮아? 이리와 보건실 가자."
    m2 "어떻게 보면 내 잘못도 있으니까... 같이 가줄게."
    label go:
    "어, 같이...?"
    menu:
        "아니야, 괜찮아! 나 혼자 갈 수 있어.":
            jump jin_ending1

        "그래줄래? 고마워." :
            jump jin_love2

label jin_love2:
    hide boy2 3
    scene background2_3
    play music "audio/급식실.mp3"
    "진혁이의 부축을 받으며 보건실로 향했지만 보건 선생님은 자리에 계시지 않는다."
    show boy2 3 with dissolve
    m2 "선생님이 안 계시네."
    "진혁이는 다친 내 발목을 보더니 한숨을 쉰다."
    "내가 뭐라도 잘못했나..."
    label sick:
    m2 "그... 너만 괜찮으면 내가 치료해줄게."
    m2 "네가 알고 있을지 모르겠는데, 나 운동부라서 치료 경험도 꽤 있거든. 안 아프게 해줄게."
    "그걸 모르는 애가 우리학교에 있을 리가..."

    menu:
        "그, 그렇게까지 안 해줘도 돼. 오실 때까지 기다리면 되지!":
        
            jump jin_ending2
        
        "그럼 믿을만 하겠네. 부탁할게.":

            jump jin_love3

label jin_love3:
    play music "audio/보건실.mp3"
    show boy2 with dissolve
    m2 "자... 다 됐다."
label abuba:
    stop music
    scene background2_2
    m2 "[player_name], 혼자 못 걷겠지? 업혀. 교실까지 데려다 줄게."
    "내 나이가 몇인데...!"
    menu:
        "아, 아니야! 충분히 혼자 걸을 수 있어.":
        
            jump jin_ending3
        
        "저, 그럼 잠시 실례할게...":

            jump jin_ending4

label jin_ending1:
    show boy2 2 with dissolve
    m2 "아... 그래."
    "진혁이는 멋쩍은듯 서있다 돌아가버렸다"
    "부탁했어야지!!"
    stop music
    play music "audio/badEnding.mp3" fadein 1.0
    "{b}Bad Ending{/b}." with hpunch
    stop music
    menu:
        "이전으로 돌아갈래요!":
            jump go
        "다른 사람을 만나러 갈래요!":
            jump choice
        "아니요, 그냥 이대로 끝낼게요!":
            return

label jin_ending2:
    show boy2 2 with dissolve
    m2 "아... 그래 미안."
    "어색한 공기가 흐른다..."
    "부탁했어야지!!"
    stop music
    play music "audio/badEnding.mp3" fadein 1.0
    "{b}Bad Ending{/b}." with hpunch
    stop music
    menu:
        "이전으로 돌아갈래요!":
            jump sick
        "다른 사람을 만나러 갈래요!":
            jump choice
        "아니요, 그냥 이대로 끝낼게요!":
            return

label jin_ending3:
    show boy2 2 with dissolve
    m2 "그래...? 내가 좀 과했나보네."
    "진혁은 어색하게 웃으며 운동장으로 돌아갔다"
    "부탁했어야지!!"
    stop music
    play music "audio/badEnding.mp3" fadein 1.0
    "{b}Bad Ending{/b}." with hpunch
    stop music
    menu:
        "이전으로 돌아갈래요!":
            jump abuba
        "다른 사람을 만나러 갈래요!":
            jump choice
        "아니요, 그냥 이대로 끝낼게요!":
            return

label jin_ending4:
    hide boy2
    play music "audio/복도.mp3"
    "그렇게 진혁이의 등에 업혀 교실까지 올라왔다..."
    show boy2 with dissolve
    "그 전부터 진혁이를 좋아했던 나는 이때를 기회로 용기를 내어본다."
    play sound "audio/sound/심장소리.wav"loop
    p "저... 진혁아."
    p "지금 이런 말 하는게 어떻게 들릴지 모르겠지만..."
    p "나, 오래 전부터 널 좋아해왔어."
    p "그러니까 우리... 사귈래?"
    show boy2 4 with dissolve
    "내 고백을 들은 진혁이는 처음보는 표정을 지으며 고개를 숙였다."
    "쟤도 얼굴이 붉어지긴 하는구나..."

    m2 "응... 좋아."
    stop sound
    play music "audio/해피엔딩.mp3" fadein 1.0
    scene background_happyEnding
    show boy2 with dissolve
    "{b}Happy Ending{/b}."
    menu:
        "역시 내 취향은 아니야 다른 사람을 만나볼래!":
            jump choice
        "다른 사람은 됐어요! 이대로 끝낼래요!":
            return

# 지승현

label start3:
    play music "audio/도서관.mp3" fadein 3.0
    hide boy3
    "시험기간 도서관에서 침 흘리며 졸고 있는 [player_name]"
    "누군가 다가와 어깨를 톡톡 친다."
    "졸린 눈을 부비며 일어나자..."
    show boy3 with dissolve
    "그... 그 전교 1등 지승현... 선배?"
    "황급히 입가에 묻은 침자국을 지우며 고개를 숙인다."

    p "아, 그... 감사합니다!"

label seng_love1:
    play music "audio/도서관.mp3" fadein 3.0
    show boy3 with dissolve
    m3 "뭘 감사할 거 까지야. [player_name]... 맞지? 공부 중인 거 같던데, 같이 할래?"
    "내 이름은 어떻게..."
    "아, 이럴 때가 아니지! 뭐라고 대답해야 좋을까..."
    menu:
        "아니에요 선배! 바쁘실 것 같은데 저 혼자 알아서 할게요":

            jump seng_ending1

        "네...! 저도 전교 1등으로 만들어 주세요!" :

            jump seng_love2

label seng_love2:
    play music "audio/도서관.mp3" fadein 3.0
    show boy3 2 with dissolve
    m3 "그래, 좋아 같이 공부하자 ㅎㅎ"
    m3 "무슨 공부 도와줄까?"

    menu:
        "html이요!":
        
            jump seng_ending2
        
        "미술이요!":

            jump seng_ending3

        "React요!":    

            jump seng_love3

label seng_love3:
    play music "audio/도서관.mp3" fadein 3.0
    m3 "그래, 리액트 좋네. 옆에 앉아도 되지?"

label graduation:
    hide boy3 2
    scene background3_2
    play music "audio/학생소리.wav" fadein 1.0
    "승현 선배의 졸업 당일"
    show boy3 with dissolve
    "이제 선배를 학교에서 볼 수 없다니... 눈물이 앞을 가린다."

    menu:
        "이대로 선배를 놓칠 수는 없어! 승현 선배에게 고백한다.":
        
            jump seng_ending4
        
        "다음에 또 만나면 되니까... 내년 ITSHOW에 놀러와 달라고 부탁하며 번호를 남긴다.":

            jump seng_love4

label seng_love4:
    scene background3_3
    play music "audio/복도.mp3" fadein 1.0
    "1년 뒤 3학년이 된 미림이의 it쇼 당일"
    "어, 저기... 설마, 승현 선배?!"

    show boy3 5 with dissolve
    m3 "[player_name]! 고생 많았지? 자 여기 꽃다발."
    "진짜 승현 선배다..."
    menu:
        "1년 만에 만난 승현 선배에게 안기며 고백한다.":
        
            jump seng_ending6
            
        "아, 저... 감사합니다..!!! (부끄러워 한 뒤 도망친다)":

            jump seng_ending5

label seng_ending1:
    play music "audio/도서관.mp3" fadein 3.0
    show boy3 3 with dissolve
    m3 "그래.. 나랑 공부하기 싫구나.."
    hide boy3 3
    "선배는 조용히 도서관을 떠난다."
    "같이 했어야지!!"
    stop music
    play music "audio/badEnding.mp3" fadein 1.0
    "{b}Bad Ending{/b}." with hpunch
    stop music
    menu:
        "이전으로 돌아갈래요!":
            jump seng_love1
        "다른 사람을 만나러 갈래요!":
            jump choice
        "아니요, 그냥 이대로 끝낼게요!":
            return

label seng_ending2:
    play music "audio/도서관.mp3" fadein 3.0
    show boy3 3 with dissolve
    m2 "이건 너무 기초인데.. 아직도 모른다니 실망이야"
    m2 "같이 공부하기로 한 건 없던 걸로 하자"
    "기초부터 다지고 다시 도전하자"
    stop music
    play music "audio/badEnding.mp3" fadein 1.0
    "{b}Bad Ending{/b}." with hpunch
    stop music

    menu:
        "이전으로 돌아갈래요!":
            jump seng_love2
        "다른 사람을 만나러 갈래요!":
            jump choice
        "아니요, 그냥 이대로 끝낼게요!":
            return

label seng_ending3:
    play music "audio/도서관.mp3" fadein 3.0
    show boy3 3 with dissolve
    m2 "내가 미술은 못 해서.."
    "승현은 당황한 표정을 짓더니 이내 나에게 말을 걸지 않았다."
    stop music
    play music "audio/badEnding.mp3" fadein 1.0
    "{b}Bad Ending{/b}." with hpunch
    stop music
    menu:
        "이전으로 돌아갈래요!":
            jump seng_love2
        "다른 사람을 만나러 갈래요!":
            jump choice
        "아니요, 그냥 이대로 끝낼게요!":
            return

label seng_ending4: 
    play music "audio/학생소리.wav" fadein 1.0
    show boy3 3 with dissolve
    m3 "미안 지금은 너무 바빠서.."
    "타이밍을 봐야지!!"
    stop music
    play music "audio/badEnding.mp3" fadein 1.0
    "{b}Bad Ending{/b}." with hpunch
    stop music
    menu:
        "이전으로 돌아갈래요!":
            jump graduation
        "다른 사람을 만나러 갈래요!":
            jump choice
        "아니요, 그냥 이대로 끝낼게요!":
            return

label seng_ending5:
    play music "audio/학생소리.wav" fadein 1.0
    m3 "아.. 가버렸네..."
    "그렇게 난 다시는 선배를 볼 수 없었다."
    "도망치면 안되지!!"
    stop music
    play music "audio/badEnding.mp3" fadein 1.0
    "{b}Bad Ending{/b}." with hpunch
    stop music
    menu:
        "이전으로 돌아갈래요!":
            jump seng_love4
        "다른 사람을 만나러 갈래요!":
            jump choice
        "아니요, 그냥 이대로 끝낼게요!":
            return

label seng_ending6:
    p "승현 선배.. 아니 승현 오빠! 사실 예전부터 오빠를 좋아했어요!!!"

    show boy3 4 with dissolve
    m3 "나도 널 좋아했어 우리 사귀자"
    stop music
    play music "audio/해피엔딩.mp3" fadein 1.0
    scene background_happyEnding
    show boy3 5 with dissolve
    "{b}Happy Ending{/b}."
    menu:
        "역시 내 취향은 아니야 다른 사람을 만나볼래!":
            jump choice
        "다른 사람은 됐어요! 이대로 끝낼래요!":
            return