import streamlit as st

# --- 페이지 설정 ---
st.set_page_config(
    page_title="MBTI 도서 추천기",
    page_icon="📚",
    layout="centered"
)

# --- 제목 영역 ---
st.title("📖 당신의 MBTI에 맞는 신간 책 추천")
st.caption("당신의 성격 유형에 딱 맞는 신간 도서 3권을 추천해드려요!")

# --- MBTI 목록 ---
mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# --- 추천 도서 데이터 (예시) ---
book_recommendations = {
    "INTJ": ["《미래의 지배자》", "《전략적 사고의 기술》", "《혼자 있는 시간의 힘》"],
    "INTP": ["《생각하는 힘, 노는 뇌》", "《AI 시대의 인간 본성》", "《이과형 인간의 철학 산책》"],
    "ENTJ": ["《탁월한 리더의 조건》", "《지금 당장 실행하라》", "《성공하는 CEO의 습관》"],
    "ENTP": ["《창의성의 탄생》", "《토론의 기술》", "《무질서의 힘》"],
    "INFJ": ["《조용한 열정》", "《감정의 온도》", "《내면을 들여다보는 시간》"],
    "INFP": ["《당신이 빛나는 순간》", "《시를 잊은 그대에게》", "《유리멘탈을 위한 심리수업》"],
    "ENFJ": ["《사람의 마음을 움직이는 대화법》", "《함께 성장하는 관계》", "《리더는 사랑으로 말한다》"],
    "ENFP": ["《모든 것이 흥미로운 나에게》", "《오늘은 어디로 튈까》", "《재미있게 살고 있습니다》"],
    "ISTJ": ["《논리로 말하는 습관》", "《기록의 힘》", "《정확함의 미학》"],
    "ISFJ": ["《소소하지만 확실한 배려》", "《따뜻한 말 한마디》", "《조용한 헌신의 가치》"],
    "ESTJ": ["《체계적으로 일 잘하는 법》", "《관리자의 심리학》", "《업무의 본질》"],
    "ESFJ": ["《함께일 때 더 행복한》", "《사람 중심의 대화》", "《따뜻한 조직 만들기》"],
    "ISTP": ["《문제해결의 기술》", "《도전의 기계들》", "《혼자서도 잘해요》"],
    "ISFP": ["《감성의 조각들》", "《예술가의 마음》", "《소박한 삶의 예술》"],
    "ESTP": ["《지금 이 순간을 살아라》", "《액션 먼저, 생각은 나중에》", "《움직이는 인간》"],
    "ESFP": ["《인생은 파티야》", "《나답게 빛나는 법》", "《오늘도 반짝이는 너에게》"],
}

# --- 사용자 입력 ---
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_list)

# --- 추천 결과 ---
if selected_mbti:
    st.subheader(f"✨ {selected_mbti} 유형에게 추천하는 책")
    books = book_recommendations.get(selected_mbti, [])
    for book in books:
        st.markdown(f"📘 **{book}**")

# --- 푸터 ---
st.markdown("---")
st.caption("Made with ❤️ by 선생님과 ChatGPT")

