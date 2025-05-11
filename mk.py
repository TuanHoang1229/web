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

# --- Hiển thị chuyên đề nếu nhấn nút ---
if st.session_state.show_topics:
    st.markdown("""
        <div style="padding: 10px; background-color: #f0f0f0; border-radius: 8px; margin-top: 20px;">
            <h3>📚 Chọn chuyên đề:</h3>
            <ul style="list-style-type: none; padding-left: 0;">
                <li>🏠 Trang chủ</li>
                <li>🔑 Kiểm tra mật khẩu</li>
                <li>🌐 Thiết kế Web cơ bản</li>
                <li>🔐 An toàn thông tin</li>
                <li>📂 Kho tài liệu</li>
                <li>🧠 Trắc nghiệm</li>
                <li>💬 Góc chia sẻ</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

# --- Trang Chủ ---
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

> **“Công nghệ sẽ không thay thế giáo viên, nhưng giáo viên biết công nghệ sẽ thay thế người không biết.”**  
> – **Ray Clifford**
""")

# --- Thiết kế Web --- 
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

# Thử thách thực hành
st.markdown("""
### Thử thách:
Tạo một trang web có:
- Một tiêu đề lớn
- Một đoạn văn mô tả
- Một hình ảnh từ Internet
- Một liên kết đến Google

**Gợi ý:** Dùng các thẻ `<h1>`, `<p>`, `<img>`, `<a>`
""")

# Học thêm
st.markdown("""
### Tài liệu thêm:
- [Video hướng dẫn HTML cơ bản](https://www.youtube.com/watch?v=Ke90Tje7VS0)
- [Tài liệu CSS tại W3Schools](https://www.w3schools.com/css/)
""")

# Mini quiz
st.markdown("### Trắc nghiệm nhanh:")
q1 = st.radio("1. Thẻ nào dùng để tạo tiêu đề lớn nhất?", ["<p>", "<h1>", "<title>", "<div>"], key="web_q1")
q2 = st.radio("2. Thuộc tính nào để đổi màu chữ trong CSS?", ["font-size", "color", "background-color", "margin"], key="web_q2")

if st.button("Nộp câu trả lời", key="submit_web_quiz"):
    score = 0
    if q1 == "<h1>": score += 1
    if q2 == "color": score += 1
    st.success(f"✅ Bạn trả lời đúng {score}/2 câu.")
    if score == 2:
        st.balloons()

# --- An toàn thông tin ---
st.header("🔐 An toàn Thông tin")

# Kiến thức cơ bản
st.markdown("""
### Kiến thức cơ bản:
- **Mật khẩu mạnh** nên có chữ hoa, chữ thường, số và ký tự đặc biệt.
- **Không chia sẻ mật khẩu** qua email hay tin nhắn.
- **Không nhấn vào liên kết lạ** trong email từ người lạ.
- **Cập nhật phần mềm thường xuyên** để tránh lỗ hổng bảo mật.
""")

# Tình huống thực tế
st.markdown("""
### Tình huống:
Bạn nhận được email từ một địa chỉ lạ với tiêu đề "Bạn đã trúng thưởng!" và tệp đính kèm là file `.exe`.  
**Bạn nên làm gì?**
- Không mở tệp đính kèm
- Kiểm tra địa chỉ người gửi
- Báo cáo cho giáo viên hoặc quản trị mạng
""")

# Danh sách mẹo
st.markdown("""
### Mẹo an toàn khi dùng Internet:
- Sử dụng xác thực 2 yếu tố (2FA)
- Không dùng chung một mật khẩu cho nhiều tài khoản
- Không dùng Wi-Fi công cộng cho việc quan trọng
- Đăng xuất sau khi dùng xong máy tính công cộng
""")

# Học thêm
st.markdown("""
### Một số cách để phòng tránh:
- [Video: Làm sao để an toàn trên mạng?](https://www.youtube.com/watch?v=1I4FZ6Nkm4A)
- [Cẩm nang an toàn thông tin của VNPT](https://attt.vnpt.vn)
""")

# Trắc nghiệm nhỏ
st.markdown("### Trắc nghiệm nhanh:")
q1 = st.radio("1. Mật khẩu an toàn nên chứa?", [
    "Ngày sinh", "Chỉ chữ thường", "Ký tự đặc biệt, số, chữ hoa thường", "Tên người thân"
], key="sec_q1")

q2 = st.radio("2. Khi nhận được email lạ có tệp đính kèm, bạn nên?", [
    "Mở ngay để xem nội dung", "Xóa email và không mở tệp", "Chuyển tiếp cho bạn bè", "Trả lời email"
], key="sec_q2")

if st.button("Nộp câu trả lời", key="submit_sec_quiz"):
    score = 0
    if q1 == "Ký tự đặc biệt, số, chữ hoa thường": score += 1
    if q2 == "Xóa email và không mở tệp": score += 1
    st.success(f"✅ Bạn trả lời đúng {score}/2 câu.")

    if score == 2:
        st.balloons()
