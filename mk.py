import streamlit as st
import random
import string

st.set_page_config(page_title="Tin Học Online", layout="wide")

# --- Logo & Menu ---
logo_url = "https://raw.githubusercontent.com/TuanHoang1229/web2/refs/heads/main/IMG_2935.JPG"
menu = ["🏠 Trang chủ", "🔑 Kiểm tra mật khẩu", "🌐 Thiết kế Web", "🔐 An toàn thông tin", "📂 Kho tài liệu", "🧠 Trắc nghiệm", "💬 Góc chia sẻ"]

# --- CSS + HTML: Bố cục logo bên trái, nút ☰ bên phải ---
menu_html = f"""
<style>
.navbar {{
    background-color: #f8f9fa;
    padding: 10px 16px;
    border-radius: 10px;
    margin-bottom: 20px;
    font-weight: bold;
}}
.navbar-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    cursor: pointer;
}}
.navbar-left {{
    display: flex;
    align-items: center;
}}
.navbar-left img {{
    height: 40px;
    margin-right: 10px;
    border-radius: 6px;
}}
.navbar-title {{
    font-size: 20px;
}}
.navbar-toggle {{
    font-size: 26px;
    padding: 0 10px;
}}
.navbar-menu {{
    display: none;
    margin-top: 10px;
    flex-direction: column;
}}
.navbar-menu a {{
    padding: 6px 0;
    color: #333;
    text-decoration: none;
}}
.navbar-menu a:hover {{
    color: #40E0D0;
    text-decoration: underline;
}}
</style>

<script>
function toggleMenu() {{
    var menu = document.getElementById("menu-items");
    menu.style.display = (menu.style.display === "flex") ? "none" : "flex";
}}
</script>

<div class="navbar">
    <div class="navbar-header">
        <div class="navbar-left">
            <img src="{logo_url}" alt="Logo">
            <span class="navbar-title">Tin Học Online</span>
        </div>
        <div class="navbar-toggle" onclick="toggleMenu()">☰</div>
    </div>
    <div class="navbar-menu" id="menu-items">
"""

# Thêm các mục menu
for i, item in enumerate(menu):
    menu_html += f'<a href="?menu={i}">{item}</a>'
menu_html += "</div></div>"

# Hiển thị menu
st.markdown(menu_html, unsafe_allow_html=True)

# === Đổi cách lấy tham số URL (Streamlit mới) ===
params = st.query_params
menu_index = int(params.get("menu", 0))

# === Nội dung các mục ===
if menu_index == 0:
    st.title("📘 Chào mừng bạn đến với Góc Tự Học Tin học")
    st.markdown("""
Trang web này hỗ trợ học sinh học và thực hành các kỹ năng **Tin học hiện đại** như:

- 🌐 Thiết kế Web
- 🔐 An toàn thông tin
- 🔑 Kiểm tra mật khẩu

---

**📌 Mục tiêu:**  
- Học qua thực hành  
- Nâng cao kỹ năng tư duy và công nghệ

**📌 Hướng dẫn:**  
- Chọn chuyên mục ở thanh phía trên  
- Làm trắc nghiệm, xem tài liệu, chia sẻ bài làm của bạn!

> **“Công nghệ sẽ không thay thế giáo viên, nhưng giáo viên biết công nghệ sẽ thay thế người không biết.”**  
> – *Ray Clifford*
""")

elif menu_index == 1:
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

    password = st.text_input("Nhập mật khẩu của bạn:", type="password")
    if password:
        strength = calculate_strength(password)
        if strength <= 2:
            st.warning("⚠️ Mật khẩu yếu")
        elif strength <= 4:
            st.info("🔐 Mật khẩu trung bình")
        else:
            st.success("💪 Mật khẩu mạnh")

    if st.button("Tạo mật khẩu ngẫu nhiên"):
        new_pass = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))
        st.write(f"🔑 Mật khẩu mới: `{new_pass}`")

elif menu_index == 2:
    st.header("🖥️ Thiết kế Web cơ bản với HTML & CSS")
