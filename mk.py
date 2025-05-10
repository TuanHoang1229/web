import streamlit as st

# --- Cấu hình trang ---
st.set_page_config(page_title="Tin Học Online", layout="wide")

# --- Khởi tạo trạng thái ---
if "show_topics" not in st.session_state:
    st.session_state.show_topics = False

# --- Layout ngang: logo bên trái, nút bên phải ---
col1, col2 = st.columns([6, 1])  # 6 phần logo + tiêu đề, 1 phần nút

with col1:
    st.markdown(f"""
        <div style="display: flex; align-items: center;">
            <img src="https://raw.githubusercontent.com/TuanHoang1229/web2/refs/heads/main/IMG_2935.JPG" width="60" style="margin-right: 10px;">
            <h2 style="color: #40E0D0; margin: 0;">Tin Học Online</h2>
        </div>
    """, unsafe_allow_html=True)

with col2:
    if st.button("📚 Chọn chuyên đề"):
        st.session_state.show_topics = not st.session_state.show_topics

st.markdown("<hr>", unsafe_allow_html=True)

# --- Hiển thị danh sách chuyên đề nếu đã nhấn nút ---
if st.session_state.show_topics:
    topic = st.radio("📂 Danh sách chuyên đề:", [
        "🌐 Thiết kế Web cơ bản",
        "🔐 An toàn thông tin",
        "📂 Kho tài liệu",
        "🧠 Trắc nghiệm",
        "💬 Góc chia sẻ"
    ])

    st.subheader(topic)
    if topic == "🌐 Thiết kế Web cơ bản":
        st.write("Hướng dẫn HTML, CSS, JS...")
    elif topic == "🔐 An toàn thông tin":
        st.write("Kiến thức bảo mật...")
    elif topic == "📂 Kho tài liệu":
        st.write("Tài liệu, giáo trình...")
    elif topic == "🧠 Trắc nghiệm":
        st.write("Luyện tập trắc nghiệm online.")
    elif topic == "💬 Góc chia sẻ":
        st.write("Nơi trao đổi, chia sẻ kinh nghiệm.")
