import streamlit as st
import random
import string

# --- Cấu hình trang ---
st.set_page_config(page_title="Tin Học Online", layout="wide")

# --- Khởi tạo trạng thái ---
if "show_topics" not in st.session_state:
    st.session_state.show_topics = False

# --- Header + Nút chọn chuyên đề ---
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

# --- Ảnh banner ---
st.image(
    "https://scontent.fhan3-2.fna.fbcdn.net/v/t39.30808-6/304851178_540789087851004_9097165287000760892_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=cc71e4&_nc_ohc=gHy6kXCaw2AQ7kNvwE-PviU&_nc_oc=Admrg-I1Ihfs1OeVmhVMDCN2WjDhY-G92J9d7FWnfMrm3PH2DaIHFPtWsp3spMJ7lTA&_nc_zt=23&_nc_ht=scontent.fhan3-2.fna&_nc_gid=zUR1Tl_81MyfEa2IiZydTg&oh=00_AfJdAFQuQ6pb2wh4fVJ3RBHgdKJnQDRy9rhd0jvLBUbplQ&oe=6825F9BA",
    use_container_width=True,
    caption="📸 Trường THPT Lương Văn Tri"
)

# --- Hiển thị chuyên mục nếu được bật ---
if st.session_state.show_topics:
    selected_topics = st.multiselect("📌 Chọn các chuyên đề bạn muốn xem:", [
        "🏠 Trang chủ",
        "🔑 Kiểm tra mật khẩu",
        "🌐 Thiết kế Web cơ bản", 
        "🔐 An toàn thông tin",
        "📂 Kho tài liệu",
        "🧠 Trắc nghiệm",
        "💬 Góc chia sẻ"
    ])

    for topic in selected_topics:
        if topic == "🏠 Trang chủ":
            st.title("📘 Chào mừng bạn đến với Góc Tự Học Tin học")
            st.markdown("👉 Nội dung phần Trang chủ ở đây...")

        elif topic == "🔑 Kiểm tra mật khẩu":
            st.header("🔐 Kiểm tra & Tạo mật khẩu mạnh")

            def calculate_strength(password):
                score = 0
                if len(password) >= 8: score += 1
                if len(password) >= 12: score += 1
                if any(c.isdigit() for c in password): score += 1
                if any(c.islower() for c in password): score += 1
                if any(c.isupper() for c in password): score += 1
                if any(c in string.punctuation for c in password): score += 1
                return score

            password = st.text_input("Nhập mật khẩu của bạn để kiểm tra:", type="password")
            if password:
                strength = calculate_strength(password)
                if strength <= 2:
                    st.warning("⚠️ Mật khẩu yếu")
                elif strength <= 4:
                    st.info("🔐 Mật khẩu trung bình")
                else:
                    st.success("💪 Mật khẩu mạnh")

            if st.button("Tạo mật khẩu ngẫu nhiên"):
                generated_password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))
                st.write(f"🔑 Mật khẩu ngẫu nhiên: {generated_password}")

        elif topic == "🌐 Thiết kế Web cơ bản":
            st.header("🖥️ Thiết kế Web cơ bản với HTML & CSS")
            st.markdown("👉 Nội dung HTML/CSS ở đây...")

        elif topic == "🔐 An toàn thông tin":
            st.header("🔐 An toàn Thông tin")
            st.markdown("👉 Nội dung An toàn thông tin ở đây...")

        elif topic == "📂 Kho tài liệu":
            st.header("📚 Kho tài liệu")
            st.markdown("👉 Nội dung Kho tài liệu ở đây...")

        elif topic == "🧠 Trắc nghiệm":
            st.header("🧠 Trắc nghiệm tự luyện")
            st.markdown("👉 Nội dung Trắc nghiệm ở đây...")

        elif topic == "💬 Góc chia sẻ":
            st.header("📬 Góc chia sẻ - Gửi bài thực hành")
            st.markdown("[📎 Gửi bài tại đây](https://forms.gle/...)")
