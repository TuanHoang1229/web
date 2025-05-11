import streamlit as st
import random
import string
import hashlib
from PIL import Image

# --- Cấu hình trang ---
st.set_page_config(page_title="Tin Học Online", layout="wide")

# --- Logo & Tiêu đề ---
logo_url = "https://raw.githubusercontent.com/TuanHoang1229/web2/refs/heads/main/IMG_2935.JPG"
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
topics = [
    "🏠 Trang chủ",
    "🔑 Kiểm tra mật khẩu",
    "🌐 Thiết kế Web cơ bản", 
    "🔐 An toàn thông tin",
    "📂 Kho tài liệu",
    "🧠 Trắc nghiệm",
    "💬 Góc chia sẻ",
]

selected_topic = st.selectbox("📂 Chọn chuyên đề:", topics)

# --- Trang Chủ ---
if selected_topic == "🏠 Trang chủ":
    st.title("📘 Chào mừng bạn đến với Góc Tự Học Tin học")
    st.markdown("""
### 💡 Giới thiệu:
Trang web này được xây dựng nhằm hỗ trợ học sinh THPT học tập và thực hành các kỹ năng **Tin học hiện đại** như:

- Thiết kế Web cơ bản với HTML/CSS
- An toàn thông tin
- Kiểm tra mật khẩu

---

### 🎯 Mục tiêu:
- Học qua thực hành
- Nâng cao tư duy logic và kỹ năng sử dụng máy tính
- Tự tin ứng dụng công nghệ trong học tập và đời sống

---

### 🗺️ Gợi ý phương pháp học tập:
1. **Bắt đầu với lý thuyết cơ bản**
2. **Xem video và làm bài tập**
3. **Làm trắc nghiệm ôn tập**
4. **Chia sẻ bài thực hành của bạn**
5. **Luyện kỹ các năng an toàn**
6. **Tăng cường mặt khẩu của bạn**\n**Lưu ý:** Bạn có thể chia sẻ các ý kiến cá nhân trong form nhaa!

--- 

### 🚀 Các chuyên mục nổi bật:
- [🔑 Kiểm tra mặt khẩu]
- [🔧 Thiết kế Web cơ bản]
- [🔐 An toàn thông tin]
- [📁 Kho tài liệu thực hành]
- [🧠 Trắc nghiệm tự luyện]
- [💬 Góc chia sẻ bài làm]

--- 

###  Hướng dẫn:
- Chọn các chuyên mục ở đầu trang.
- Mỗi mục có video, tài liệu và bài tập kèm theo.
- Đừng quên làm trắc nghiệm để kiểm tra kiến thức nhé!

--- 

> **“Công nghệ sẽ không thay thế giáo viên, nhưng giáo viên biết công nghệ sẽ thay thế người không biết.”**  
> – **Ray Clifford**
""")

# --- Kiểm tra mật khẩu ---
elif selected_topic == "🔑 Kiểm tra mật khẩu":
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

    # Tạo mật khẩu ngẫu nhiên
    if st.button("Tạo mật khẩu ngẫu nhiên"):
        generated_password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))
        st.write(f"🔑 Mật khẩu ngẫu nhiên: {generated_password}")

# --- Thiết kế Web ---
elif selected_topic == "🌐 Thiết kế Web cơ bản":
    st.header("🖥️ Thiết kế Web cơ bản với HTML & CSS")

    # Giới thiệu kiến thức
    st.markdown("""
    ### Giới thiệu nhanh:
    - **HTML**: Dùng để xây dựng cấu trúc trang web.
    - **CSS**: Dùng để tạo kiểu dáng (màu sắc, font chữ, bố cục).
    - Một số thẻ HTML cơ bản: `<h1>`, `<p>`, `<a>`, `<img>`, `<div>`
    - Một số thuộc tính CSS thường gặp: `color`, `font-size`, `margin`, `padding`, `background-color`
    """)

    # Ví dụ minh hoạ
    st.markdown("### Ví dụ đơn giản với HTML + CSS:")
    st.code("""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            h1 { color: blue; }
            p { font-size: 16px; }
        </style>
    </head>
    <body>
        <h1>Xin chào!</h1>
        <p>Đây là trang web đầu tiên của tôi.</p>
    </body>
    </html>
    """, language="html")

    # Nút tải file mẫu
    html_file = """
<!DOCTYPE html>
<html>
<head>
    <style>
        h1 { color: blue; }
        p { font-size: 16px; }
    </style>
</head>
<body>
    <h1>Xin chào!</h1>
    <p>Đây là trang web đầu tiên của tôi.</p>
</body>
</html>
"""
    st.download_button("Tải file HTML mẫu", html_file, file_name="mau_trang_web.html")

# --- An toàn thông tin ---
elif selected_topic == "🔐 An toàn thông tin":
    st.header("🔐 An toàn Thông tin")

    # Kiến thức cơ bản
    st.markdown("""
    ### Kiến thức cơ bản:
    - **Mật khẩu mạnh** nên có chữ hoa, chữ thường, số và ký tự đặc biệt.
    - **Không chia sẻ mật khẩu** qua email hay tin nhắn.
    - **Không nhấn vào liên kết lạ** trong email từ người lạ.
    - **Cập nhật phần mềm thường xuyên** để tránh lỗ hổng bảo mật.
    """)

# --- Kho tài liệu ---
elif selected_topic == "📂 Kho tài liệu":
    st.header("📚 Kho tài liệu")
    st.markdown("### Tài liệu PDF:")
    st.download_button("⬇️ Tải PDF bài giảng", "Nội dung giả định", file_name="baigiang.pdf")

# --- Trắc nghiệm ---
elif selected_topic == "🧠 Trắc nghiệm":
    st.header("🧠 Trắc nghiệm tự luyện")
    st.write("Trắc nghiệm nội dung tự luyện sẽ được thêm vào đây.")

# --- Góc chia sẻ ---
elif selected_topic == "💬 Góc chia sẻ":
    st.header("📬 Góc chia sẻ - Gửi bài thực hành")
    st.markdown("Gửi qua Google Forms dưới đây: [📎 Biểu mẫu gửi bài](https://forms.gle/...)")
