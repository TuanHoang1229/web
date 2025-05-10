import streamlit as st

st.set_page_config(page_title="Tin Học Online", layout="wide")

logo_url = "https://raw.githubusercontent.com/TuanHoang1229/web2/refs/heads/main/IMG_2935.JPG"

menu_items = ["Mua sách", "Giới thiệu", "Tủ sách", "Học liệu", "Bài giảng", "Đề kiểm tra"]
submenu_items = ["Về chúng tôi", "Sứ mệnh", "Liên hệ"]

if "current_page" not in st.session_state:
    st.session_state.current_page = "Trang chủ"

# --- HTML Navbar với Dropdown ---
navbar_html = f"""
<style>
.navbar {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    background-color: white;
    padding: 10px 20px;
    font-family: sans-serif;
    border-bottom: 1px solid #eee;
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
    position: relative;
}}
.menu-item {{
    position: relative;
}}
.menu-button {{
    background: none;
    border: none;
    font-size: 16px;
    font-weight: 500;
    color: #1a1a1a;
    cursor: pointer;
    padding: 5px;
}}
.menu-button:hover {{
    color: #f58220;
}}
.dropdown {{
    display: none;
    position: absolute;
    top: 35px;
    left: 0;
    background-color: white;
    border: 1px solid #ddd;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    z-index: 10;
}}
.menu-item:hover .dropdown {{
    display: block;
}}
.dropdown button {{
    background: none;
    border: none;
    padding: 8px 20px;
    width: 150px;
    text-align: left;
    font-size: 15px;
    cursor: pointer;
}}
.dropdown button:hover {{
    background-color: #f2f2f2;
}}
.breadcrumb {{
    margin: 10px 20px;
    font-size: 14px;
    color: #666;
    font-family: sans-serif;
}}
.breadcrumb span {{
    cursor: pointer;
    color: #1a73e8;
}}
.breadcrumb span:hover {{
    text-decoration: underline;
}}
</style>

<div class="navbar">
    <div class="navbar-left">
        <img src="{logo_url}" alt="logo">
        <span>Tin Học Online</span>
    </div>
    <div class="navbar-menu">
        <form method="post"><button name="menu" value="Mua sách" class="menu-button">Mua sách</button></form>
        <div class="menu-item">
            <button class="menu-button">Giới thiệu ▼</button>
            <div class="dropdown">
"""

for sub in submenu_items:
    navbar_html += f"""<form method="post"><button name="menu" value="{sub}">{sub}</button></form>"""

navbar_html += """
            </div>
        </div>
        <form method="post"><button name="menu" value="Tủ sách" class="menu-button">Tủ sách</button></form>
        <form method="post"><button name="menu" value="Học liệu" class="menu-button">Học liệu</button></form>
        <form method="post"><button name="menu" value="Bài giảng" class="menu-button">Bài giảng</button></form>
        <form method="post"><button name="menu" value="Đề kiểm tra" class="menu-button">Đề kiểm tra</button></form>
    </div>
</div>
"""

# Breadcrumb
breadcrumb_html = f"""<div class="breadcrumb"><span onclick="window.location.reload()">Trang chủ</span>"""
if st.session_state.current_page != "Trang chủ":
    breadcrumb_html += f" › {st.session_state.current_page}"
breadcrumb_html += "</div>"

# Hiển thị HTML
st.markdown(navbar_html, unsafe_allow_html=True)
st.markdown(breadcrumb_html, unsafe_allow_html=True)

# Cập nhật nội dung nếu có click
if st.session_state.get("menu") is not None:
    st.session_state.current_page = st.session_state.menu

# Nội dung trang
page = st.session_state.current_page

if page == "Trang chủ":
    st.markdown("""
        <div style="position: relative; text-align: center; color: white;">
            <img src="https://hoc10.monkeyuni.net/upload/hoc10/thumb/Artboard4.png" 
                 style="width: 100%; height: auto; border-radius: 10px;">
            <div style="position: absolute; top: 50%; left: 50%;
                        transform: translate(-50%, -50%);
                        font-size: 36px; font-weight: bold; background-color: rgba(0,0,0,0.4); padding: 10px 20px; border-radius: 10px;">
                Học Tin Học Online
            </div>
            <div style="position: absolute; top: 60%; left: 50%;
                        transform: translate(-50%, -50%);
                        font-size: 24px; font-weight: normal; background-color: rgba(0,0,0,0.6); padding: 8px 16px; border-radius: 10px;">
                Chương trình học đa dạng, dễ tiếp cận.
            </div>
            <div style="position: absolute; top: 70%; left: 50%;
                        transform: translate(-50%, -50%);
                        font-size: 20px; font-weight: normal; background-color: rgba(0,0,0,0.6); padding: 8px 16px; border-radius: 10px;">
                Học mọi lúc, mọi nơi với tài liệu phong phú.
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.title("🎓 Chào mừng đến với Tin Học Online")
    st.write("Trang web học tập, ôn luyện và chia sẻ tài liệu Tin học.")
elif page == "Mua sách":
    st.title("📘 Mua sách")
    st.write("Bạn có thể đặt mua các sách Tin học tại đây...")
elif page == "Tủ sách":
    st.title("📚 Tủ sách")
    st.write("Tủ sách bao gồm nhiều tài liệu học tập hữu ích.")
elif page == "Học liệu":
    st.title("📂 Học liệu")
    st.write("Tổng hợp các tài liệu học tập đa dạng.")
elif page == "Bài giảng":
    st.title("🎓 Bài giảng")
    st.write("Video và bài giảng chất lượng cao.")
elif page == "Đề kiểm tra":
    st.title("📝 Đề kiểm tra")
    st.write("Kiểm tra kiến thức với các đề kiểm tra.")
elif page == "Về chúng tôi":
    st.title("ℹ️ Về chúng tôi")
    st.write("Thông tin về nhóm phát triển và mục tiêu của trang.")
elif page == "Sứ mệnh":
    st.title("🎯 Sứ mệnh")
    st.write("Sứ mệnh của chúng tôi là giúp học sinh yêu thích Tin học.")
elif page == "Liên hệ":
    st.title("📞 Liên hệ")
    st.write("Bạn có thể liên hệ qua email hoặc fanpage.")
