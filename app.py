import streamlit as st
from pathlib import Path

# ─────────────────────────────────────────────
# 페이지 기본 설정
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="수현 언니에게 💛",
    page_icon="🌻",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
# 30일치 날짜별 데이터
#
# 📌 photo / video 파일명은 아래 media 폴더 안 파일 이름과 똑같이 써줘!
# 📌 사진도 영상도 없는 날은 이모지 배경이 자동으로 나와요
# ─────────────────────────────────────────────
DAY_DATA = {
    1: {
        "emoji": "🌱",
        "photo": None,
        "video": None,
        "message": (
            "언니 오늘 입원했겠네\n"
            "두렵고 떨리는 거 다 알아\n"
            "근데 있잖아 ~ 언니는 분명히 잘 할 수 있오\n"
            "내가 그냥 하는 말이 아니라 진짜로 믿어 💛"
        ),
    },
    2: {
        "emoji": "🌙",
        "photo": None,
        "video": None,
        "message": (
            "수술 전날 밤이야\n"
            "걱정 많이 되지? 그 마음 당연한 거야..!\n"
            "근데 너무 걱정하지 마!\n"
            "내일 끝나고 나면 '별거 아니었네' 할 거야\n"
            "오늘 밤 푹 자고 내일 멋지게 들어가 💪"
        ),
    },
    3: {
        "emoji": "🙏",
        "photo": None,
        "video": None,
        "message": (
            "언니 오늘 수술 잘 받고 와!!!\n"
            "나 열심히 기도하고 있을게🙏\n"
            "언니 손 꼭 잡아주고 싶다 ㅠㅠ\n"
            "마음은 항상 옆에 있어 ✨"
        ),
    },
    4: {
        "emoji": "☀️",
        "photo": None,
        "video": None,
        "message": (
            "언니 수술 받느라 진짜 고생 많았어!!\n"
            "오늘 눈 뜬 것만으로도 충분해 정말로 ~\n"
            "아무것도 안 해도 돼 그냥 숨만 쉬어 후후\n"
            "언니가 잘 마치고 나온 걸로도 난 행복해 ☀️"
        ),
    },
    5: {
        "emoji": "🤍",
        "photo": None,
        "video": None,
        "message": (
            "중환자실.. 낯설고 무섭지?\n"
            "모르는 곳에서 혼자 있는 느낌 들 것 같아서 걱정도 되고 마음도 아프네 ㅠㅠ\n"
            "근데 언니 나 항상 응원하고 있어!\n"
            "눈에 안 보여도 마음은 늘 옆에 있어 🤍"
        ),
    },
    6: {
        "emoji": "🛌",
        "photo": None,
        "video": None,
        "message": (
            "지금은 그냥 회복에만 집중!!\n"
            "다른 거 생각하지 말고 아무 걱정도 하지 말고\n"
            "언니 몸 낫는 게 지금 제일 중요한 일이야!!\n"
            "잘 먹고, 잘 자고, 잘 쉬어 🛌💛"
        ),
    },
    7: {
        "emoji": "🧸",
        "photo": None,
        "video": None,
        "message": (
            "아프면 아프다고 해도 돼\n"
            "힘들면 힘들다고 해도 되고 울어도 돼\n"
            "참지 않아도 돼 괜찮은 척 안 해도 돼\n"
            "그 모습 그대로 다 괜찮아 🧸\n"
            "언제든지 기대줘 내가 덩치 키워둘게 크크"
        ),
    },
    8: {
        "emoji": "🎉",
        "photo": "photo_01.JPG",
        "video": None,
        "message": (
            "우리 이때 좀 어색했던 거 기억해? ㅎㅎ\n"
            "나는 이때도 언니가 진짜 정말 좋았오 ~\n"
            "어색했어도 같이 있는 게 그냥 좋았걸랑\n"
            "다 나으면 연말 파티 하자 ~!!!🎉"
        ),
    },
    9: {
        "emoji": "🌈",
        "photo": None,
        "video": None,
        "message": (
            "비 오는 날 다음엔 꼭 무지개 뜨잖아!\n"
            "지금 언니한테 비가 많이 오고 있어두\n"
            "그 다음에 뜰 무지개 진짜 크고 선명할 거야 🌈\n"
            "그날까지 같이 힘내보장"
        ),
    },
    10: {
        "emoji": "🌙",
        "photo": None,
        "video": None,
        "message": (
            "오늘 하루도 정말 수고했오\n"
            "오늘도, 내일도, 그 다음날도!\n"
            "언니 옆에서 항상 응원하고 있어!!\n"
            "오늘 밤 푹 자 🌙 내일도 파이팅이야 💛"
        ),
    },
    11: {
        "emoji": "🌻",
        "photo": None,
        "video": None,
        "message": (
            "해바라기는 항상 해를 바라보잖아!\n"
            "언니가 딱 그래\n"
            "힘들어도 밝은 쪽으로 고개 드는 사람 ㅎㅎ\n"
            "항상 힘내자앙 🌻"
        ),
    },
    12: {
        "emoji": "😊",
        "photo": "photo_08.jpg",
        "video": None,
        "message": (
            "언니 웃는 거 진짜 예쁜 거 알아?\n"
            "나 그 웃음 보면 괜히 나도 기분 좋아지거든 ㅎㅎ\n"
            "지금 이거 보면서 한 번 웃자!!\n"
            "언니 웃는 거 보고 싶어서 그래 😊💛"
        ),
    },
    13: {
        "emoji": "😂",
        "photo": "photo_02.jpg",
        "video": None,
        "message": (
            "이거 다시 봐도 진짜 웃기지 않아?? 😂\n"
            "동성 배경 진짜 웃겼는데 ㅠㅠㅋㅋㅋ\n"
            "한번 더 웃어 이 사진 보면서 ㅋㅋㅋㅋ"
        ),
    },
    14: {
        "emoji": "🌤️",
        "photo": None,
        "video": None,
        "message": (
            "오늘 잠깐 창문 열고 하늘 한번 봐!\n"
            "구름이 있든 맑든 상관없이\n"
            "그 하늘 아래 나도 언니 생각하면서 같은 하늘 보고 있어 🌤️\n"
            "멀어도 연결돼있는 느낌 들지 않아? 💛"
        ),
    },
    15: {
        "emoji": "🍀",
        "photo": None,
        "video": None,
        "message": (
            "오늘의 행운은 전부 다 언니 거야!!\n"
            "내 것까지 다 빌어줬거든 🍀\n"
            "오늘 좋은 일 하나는 꼭 있을 거양\n"
            "아주 작은 거라도 발견해봐 😊"
        ),
    },
    16: {
        "emoji": "💌",
        "photo": "photo_03.jpg",
        "video": None,
        "message": (
            "언니는 정말 따뜻하고 좋은 사람이야\n"
            "깜짝 선물 얼마나 감동이었는지 ㅜ.ㅜ\n"
            "이제 내 차례야!\n"
            "나도 열심히 응원하고 있어 언니 💌💛"
        ),
    },
    17: {
        "emoji": "🎶",
        "photo": None,
        "video": None,
        "message": (
            "오늘은 그냥 쉬어 ~\n"
            "제일 좋아하는 노래 틀어놓고 눈 감고 있어봐!\n"
            "노래도 치료야!! 🎶\n"
            "언니가 제일 좋아하는 노래 뭔지 나중에 알려줘 😊"
        ),
    },
    18: {
        "emoji": "🤝",
        "photo": None,
        "video": None,
        "message": (
            "언니 손 잡아주고 싶다\n"
            "옆에서 괜찮다고 말해주고 싶은데 ㅠㅠ\n"
            "회복되면 제일 먼저 달려갈게 💨💛"
        ),
    },
    19: {
        "emoji": "📸",
        "photo": None,
        "video": "video_01.MP4",
        "message": (
            "언니랑 사진 또 찍고 싶다아앙\n"
            "우리 진짜 너무 귀엽잖아 ~ 봐봐 ㅋㅋㅋ 📸\n"
            "얼른 나와서 또 찍쟈\n"
            "다음엔 더 재밌게 찍어보자 😆💛"
        ),
    },
    20: {
        "emoji": "🍽️",
        "photo": "photo_04.jpg",
        "video": None,
        "message": (
            "언니 지금부터 먹고 싶은 거 리스트 적어!!\n"
            "회복하면 맛있는 거 잔뜩 묵쟈앙🍽️\n"
            "제일 먹고 싶은 1순위 생각해두기 ~"
        ),
    },
    21: {
        "emoji": "🌊",
        "photo": None,
        "video": None,
        "message": (
            "파도가 강하게 칠수록 모래사장이 더 단단해진대\n"
            "지금 언니한테 파도가 엄청 세게 치고 있는 거 알아\n"
            "근데 그만큼 언니도 더 단단해지고 있어 🌊\n"
            "나는 그걸 알기 때문에 믿어!!"
        ),
    },
    22: {
        "emoji": "⭐",
        "photo": None,
        "video": None,
        "message": (
            "오늘 하루도 진짜 고생 많았옹\n"
            "언니 지금 정말 잘 하고 있어!\n"
            "스스로한테 오늘 수고했다고 한 번 말해줘 ⭐\n"
            "나도 말해줄게! 언니 오늘도 최고야 💛"
        ),
    },
    23: {
        "emoji": "😂",
        "photo": None,
        "video": "video_02.MP4",
        "message": (
            "이날 다시 생각해도 진짜 웃기지 않아?? 😂\n"
            "우리 이제 저기 마스터 됐으니까\n"
            "다 나으면 다시 찍으러 가자 ㅋㅋㅋ\n"
            "진짜 또 가야 해 꼭!!!"
        ),
    },
    24: {
        "emoji": "💌",
        "photo": None,
        "video": "video_03.MP4",
        "message": (
            "이 메시지들 보면서 언니가 한 번이라도 웃었으면 좋겠당\n"
            "조금이라도 힘이나길..!!\n"
            "그게 내가 이거 만든 이유야 💌\n"
            "언니 행복을 위해 ~"
        ),
    },
    25: {
        "emoji": "🌈",
        "photo": None,
        "video": None,
        "message": (
            "지금 이 힘든 시간이 지나면\n"
            "나중에 기쁠 때 더 크게 기쁠 수 있어!\n"
            "지금 버티는 언니가 나중에 더 환하게 웃을 거야 🌈\n"
            "그때까지 응원할겡 💛"
        ),
    },
    26: {
        "emoji": "🙌",
        "photo": None,
        "video": None,
        "message": (
            "오늘도 잘 버텨줘서 고마워\n"
            "버티고 기대는 것도 엄청난 용기야\n"
            "매일 여기 열어보는 것도 나한텐 언니가 열심히 하고 있다는 신호야 🙌\n"
            "마지막까지 기대해조 ㅎㅎ"
        ),
    },
    27: {
        "emoji": "😤",
        "photo": "photo_05.JPG",
        "video": None,
        "message": (
            "이거 다시 봐도 진짜 너무하지 않아?? 😤\n"
            "저 글씨 색 진짜 속잖아요!!\n"
            "우리 이때 얼마나 황당했는지 ㅋㅋㅋ\n"
            "웃다 눈물 났잖아 😂"
        ),
    },
    28: {
        "emoji": "💐",
        "photo": "photo_06.JPG",
        "video": None,
        "message": (
            "언니가 병원에서 제일 예쁠 듯 ~ 💐\n"
            "오늘도 한번 웃어봐!\n"
            "언니 웃는 모습 보고싶당 ㅎㅎ\n"
            "파이팅 언니!! 거의 다 왔어 💛"
        ),
    },
    29: {
        "emoji": "🎊",
        "photo": None,
        "video": None,
        "message": (
            "벌써 한 달이 됐어!!\n"
            "언니 진짜 고생 많았옹\n"
            "앞으로도 같이 가는 거야 ~\n"
            "항암도 같이 이겨내자 🎊 항상 응원 중이야!!!"
        ),
    },
    30: {
        "emoji": "🌻",
        "photo": "photo_07.jpg",
        "video": None,
        "message": (
            "우리 피크닉 또 가자 🌻\n"
            "이번엔 다른 데로! 더 예쁜 데 찾아서!\n"
            "언니 나으면 달려갈게엥\n"
            "언니 30일 동안 정말 수고 많았어 ㅎㅎ\n"
            "앞으로 항암도 같이 이겨낼 거얍!!!!!\n"
            "나는 항상 언니 편이야!! 지금도, 앞으로도 🌻"
        ),
    },
}

EMOJI_FALLBACK = ["🌻", "🌸", "🍊", "💛", "🌈", "☀️", "🌺", "🎀", "🍀", "🌙",
                  "✨", "💌", "🌷", "🌱", "⭐", "🎶", "🤍", "🌊", "💪", "🎊"]

MEDIA_DIR = Path("media")

# ─────────────────────────────────────────────
# CSS 스타일
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gaegu:wght@400;700&family=Noto+Sans+KR:wght@400;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Noto Sans KR', sans-serif;
}
.stApp {
    background: linear-gradient(160deg, #FFF8ED 0%, #FFE8C8 100%);
    min-height: 100vh;
}
.main-title {
    font-family: 'Gaegu', cursive;
    font-size: 2.4rem;
    color: #E8720C;
    text-align: center;
    margin-bottom: 0.2rem;
    letter-spacing: 1px;
}
.sub-title {
    font-family: 'Gaegu', cursive;
    font-size: 1.1rem;
    color: #F5A623;
    text-align: center;
    margin-bottom: 1.5rem;
}
.day-badge {
    background: #E8720C;
    color: white;
    border-radius: 50px;
    padding: 0.3rem 1rem;
    font-size: 0.9rem;
    font-weight: 700;
    display: inline-block;
    margin-bottom: 0.8rem;
}
.message-box {
    background: linear-gradient(135deg, #FFF3D4, #FFE0A3);
    border-radius: 18px;
    padding: 1.4rem 1.6rem;
    font-size: 1.05rem;
    line-height: 1.9;
    color: #5C3D11;
    font-family: 'Noto Sans KR', sans-serif;
    white-space: pre-line;
    border-left: 5px solid #F5A623;
    margin-top: 1rem;
}
.emoji-bg {
    font-size: 6rem;
    text-align: center;
    padding: 1.5rem;
    background: linear-gradient(135deg, #FFF3D4, #FFDDA3);
    border-radius: 18px;
    margin-bottom: 0.8rem;
}
.stButton > button {
    background: linear-gradient(135deg, #F5A623, #E8720C);
    color: white;
    border: none;
    border-radius: 50px;
    padding: 0.6rem 2rem;
    font-size: 1rem;
    font-weight: 700;
    font-family: 'Noto Sans KR', sans-serif;
    transition: all 0.2s;
    box-shadow: 0 3px 12px rgba(232,114,12,0.3);
}
.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 18px rgba(232,114,12,0.4);
}
.stTabs [data-baseweb="tab-list"] {
    background: #FFF3D4;
    border-radius: 12px;
    padding: 4px;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 10px;
    font-family: 'Noto Sans KR', sans-serif;
    font-weight: 600;
}
.stTabs [aria-selected="true"] {
    background: #E8720C !important;
    color: white !important;
}
hr { border: none; border-top: 2px dashed #FFD89B; margin: 1.2rem 0; }
[data-testid="collapsedControl"] { display: none; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# 헬퍼 함수
# ─────────────────────────────────────────────
def get_media(day: int):
    data = DAY_DATA.get(day, {})
    photo_file = data.get("photo")
    video_file = data.get("video")
    photo_path = None
    video_path = None
    if photo_file:
        p = MEDIA_DIR / "photos" / photo_file
        if p.exists():
            photo_path = str(p)
    if video_file:
        v = MEDIA_DIR / "videos" / video_file
        if v.exists():
            video_path = str(v)
    return photo_path, video_path

def get_day_info(day: int):
    data = DAY_DATA.get(day, {})
    emoji = data.get("emoji", EMOJI_FALLBACK[(day - 1) % len(EMOJI_FALLBACK)])
    message = data.get("message", "오늘도 언니 응원해 💛")
    return emoji, message

def show_card(day: int):
    emoji, message = get_day_info(day)
    photo_path, video_path = get_media(day)
    st.markdown(f'<div class="day-badge">Day {day} 💛</div>', unsafe_allow_html=True)
    if video_path:
        st.video(video_path)
    if photo_path:
        st.image(photo_path, use_container_width=True)
    if not video_path and not photo_path:
        st.markdown(f'<div class="emoji-bg">{emoji}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="message-box">{emoji}&nbsp;&nbsp;{message}</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────
# 헤더
# ─────────────────────────────────────────────
st.markdown('<div class="main-title">🌻 수현 언니에게 💛</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">30일 동안 매일 열어봐 ☀️</div>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📅 오늘의 카드", "🗓️ 전체 보기", "🎬 영상 모음"])

# ══════════════════════════════════════════════
# 탭 1: 오늘의 카드
# ══════════════════════════════════════════════
with tab1:
    st.markdown("#### 오늘 며칠 차야? 👇")
    day = st.slider(
        label="날짜",
        min_value=1,
        max_value=30,
        value=1,
        step=1,
        format="%d일차",
        label_visibility="collapsed",
    )
    st.markdown("---")
    show_card(day)
    if day == 30:
        st.balloons()

# ══════════════════════════════════════════════
# 탭 2: 전체 보기
# ══════════════════════════════════════════════
with tab2:
    st.markdown("#### 보고 싶은 날 눌러봐 📋")
    cols_per_row = 5
    for row_start in range(0, 30, cols_per_row):
        cols = st.columns(cols_per_row)
        for i, col in enumerate(cols):
            d = row_start + i + 1
            if d > 30:
                break
            with col:
                e, _ = get_day_info(d)
                if st.button(f"{e}\n{d}일", key=f"btn_{d}", use_container_width=True):
                    st.session_state["selected_day"] = d

    if "selected_day" in st.session_state:
        st.markdown("---")
        show_card(st.session_state["selected_day"])

# ══════════════════════════════════════════════
# 탭 3: 영상 모음
# ══════════════════════════════════════════════
with tab3:
    st.markdown("#### 우리 인생네컷 모음 🎬")
    st.caption("소중한 영상들 💛")

    video_info = [
        ("video_01.MP4", "Day 19 — 언니랑 또 찍고 싶다 📸"),
        ("video_02.MP4", "Day 23 — 이날 다시 생각해도 웃겨 😂"),
        ("video_03.MP4", "Day 24 — 언니가 웃었으면 해서 💌"),
        ("video_04.MP4", "또 찍으러 가쟝 🎁"),
    ]

    for vfile, label in video_info:
        vpath = MEDIA_DIR / "videos" / vfile
        st.markdown(f"**{label}**")
        if vpath.exists():
            st.video(str(vpath))
        else:
            st.info(f"📂 `media/videos/{vfile}` 파일을 넣어줘!")
        st.markdown("---")

# ─────────────────────────────────────────────
# 푸터
# ─────────────────────────────────────────────
st.markdown("""
<div style='text-align:center; color:#F5A623; font-size:0.9rem; margin-top:2rem; font-family:Gaegu,cursive;'>
언니를 응원하는 희원이가 💛 꼭 이겨내자 🌻
</div>
""", unsafe_allow_html=True)
