import streamlit as st

st.set_page_config(page_title="Tin Học Online", layout="wide")

logo_url = "https://raw.githubusercontent.com/TuanHoang1229/web2/refs/heads/main/IMG_2935.JPG"
menu_items = ["Mua sách", "Giới thiệu", "Tủ sách", "Học liệu", "Bài giảng", "Đề kiểm tra"]

# --- CSS + HTML mới không có 3 gạch ---
navbar_html = f"""
<style>
.navbar {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    background-color: white;
    padding: 10px 20px;
    font-family: sans-serif;
    border-bottom: 2px solid #f0f0f0;
}}
.navbar-left {{
    display: flex;
    align-items: center;
}}
.navbar-left img {{
    height: 40px;
    margin-right: 10px;
}}
.navbar-left span {{
    font-size: 22px;
    font-weight: bold;
    color: #1a1a1a;
}}
.navbar-menu {{
    display: flex;
    gap: 30px;
}}
.navbar-menu a {{
    text-decoration: none;
    color: #1a1a1a;
    font-weight: 500;
    font-size: 16px;
    position: relative;
}}
.navbar-menu a:hover::after {{
    content: "";
    position: absolute;
    left: 0;
    bottom: -4px;
    width: 100%;
    height: 2px;
    background-color: #f58220;
}}
</style>

<div class="navbar">
    <div class="navbar-left">
        <img src="{logo_url}" alt="logo">
        <span>Tin Học Online</span>
    </div>
    <div class="navbar-menu">
"""

# Thêm mục menu vào HTML
for i, item in enumerate(menu_items):
    navbar_html += f'<a href="?menu={i}">{item}</a>'
navbar_html += "</div></div>"

# Hiển thị menu
st.markdown(navbar_html, unsafe_allow_html=True)

# Lấy menu đang chọn
params = st.query_params
menu_index = int(params.get("menu", 0))

# Nội dung các mục
if menu_index == 0:
    st.title("📘 Mua sách")
    st.markdown("Bạn có thể đặt mua các sách Tin học tại đây...")

elif menu_index == 1:
    st.title("📖 Giới thiệu")
    st.markdown("Trang web học tập Tin học hiện đại, hỗ trợ tự học hiệu quả.")

elif menu_index == 2:
    st.title("📚 Tủ sách")
    st.markdown("Danh sách tài liệu và sách tham khảo được phân loại.")

elif menu_index == 3:
    st.title("📂 Học liệu")
    st.markdown("Tổng hợp các bài tập, đề thi, slide bài giảng...")

elif menu_index == 4:
    st.title("🎓 Bài giảng")
    st.markdown("Video bài giảng và hướng dẫn thực hành.")

elif menu_index == 5:
    st.title("📝 Đề kiểm tra")
    st.markdown("Kiểm tra kiến thức qua các đề trắc nghiệm ngắn.")

