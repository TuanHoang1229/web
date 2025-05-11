import streamlit as st

# --- Cấu hình trang ---
st.set_page_config(page_title="Tin Học Online", layout="wide")

# --- Khởi tạo trạng thái ---
if "show_topics" not in st.session_state:
    st.session_state.show_topics = False

# --- Layout logo + nút chuyên đề ---
col1, col2 = st.columns([7, 1.5])

with col1:
    st.markdown(f"""
        <div style="display: flex; align-items: center; height: 60px;">
            <img src="https://raw.githubusercontent.com/TuanHoang1229/web2/refs/heads/main/IMG_2935.JPG" width="50" style="margin-right: 12px;">
            <h2 style="color: #40E0D0; margin: 0;">Tin Học Online</h2>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("<div style='height: 24px;'></div>", unsafe_allow_html=True)
    if st.button("📚 Chọn chuyên đề"):
        st.session_state.show_topics = not st.session_state.show_topics

# --- Gạch ngang ---
st.markdown("<hr style='margin-top: 0;'>", unsafe_allow_html=True)

# --- Chuyên mục có thể chọn nhiều ---
topics_list = [
    "🌐 Thiết kế Web cơ bản",
    "🔐 An toàn thông tin",
    "📂 Kho tài liệu",
    "🧠 Trắc nghiệm",
    "💬 Góc chia sẻ"
]

# --- Nếu bật chuyên đề: hiển thị multiselect ---
if st.session_state.show_topics:
    selected_topics = st.multiselect("📂 Chọn các chuyên đề bạn quan tâm:", topics_list)

    for topic in selected_topics:
        st.subheader(topic)
        if topic == "🌐 Thiết kế Web cơ bản":
            st.write("📘 Hướng dẫn HTML, CSS, JS từ cơ bản đến nâng cao.")
        elif topic == "🔐 An toàn thông tin":
            st.write("🔒 Các kiến thức về bảo mật, phòng chống tấn công mạng.")
        elif topic == "📂 Kho tài liệu":
            st.write("📁 Tài liệu tham khảo, giáo trình, bài giảng...")
        elif topic == "🧠 Trắc nghiệm":
            st.write("📝 Các bộ đề trắc nghiệm luyện tập.")
        elif topic == "💬 Góc chia sẻ":
            st.write("💡 Chia sẻ kinh nghiệm, hỏi đáp, thảo luận học thuật.")

# --- Trang chủ nếu chưa chọn ---
else:
    st.subheader("🏠 Trang chủ")
    st.write("""
        👋 Chào mừng bạn đến với **Tin Học Online**!

        Đây là nền tảng học tập các kiến thức cơ bản và nâng cao về:
        - Thiết kế Web
        - An toàn thông tin
        - Trắc nghiệm luyện tập
        - Kho tài liệu bổ ích
        - Khu vực chia sẻ và giao lưu

        👉 Hãy nhấn **📚 Chọn chuyên đề** ở góc trên bên phải để bắt đầu!
    """)
