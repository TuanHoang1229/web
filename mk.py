import streamlit as st

# --- Cấu hình trang ---
st.set_page_config(page_title="Tin Học Online", layout="wide")

# --- Khởi tạo trạng thái ---
if "show_topics" not in st.session_state:
    st.session_state.show_topics = False

# --- Logo + Nút chọn chuyên đề ---
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

st.image(
    "https://scontent.fhan3-2.fna.fbcdn.net/v/t39.30808-6/304851178_540789087851004_9097165287000760892_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=cc71e4&_nc_ohc=gHy6kXCaw2AQ7kNvwE-PviU&_nc_oc=Admrg-I1Ihfs1OeVmhVMDCN2WjDhY-G92J9d7FWnfMrm3PH2DaIHFPtWsp3spMJ7lTA&_nc_zt=23&_nc_ht=scontent.fhan3-2.fna&_nc_gid=zUR1Tl_81MyfEa2IiZydTg&oh=00_AfJdAFQuQ6pb2wh4fVJ3RBHgdKJnQDRy9rhd0jvLBUbplQ&oe=6825F9BA",
    use_container_width=True,
    caption="📸 Trường THPT Lương Văn Tri"
)


# --- Danh sách chuyên đề (có cả Trang chủ) ---
topics_list = [
    "🏠 Trang chủ",
    "🌐 Thiết kế Web cơ bản",
    "🔐 An toàn thông tin",
    "📂 Kho tài liệu",
    "🧠 Trắc nghiệm",
    "💬 Góc chia sẻ"
]

# --- Giao diện chọn chuyên đề ---
if st.session_state.show_topics:
    selected_topic = st.selectbox("📂 Chọn chuyên đề:", topics_list)

    st.subheader(selected_topic)

    if selected_topic == "🏠 Trang chủ":
        st.write("""
            👋 Chào mừng bạn đến với **Tin Học Online**!

            Đây là nền tảng học tập các kiến thức cơ bản và nâng cao về:
            - Thiết kế Web
            - An toàn thông tin
            - Trắc nghiệm luyện tập
            - Kho tài liệu bổ ích
            - Khu vực chia sẻ và giao lưu

            👉 Hãy chọn chuyên đề bạn quan tâm ở danh sách bên trên!
        """)
    elif selected_topic == "🌐 Thiết kế Web cơ bản":
        st.write("📘 Hướng dẫn HTML, CSS, JS từ cơ bản đến nâng cao.")
    elif selected_topic == "🔐 An toàn thông tin":
        st.write("🔒 Các kiến thức về bảo mật, phòng chống tấn công mạng.")
    elif selected_topic == "📂 Kho tài liệu":
        st.write("📁 Tài liệu tham khảo, giáo trình, bài giảng...")
    elif selected_topic == "🧠 Trắc nghiệm":
        st.write("📝 Các bộ đề trắc nghiệm luyện tập.")
    elif selected_topic == "💬 Góc chia sẻ":
        st.write("💡 Chia sẻ kinh nghiệm, hỏi đáp, thảo luận học thuật.")

# --- Nếu chưa bật menu: hiển thị Trang chủ mặc định ---
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
