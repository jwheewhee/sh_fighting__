import streamlit as st
from pathlib import Path

# ─────────────────────────────────────────────
# 페이지 기본 설정
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="언니에게 💛",
    page_icon="🌻",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
# 30일치 날짜별 데이터
#
# photo  : media/photos/ 안의 파일명  (없으면 None)
# video  : media/videos/ 안의 파일명  (없으면 None)
# youtube: 유튜브 전체 URL            (없으면 None)
#
# 우선순위: video > photo > youtube > 이모지
# ─────────────────────────────────────────────
DAY_DATA = {
    1: {
        "emoji": "🌱",
        "photo": None,
        "video": None,
        "youtube": None,
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
        "youtube": None,
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
        "youtube": "https://www.youtube.com/watch?v=BzYnNdJhZQw",
        "message": (
            "언니 오늘 수술 잘 받고 와!\n"
            "열심히 기도하고 있을게\n"
            "옆에 있진 못 하지만 응원 다 전해지도록 매시간마다 해야겠당 🙏🙏\n"
            "잘 될 거야 정말로!!!🍀🍀🍀🍀✨"
        ),
    },
    4: {
        "emoji": "☀️",
        "photo": None,
        "video": None,
        "youtube": "https://www.youtube.com/watch?v=lqAeYl05V2k",
        "message": (
            "언니 수술 받느라 진짜 고생 많았어!!\n"
            "눈 뜬 것만으로도 충분해\n"
            "아무것도 안 해도 되구 그냥 이렇게 숨 쉬고 있는 것만으로도\n"
            "정말 좋고 행복하다 ☀️"
        ),
    },
    5: {
        "emoji": "🤍",
        "photo": None,
        "video": None,
        "youtube": "https://www.youtube.com/watch?v=3VK5hdhfYfE",
        "message": (
            "중환자실.. 많이 낯설고 무섭지?\n"
            "모르는 곳에서 혼자 있는 느낌 들 것 같아서 걱정이 되네..\n"
            "근데 난 항상 응원하고 있고\n"
            "눈에 안 보여도 마음은 늘 옆에 있어 🤍"
        ),
    },
    6: {
        "emoji": "🛌",
        "photo": None,
        "video": None,
        "youtube": "https://www.youtube.com/watch?v=fWnno0ZFjRQ",
        "message": (
            "지금은 그냥 회복에만 집중!!!!\n"
            "다른 거 생각하지 말고 아무 걱정도 하지 말고!!\n"
            "언니 몸 낫는 게 지금 제일 중요한 일이야\n"
            "잘 먹고, 잘 자고, 잘 쉬어 🛌💛"
        ),
    },
    7: {
        "emoji": "🧸",
        "photo": None,
        "video": None,
        "youtube": "https://www.youtube.com/watch?v=jzo-Lm1mJSU",
        "message": (
            "아프면 아프다고 해도 돼\n"
            "힘들면 힘들다고 해도 되고 울어도 돼\n"
            "괜찮은 척 안 해도 되니까 혼자 참지마!!\n"
            "그 모습 그대로 다 괜찮아 🧸\n"
            "언니가 어떤 모습이라도 응원하는 \n"
            "사람이 많다는 걸 기억해조 ㅎㅎ🍀"
        ),
    },
    8: {
        "emoji": "🎉",
        "photo": "photo_01.JPG",
        "video": None,
        "youtube": None,
        "message": (
            "우리 이때는 좀 어색했는데!\n"
            "근데 있잖아 ~ 나는 이때도 언니가 진짜 정말 좋았어 ㅎㅎ\n"
            "(두쫀쿠 줘서 그런거 아니고..ㅎㅎ) \n"
            "좀 어색했어도 뭔가 통하는 느낌? >_<"
            "다 나으면 연말 파티 하자!!🎉"
        ),
    },
    9: {
        "emoji": "🌈",
        "photo": None,
        "video": None,
        "youtube": "https://www.youtube.com/watch?v=z5bayJX4MTg",
        "message": (
            "비 온 다음 날에는 항상 하늘이 예쁘거나\n"
            "환한 무지개가 뜨잖아!\n"
            "지금 언니한테 비가 많이 오고 있을지라도 \n"
            "곧 엄청나게 예쁜 무지개가 뜰거야 🌈\n"
            "그때까지 난 매일 기도할게"
        ),
    },
    10: {
        "emoji": "🌙",
        "photo": None,
        "video": None,
        "youtube": "https://www.youtube.com/watch?v=iD7wekhUE7I",
        "message": (
            "오늘 하루도 정말 수고했어!\n"
            "오늘도! 내일도! 그 다음날도!!!\n"
            "오늘 밤 푹 자 🌙 내일도 파이팅이야 💛"
        ),
    },
    11: {
        "emoji": "🌻",
        "photo": None,
        "video": None,
        "youtube": "https://www.youtube.com/watch?v=uw5s25PcSPE",
        "message": (
            "해바라기는 항상 해를 바라보잖아!\n"
            "언니가 딱 그래\n"
            "힘들어도 밝은 쪽으로 고개 드는 사람 ㅎㅎ\n"
            "항상 힘내자앙 🌻"
        ),
    },
    12: {
        "emoji": "😊",
        "photo": None,
        "video": None,
        "youtube": "https://www.youtube.com/watch?v=D54StAZFUrc",
        "message": (
            "언니 웃는 거 진짜 예쁜 거 알아?\n"
            "그래서 언니랑 있으면 더 재밌고 좋았나봐 ㅎ\n"
            "지금 이거 보면서 한 번 웃자!!\n"
            "언니 웃는 거 보고 싶어서 그래 😊💛"
        ),
    },
    13: {
        "emoji": "😂",
        "photo": "photo_02.jpg",
        "video": None,
        "youtube": None,
        "message": (
            "이거 다시 봐도 진짜 웃기지 않아?? 😂\n"
            "동성 배경 ㅠㅠ 너무 웃겨요\n"
            "웃느라 광대 아팠는데 ㅋㅋㅋ\n"
            "오늘도 이거 보고 또 웃쟈!!"
        ),
    },
    14: {
        "emoji": "🌤️",
        "photo": None,
        "video": None,
        "youtube": "https://www.youtube.com/watch?v=wR8zBI2DA3M",
        "message": (
            "오늘 잠깐 창문 열고 하늘 한번 봐\n"
            "구름이 있든 맑든 상관없이\n"
            "그 하늘 아래 나도 언니 생각하면서 같은 하늘 보고 있어 🌤️\n"
            "멀어도 연결돼있는 느낌 들지 않아? 💛"
        ),
    },
    15: {
        "emoji": "🍀",
        "photo": None,
        "video": None,
        "youtube": "https://www.youtube.com/watch?v=O-1FpjPP6_c",
        "message": (
            "오늘의 행운은 전부 다 언니 거야!!\n"
            "내 것까지 다 빌어줬거든🍀🍀🍀🍀🍀\n"
            "오늘 좋은 일 하나는 꼭 있을 거야\n"
            "아주 작은 거라도 발견해봐 😊"
        ),
    },
    16: {
        "emoji": "💌",
        "photo": "photo_03.jpg",
        "video": None,
        "youtube": None,
        "message": (
            "언니가 깜짝 꽃 선물 해줬을 때 얼마나 감동이었는지..\n"
            "언니 응원 덕분에 정말 기분 좋았엉 ㅎㅎ\n"
            "이제 내 차례야 🍀\n"
            "나도 열심히 응원하고 있어!!💌💛"
        ),
    },
    17: {
        "emoji": "🎶",
        "photo": None,
        "video": None,
        "youtube": "https://www.youtube.com/watch?v=uuGtrxDsrws",
        "message": (
            "오늘은 그냥 쉬어\n"
            "내가 좋아하는 노래 하나 추천해줄게 ㅎㅎ\n"
            "노래도 치료야!! 🎶\n"
            "언니가 제일 좋아하는 노래는 뭔지 나중에 알려줘 😊"
        ),
    },
    18: {
        "emoji": "🤝",
        "photo": None,
        "video": None,
        "youtube": "https://www.youtube.com/watch?v=D9UoOkoGfvI",
        "message": (
            "언니 애착인형 잘 붙들고 있쥥?\n"
            "애착인형도 언니 열심히 응원하고 있을거얌 ㅎㅎ\n"
            "나도 열심히 기도중!!\n"
            "회복되면 바로 달려갈게 💨💛"
        ),
    },
    19: {
        "emoji": "📸",
        "photo": None,
        "video": "video_01.MP4",
        "youtube": None,
        "message": (
            "언니랑 사진 또 찍고 싶다!\n"
            "우리 진짜 너무 귀엽잖아 ~~ 봐봐 ㅋㅋㅋ 📸\n"
            "얼른 나와서 또 찍쟝\n"
            "다음엔 더 재밌게 찍어보자 😆💛"
        ),
    },
    20: {
        "emoji": "🍽️",
        "photo": "photo_04.jpg",
        "video": None,
        "youtube": None,
        "message": (
            "언니 지금부터 먹고 싶은 거 리스트 적어놔!\n"
            "언니를 위해서라면 뭐든지 다 사줄 수 있어 헤헤\n"
            "맛있는 거 잔뜩 먹자 🍽️\n"
            "제일 먹고 싶은 거 1순위가 몰까용 ~~"
        ),
    },
    21: {
        "emoji": "🌊",
        "photo": None,
        "video": None,
        "youtube": "https://www.youtube.com/watch?v=K_8ITDLT4G8",
        "message": (
            "파도가 강하게 칠수록 모래사장이 더 단단해진대\n"
            "지금 언니한테 파도가 엄청 세게 치고 있는 거 알아\n"
            "근데 그만큼 언니도 더 단단해지고 있어!! 🌊\n"
            "나는 그걸 알기 때문에 믿어🍀🍀"
        ),
    },
    22: {
        "emoji": "⭐",
        "photo": None,
        "video": None,
        "youtube": "https://www.youtube.com/watch?v=jz8EucFSkxc",
        "message": (
            "오늘 하루도 진짜 고생 많았어 ~\n"
            "언니 지금 정말 잘 하고 있어!!\n"
            "스스로한테 오늘 수고했다고 한 번 말해줘 ⭐\n"
            "나도 말해줄게 ~ 언니 오늘도 최고야 💛"
        ),
    },
    23: {
        "emoji": "😂",
        "photo": None,
        "video": "video_02.mp4",
        "youtube": None,
        "message": (
            "이날 다시 생각해도 진짜 웃기지 않아?? 😂\n"
            "우리 이제 저기 마스터 됐으니까\n"
            "다 나으면 다시 찍으러 가자 ㅋㅋㅋ\n"
            "진짜 또 가야 해!!!!"
        ),
    },
    24: {
        "emoji": "💌",
        "photo": None,
        "video": "video_03.MP4",
        "youtube": None,
        "message": (
            "이 메시지들 보면서 언니가 한 번이라도 웃었으면 좋겠어\n"
            "조금이라도 힘이 났으면 좋겠당 ㅎㅎ\n"
            "그게 내가 이거 만든 이유야 💌\n"
            "언니 행복했으면 좋겠어 ㅎㅎ"
        ),
    },
    25: {
        "emoji": "🌈",
        "photo": None,
        "video": None,
        "youtube": "https://www.youtube.com/watch?v=SNn_H_Q2moo",
        "message": (
            "지금 이 힘든 시간이 지나면\n"
            "나중에 기쁠 때 더 크게 기쁠 수 있어!\n"
            "지금 버티는 언니가 나중에 더 환하게 웃을 거야 🌈\n"
            "그 모습 꼭 보고 싶어 💛"
        ),
    },
    26: {
        "emoji": "🙌",
        "photo": None,
        "video": None,
        "youtube": "https://www.youtube.com/watch?v=CTpbD4Y0IFU",
        "message": (
            "오늘도 잘 버텨줘서 진짜 고마워\n"
            "매일 여기 열어보는 것도 나한텐 언니가 열심히 하고 있다는 신호야 🙌\n"
            "멋지다 우리 언닝"
        ),
    },
    27: {
        "emoji": "😤",
        "photo": "photo_05.JPG",
        "video": None,
        "youtube": None,
        "message": (
            "이거 다시 봐도 진짜 너무하지 않아?? 😤\n"
            "글씨색도..사진 선택도..!!!!!\n"
            "우리 이거 보고 얼마나 황당했는지 ㅋㅋㅋ\n"
            "이런 추억도 다 나중에 웃긴 얘기 되는 거야 😂"
        ),
    },
    28: {
        "emoji": "💐",
        "photo": "photo_06.JPG",
        "video": None,
        "youtube": None,
        "message": (
            "언니가 병원에서 젤 예쁠듯 ~~💐\n"
            "오늘도 한번 웃어봐\n"
            "(아.. 그럼 사람들이 다 반하려나 막이래)\n"
            "파이팅 언니!! 거의 다 왔어 💛"
        ),
    },
    29: {
        "emoji": "🎊",
        "photo": None,
        "video": None,
        "youtube": "https://www.youtube.com/watch?v=19oT04OuBhg",
        "message": (
            "지금 여기까지 왔다면 언니 정말 멋지다!\n"
            "내 진심을 열심히 담았는데 잘 전달 됐으면 좋겠당\n"
            "응원이 됐나용 ㅎㅎ\n"
            "이렇게 난 항상 언니 옆에서 응원할거야!!"
        ),
    },
    30: {
        "emoji": "🌻",
        "photo": "photo_07.jpg",
        "video": None,
        "youtube": None,
        "message": (
            "우리 피크닉 또 가자 🌻\n"
            "이번엔 다른 데로! 더 예쁜 데 찾아서!\n"
            "언니 나으면 여행도 가구 ~\n"
            "그날만 기다리는중 ㅎㅎ 💛\n\n"
            "언니 30일 동안 정말 수고 많았어!\n"
            "앞으로도 잘 이겨내보쟈 진짜 다 잘 될 거야 ~~🍀\n"
            "나는 항상 언니 편이야!! 지금도, 앞으로도, 영원히🌻"
        ),
    },
}

# ─────────────────────────────────────────────
# 추억 모음집 — 사진 + 영상 전체 목록
# label: 탭3에서 보여줄 제목
# ─────────────────────────────────────────────
MEMORY_COLLECTION = [
    {"type": "photo", "file": "photo_01.JPG", "label": "Day 8 — 메리연남크리스마스 🎉"},
    {"type": "photo", "file": "photo_02.jpg", "label": "Day 13 — 동성 배경 ㅋㅋ 😂"},
    {"type": "photo", "file": "photo_03.jpg", "label": "Day 16 — 언니한테 감동 받은 날 💌"},
    {"type": "video", "file": "video_01.MP4", "label": "Day 19 — 인생네컷 타임랩스 1 📸"},
    {"type": "photo", "file": "photo_04.jpg", "label": "Day 20 — 맛있는 거 먹은 날 🍽️"},
    {"type": "video", "file": "video_02.MP4", "label": "Day 23 — 인생네컷 타임랩스 2 😂"},
    {"type": "video", "file": "video_03.MP4", "label": "Day 24 — 언니가 웃었으면 해서 💌"},
    {"type": "photo", "file": "photo_05.JPG", "label": "Day 27 — 너무하다 저기 증말(?) 😤"},
    {"type": "photo", "file": "photo_06.JPG", "label": "Day 28 — 언니 제일 예뻐 💐"},
    {"type": "photo", "file": "photo_07.jpg", "label": "Day 30 — 피크닉 또 가자 🌻"},
    {"type": "video", "file": "video_04.MP4", "label": "또 찍쟝 🎁"},
]

EMOJI_FALLBACK = ["🌻", "🌸", "🍊", "💛", "🌈", "☀️", "🌺", "🎀", "🍀", "🌙",
                  "✨", "💌", "🌷", "🌱", "⭐", "🎶", "🤍", "🌊", "💪", "🎊"]

MEDIA_DIR = Path("media")

# ─────────────────────────────────────────────
# CSS 스타일
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gaegu:wght@400;700&family=Noto+Sans+KR:wght@400;700&display=swap');

html, body, [class*="css"] { font-family: 'Noto Sans KR', sans-serif; }
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
.nav-hint {
    text-align: center;
    color: #F5A623;
    font-size: 0.85rem;
    margin-bottom: 0.5rem;
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
# session_state 초기화
# ─────────────────────────────────────────────
if "current_day" not in st.session_state:
    st.session_state["current_day"] = 1   # 마지막 본 날짜 기억

if "active_tab" not in st.session_state:
    st.session_state["active_tab"] = "card"  # card / gallery

# ─────────────────────────────────────────────
# 헬퍼 함수
# ─────────────────────────────────────────────
def get_media(day: int):
    data = DAY_DATA.get(day, {})
    photo_file = data.get("photo")
    video_file = data.get("video")
    youtube_url = data.get("youtube")

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

    return photo_path, video_path, youtube_url

def get_day_info(day: int):
    data = DAY_DATA.get(day, {})
    emoji = data.get("emoji", EMOJI_FALLBACK[(day - 1) % len(EMOJI_FALLBACK)])
    message = data.get("message", "오늘도 언니 응원해 💛")
    return emoji, message

def show_card(day: int):
    emoji, message = get_day_info(day)
    photo_path, video_path, youtube_url = get_media(day)

    st.markdown(f'<div class="day-badge">Day {day} 💛</div>', unsafe_allow_html=True)

    # 미디어 우선순위: 로컬 영상 > 로컬 사진 > 유튜브 > 이모지
    if video_path:
        st.video(video_path)
    elif photo_path:
        st.image(photo_path, use_container_width=True)
    elif youtube_url and "여기에URL" not in youtube_url:
        st.video(youtube_url)
    else:
        st.markdown(f'<div class="emoji-bg">{emoji}</div>', unsafe_allow_html=True)

    st.markdown(f'<div class="message-box">{emoji}&nbsp;&nbsp;{message}</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────
# 헤더
# ─────────────────────────────────────────────
st.markdown('<div class="main-title">🌻 언니에게 💛</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">30일 동안 매일 열어봐 ☀️</div>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📅 오늘의 카드", "🗓️ 전체 보기", "📷 추억 모음집"])

# ══════════════════════════════════════════════
# 탭 1: 오늘의 카드
# ══════════════════════════════════════════════
with tab1:

    # 좌우 버튼 + 날짜 표시
    col_left, col_mid, col_right = st.columns([1, 3, 1])

    with col_left:
        if st.button("◀ 이전", key="prev", use_container_width=True):
            if st.session_state["current_day"] > 1:
                st.session_state["current_day"] -= 1

    with col_mid:
        st.markdown(
            f"<div style='text-align:center; font-size:1.1rem; font-weight:700; color:#E8720C; padding-top:0.4rem;'>"
            f"Day {st.session_state['current_day']} / 30</div>",
            unsafe_allow_html=True,
        )

    with col_right:
        if st.button("다음 ▶", key="next", use_container_width=True):
            if st.session_state["current_day"] < 30:
                st.session_state["current_day"] += 1

    st.markdown(
        '<div class="nav-hint">◀ 왼쪽 = 전날 &nbsp;|&nbsp; 오른쪽 = 다음날 ▶</div>',
        unsafe_allow_html=True,
    )
    st.markdown("---")

    show_card(st.session_state["current_day"])

    if st.session_state["current_day"] == 30:
        st.balloons()

# ══════════════════════════════════════════════
# 탭 2: 전체 보기
# ══════════════════════════════════════════════
with tab2:
    st.markdown("#### 보고 싶은 날 눌러봐 📋")
    st.caption("누르면 바로 그날 카드로 이동해!")

    cols_per_row = 5
    for row_start in range(0, 30, cols_per_row):
        cols = st.columns(cols_per_row)
        for i, col in enumerate(cols):
            d = row_start + i + 1
            if d > 30:
                break
            with col:
                e, _ = get_day_info(d)
                # 현재 보고 있는 날 강조
                label = f"**{e}**\n{d}일" if d == st.session_state["current_day"] else f"{e}\n{d}일"
                if st.button(label, key=f"btn_{d}", use_container_width=True):
                    st.session_state["current_day"] = d
                    # 탭1(오늘의 카드)으로 이동 안내
                    st.success(f"Day {d} 선택됐어! '📅 오늘의 카드' 탭 눌러봐 💛")

# ══════════════════════════════════════════════
# 탭 3: 추억 모음집
# ══════════════════════════════════════════════
with tab3:
    st.markdown("#### 우리 추억 모음집 📷")
    st.caption("사진이랑 영상 다 모아뒀어 💛")

    for item in MEMORY_COLLECTION:
        st.markdown(f"**{item['label']}**")

        if item["type"] == "photo":
            p = MEDIA_DIR / "photos" / item["file"]
            if p.exists():
                st.image(str(p), use_container_width=True)
            else:
                st.info(f"📂 `media/photos/{item['file']}` 파일을 넣어줘!")

        elif item["type"] == "video":
            v = MEDIA_DIR / "videos" / item["file"]
            if v.exists():
                st.video(str(v))
            else:
                st.info(f"📂 `media/videos/{item['file']}` 파일을 넣어줘!")

        st.markdown("---")

# ─────────────────────────────────────────────
# 푸터
# ─────────────────────────────────────────────
st.markdown("""
<div style='text-align:center; color:#F5A623; font-size:0.9rem; margin-top:2rem; font-family:Gaegu,cursive;'>
언니를 응원하는 희원이가 💛 꼭 이겨내자 🌻
</div>
""", unsafe_allow_html=True)
