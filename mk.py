import streamlit as st

# --- Cấu hình trang ---
st.set_page_config(page_title="Tin Học Online", layout="wide")

# --- Logo & Tiêu đề ---
logo_url = "https://raw.githubusercontent.com/TuanHoang1229/web2/refs/heads/main/IMG_2935.JPG"

# --- Giao diện đầu trang ---
st.markdown(f"""
    <div style="display: flex; align-items: center; justify-content: space-between; padding: 10px 0;">
        <div style="display: flex; align-items: center;">
            <img src="{logo_url}" alt="Logo" width="60" style="margin-right: 10px;">
            <h2 style="margin: 0; color: #40E0D0;">Tin Học Online</h2>
        </div>
    </div>
    <hr style="margin-top: 0;">
""", unsafe_allow_html=True)

# --- Nút chọn chuyên đề ---
if st.button("📚 Chọn chuyên đề"):
    st.session_state.show_topics = not st.session_state.get("show_topics", False)

# --- Hiển thị danh sách chuyên đề dọc khi đã nhấn nút ---
if st.session_state.get("show_topics", False):
    topic = st.radio("📂 Danh sách chuyên đề:", [
        "🌐 Thiết kế Web cơ bản",
        "🔐 An toàn thông tin",
        "📂 Kho tài liệu",
        "🧠 Trắc nghiệm",
        "💬 Góc chia sẻ"
    ])
    
    # Hiển thị nội dung theo chuyên đề đã chọn
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
else:
    st.info("Nhấn nút '📚 Chọn chuyên đề' để bắt đầu.")
