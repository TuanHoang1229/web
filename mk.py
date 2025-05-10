import streamlit as st

# --- Cấu hình trang ---
st.set_page_config(page_title="Tin Học Online", layout="wide")

# --- Logo & Tiêu đề ---
logo_url = "https://raw.githubusercontent.com/TuanHoang1229/web2/refs/heads/main/IMG_2935.JPG"

# --- Danh sách chuyên mục ---
menu_items = [
    ("🏠 Trang chủ", 0),
    ("🔑 Kiểm tra mật khẩu", 1),
    ("🌐 Thiết kế Web cơ bản", 2),
    ("🔐 An toàn thông tin", 3),
    ("📂 Kho tài liệu", 4),
    ("🧠 Trắc nghiệm", 5),
    ("💬 Góc chia sẻ", 6),
]

# --- Đọc tab hiện tại từ query params ---
query_params = st.query_params
tab_index = int(query_params.get("tab", 0)) if "tab" in query_params else 0

# --- Giao diện đầu trang với menu ngang ---
st.markdown(f"""
    <div style="display: flex; align-items: center; justify-content: space-between; padding: 10px 0;">
        <div style="display: flex; align-items: center;">
            <img src="{logo_url}" alt="Logo" width="60" style="margin-right: 10px;">
        </div>
        <div style="display: flex; gap: 20px; font-size: 16px;">
            {''.join([f'<a href="?tab={i}" style="text-decoration:none; color:{"#40E0D0" if i==tab_index else "#000"};">{name}</a>' for name, i in menu_items])}
        </div>
    </div>
    <hr style="margin-top: 0;">
""", unsafe_allow_html=True)

# --- Nội dung tương ứng từng chuyên mục ---
if tab_index == 0:
    st.subheader("🏠 Trang chủ")
    st.write("Chào mừng bạn đến với Tin Học Online!")
elif tab_index == 1:
    st.subheader("🔑 Kiểm tra mật khẩu")
    st.write("Nhập mật khẩu để kiểm tra độ mạnh...")
elif tab_index == 2:
    st.subheader("🌐 Thiết kế Web cơ bản")
    st.write("Học HTML, CSS, JS cơ bản tại đây.")
elif tab_index == 3:
    st.subheader("🔐 An toàn thông tin")
    st.write("Các kiến thức về bảo mật, an toàn khi sử dụng internet.")
elif tab_index == 4:
    st.subheader("📂 Kho tài liệu")
    st.write("Tổng hợp tài liệu học tập, ebook, giáo trình...")
elif tab_index == 5:
    st.subheader("🧠 Trắc nghiệm")
    st.write("Làm bài kiểm tra để ôn luyện kiến thức.")
elif tab_index == 6:
    st.subheader("💬 Góc chia sẻ")
    st.write("Nơi bạn chia sẻ kinh nghiệm, mẹo hay về tin học.")

