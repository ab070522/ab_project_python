import streamlit as st
from glob import glob
st.title("설문조사")

st.header("게임 중독 테스트")

gender = st.radio("당신은 여자 입니까 남자 입니까?", ('여자', '남자'))
if gender == '여자':
    gender_Eng = 'woman'
else:
    gender_Eng = 'man'

age = st.number_input('당신의 나이는?', value= 20 )
st.write('당신의 나이는 ', age)
# 1번 문제

Q_1 = st.select_slider('1번. 당신의 평균 게임 시간.',
                       options=[0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0,
                                8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0,
                                20.0, 21.0, 22.0, 23.0, 24.0])
st.write('평균 게임 시간 : {} hour'.format(Q_1))

Q_2 = st.radio(
    "2번. 당신은 컴퓨터를 켠 후 가장 먼저 게임을 시작한다.",
    ('네', '아니요'))

Q_3 = st.radio(
    "3번. 꼭 해야할 일이 없으면 거의 모든 시간을 게임하는데 보낸다.",
    ('네', '아니요'))

Q_4 = st.radio(
    "4번. 인터넷 사용 때문에 성적이나 학교 생활에 문제가 생긴 적이 있나요?",
    ('네', '아니요'))

Q_5 = st.radio(
    "5번. 인터넷에서 무엇을 했느냐고 물었을 때 숨기거나 변명을 하며 얼버무린 경험이 있나요?",
    ('네', '아니요'))

Q_6 = st.radio(
    "6번. 	외출하는 것보다 인터넷 을 하기 위해 집에 남아 있겠다고 한 적이 있나요?",
    ('네', '아니요'))

Q_7 = st.radio(
    "6번.   인터넷에 접속해 있을 때 '몇 분만 더' 라고 말하며 시간을 허비한 적이 있나요?",
    ('네', '아니요'))

Q_8 = st.radio(
    "8번. 	가족과의 관계보다 인터넷에서 더 흥미를 느낀 적이 있나요?",
    ('네', '아니요'))

Q_9 = st.radio(
    "9번. 	인터넷 하는 것 때문에 잔소리를 들은 적이 있나요?",
    ('네', '아니요'))

Q_10 = st.radio(
    "10번. 인터넷 사용 시간을 줄이도록 노력 했지만 실패한 적이 있나요?",
    ('네', '아니요'))
if Q_10 == '네':
    st.write('만약 "네" 라고 대답 했다면 11번으로 가십시오.')

else:
    st.write('만약 "아니오" 라고 대답 했다면 12번으로 가십시오.')

Q_11 = st.text_area('Q_11. 인터넷을 줄이기 위해 노력했다면 어떻게 노력 하였습니까?', '''   
     ''')

Q_12 = st.selectbox(
    'Q_12. 당신은 게임을 하기 위해 몇시까지 깨어 있었나요?',
    ('그런적 없다', '11시', '12시', '1시', '2시', '3시', '4시', '5시', '6시', '밤 새기'))
st.write('You selected:', Q_12)

if st.button('만약 모든 설문지에 답변 하였다면 클릭해 주세요.'):

    point = 0

    if Q_1 < 1:
        point += 1
    elif Q_1 < 3:
        point += 2
    elif Q_1 < 6:
        point += 3
    elif Q_1 < 10:
        point += 4
    elif Q_1 < 16:
        point += 5
    elif Q_1 <= 24:
        point += 6

    if Q_2 == '네':
        point += 3
    if Q_3 == '네':
        point += 3
    if Q_4 == '네':
        point += 3
    if Q_5 == '네':
        point += 3
    if Q_6 == '네':
        point += 3
    if Q_7 == '네':
        point += 3
    if Q_8 == '네':
        point += 3
    if Q_9 == '네':
        point += 3
    if Q_10 == '네':
        point += 3

    if Q_12 == '그런적 없다':
        point += 0
    elif Q_12 == '11시' or Q_12 == '12시':
        point += 1
    elif Q_12 == '1시' or Q_12 == '2시':
        point += 2
    elif Q_12 == '3시' or Q_12 == '4시':
        point += 3
    elif Q_12 == '5시' or Q_12 == '6시':
        point += 4
    elif Q_12 == '밤 새기':
        point += 5

    st.write('10점까지 :정상, 16점까지 : 게임 조금, 23점까지 : 중독, 32점까지 : 많이 중독 33점이상 : 병원')
    st.write('당신의 점수는 {} 점 입니다'.format(point))
    if point < 17:
        st.write('당신을 정상인 입니다.')
    elif point < 32:
        st.write('당신은 게임 중독 증상이 있습니다. 가까운 병원에 가는것을 추천 드립니다.')
    elif point >= 32:
        st.write('당신은 심각한 게임 중독 증세가 있습니다. 병원에 빨리 가보십시오.')


    all_files = glob("./*.txt")

    f = open("person {} .txt".format(int(len(all_files) + 1)), 'w')

    f.write("gender : {} \n".format(gender_Eng))
    f.write("age : {} \n".format(age))
    f.write("point : {} \n".format(point))


    f.close()
