import streamlit as st

# Cấu hình trang
st.set_page_config(page_title="Tin Học Online", layout="wide")

# URL logo
logo_url = "https://raw.githubusercontent.com/TuanHoang1229/web2/refs/heads/main/IMG_2935.JPG"

# Tạo menu ngang giả lập
menu_items = ["🏠 Trang chủ", "🔑 Kiểm tra mật khẩu", "🌐 Thiết kế Web cơ bản", 
              "🔐 An toàn thông tin", "📂 Kho tài liệu", "🧠 Trắc nghiệm", "💬 Góc chia sẻ"]

selected_tab = st.sidebar.radio("Chọn chuyên mục", menu_items)  # sidebar để điều hướng, hoặc dùng session_state nếu muốn menu ngang hoạt động như thật

# Giao diện phần đầu trang
st.markdown(f"""
    <div style="display: flex; align-items: center; justify-content: space-between;">
        <div style="display: flex; align-items: center;">
            <img src="{logo_url}" alt="Logo" width="60" style="margin-right: 10px;">
            <h2 style="margin: 0; color: #40E0D0;">Tin Học Online</h2>
        </div>
        <div style="display: flex; gap: 15px; font-size: 16px;">
            {''.join([f'<a href="?tab={i}" style="text-decoration:none; color:#333;">{item}</a>' for i, item in enumerate(menu_items)])}
        </div>
    </div>
    <hr>
""", unsafe_allow_html=True)

# Lấy tab từ query params
tab_index = int(st.query_params.get("tab", 0)) if "tab" in st.query_params else 0

# Hiển thị nội dung tương ứng
if tab_index == 0:
    st.write("🏠 Đây là Trang chủ")
elif tab_index == 1:
    st.write("🔑 Kiểm tra mật khẩu")
# ... và tiếp tục cho các tab khác
