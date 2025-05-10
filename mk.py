import streamlit as st

# --- Cấu hình trang ---
st.set_page_config(page_title="Tin Học Online", layout="wide")

# --- Logo & Tiêu đề ---
logo_url = "https://raw.githubusercontent.com/TuanHoang1229/web2/refs/heads/main/IMG_2935.JPG"

# --- Khởi tạo trạng thái toggle ---
if "show_topics" not in st.session_state:
    st.session_state.show_topics = False

# --- Xử lý toggle từ query_params ---
query_params = st.query_params
if "toggle" in query_params:
    st.session_state.show_topics = not st.session_state.show_topics
    st.query_params.clear()  # Xoá query để tránh lặp toggle khi reload

# --- Giao diện đầu trang với nút ở bên phải ---
st.markdown(f"""
    <div style="display: flex; align-items: center; justify-content: space-between; padding: 10px 5px;">
        <div style="display: flex; align-items: center;">
            <img src="{logo_url}" alt="Logo" width="60" style="margin-right: 10px;">
            <h2 style="margin: 0; color: #40E0D0;">Tin Học Online</h2>
        </div>
        <a href="?toggle=1">
            <button style="
                background-color: #40E0D0; 
                color: white; 
                border: none; 
                padding: 8px 16px; 
                font-size: 14px; 
                border-radius: 6px; 
                cursor: pointer;">
                📚 Chọn chuyên đề
            </button>
        </a>
    </div>
    <hr style="margin-top: 0;">
""", unsafe_allow_html=True)

# --- Hiển thị danh sách chuyên đề nếu đã bật ---
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
