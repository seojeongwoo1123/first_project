import streamlit as st
import random

# 🎨 페이지 설정
st.set_page_config(
    page_title="가위✌️ 바위✊ 보✋ 게임",
    page_icon="🎮",
    layout="centered"
)

# 🌟 타이틀
st.markdown("""
    <div style='text-align: center;'>
        <h1>🎮 가위 ✌️ 바위 ✊ 보 ✋ 게임!</h1>
        <h3>운을 시험해 보세요! 😎</h3>
    </div>
""", unsafe_allow_html=True)

# 🎲 게임 선택
options = {
    "✌️ 가위": "scissors",
    "✊ 바위": "rock",
    "✋ 보": "paper"
}

user_choice_display = st.selectbox("무엇을 낼까요? 🤔", list(options.keys()))
user_choice = options[user_choice_display]

# 🧠 컴퓨터 선택
computer_choice = random.choice(list(options.values()))
computer_emoji = [k for k, v in options.items() if v == computer_choice][0]

# 📊 게임 결과 판정 함수
def determine_winner(user, computer):
    if user == computer:
        return "😐 비겼어요!"
    elif (user == "scissors" and computer == "paper") or \
         (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock"):
        return "🎉 당신이 이겼어요! 🎊"
    else:
        return "😭 컴퓨터가 이겼어요!"

# 🎮 게임 시작 버튼
if st.button("대결 시작! ⚔️"):
    st.markdown("---")
    st.write(f"👨 당신의 선택: **{user_choice_display}**")
    st.write(f"💻 컴퓨터의 선택: **{computer_emoji}**")
    
    result = determine_winner(user_choice, computer_choice)
    st.markdown(f"<h2 style='text-align: center;'>{result}</h2>", unsafe_allow_html=True)

    st.balloons()

# ⬇️ 하단
st.markdown("---")
st.markdown("<div style='text-align: center;'>© 2025 RPS Game Co. | 🎮 Made with ❤️ using Streamlit</div>", unsafe_allow_html=True)

