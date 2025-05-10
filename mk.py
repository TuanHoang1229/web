import streamlit as st
import random
import string
import hashlib
# --- Logo & Tiêu đề (bo tròn + gọn đẹp) ---
logo_url = "https://raw.githubusercontent.com/TuanHoang1229/web2/refs/heads/main/IMG_2935.JPG"
st.markdown("""
    <div style="
        display: flex; align-items: center; justify-content: space-between;
        padding: 10px 20px; background-color: #ffffff;
        border-radius: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
        <div style="display: flex; align-items: center;">
            <img src="{logo_url}" alt="Logo" width="50" height="50" style="border-radius: 50%; margin-right: 15px;">
            <h2 style="margin: 0; color: #40E0D0;">Tin Học Online</h2>
        </div>
    </div>
    <hr style="margin-top: 10px;">
""", unsafe_allow_html=True)

# --- Menu 3 gạch (sidebar) ---
with st.sidebar:
    st.image(logo_url, width=100)
    st.title("☰ Menu")
    choice = st.radio("Chọn chuyên mục:", [
        "🏠 Trang chủ",
        "🔑 Kiểm tra mật khẩu",
        "🌐 Thiết kế Web cơ bản", 
        "🔐 An toàn thông tin",
        "📂 Kho tài liệu",
        "🧠 Trắc nghiệm",
        "💬 Góc chia sẻ"
    ])

if choice == "🏠 Trang chủ":
    st.title("📘 Chào mừng bạn đến với Góc Tự Học Tin học")
    st.markdown("""
    (nội dung như bạn đã viết ở `tabs[0]`)
    """)

elif choice == "🔑 Kiểm tra mật khẩu":
    st.header("🔐 Kiểm tra & Tạo mật khẩu mạnh")
    # (phần kiểm tra mật khẩu như cũ)

elif choice == "🌐 Thiết kế Web cơ bản":
    st.header("🖥️ Thiết kế Web cơ bản với HTML & CSS")
    # (phần thiết kế web như tabs[2])

# ... tiếp tục cho các chuyên mục khác


# Tính độ mạnh mật khẩu
def calculate_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if any(c.islower() for c in password):
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in string.punctuation for c in password):
        strength += 1
    return strength

# UI
st.set_page_config(page_title="Tạo mật khẩu mạnh", page_icon="🔒")
st.title("🔐 Trình tạo mật khẩu mạnh")

length = st.number_input("Độ dài mật khẩu", min_value=6, max_value=100, value=12)

if st.button("Tạo mật khẩu"):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    st.text_input("Mật khẩu của bạn", password)
    
    strength = calculate_strength(password)
    strength_labels = ["Rất yếu", "Yếu", "Trung bình", "Mạnh", "Rất mạnh"]
    st.progress(strength * 20)
    st.success(f"Độ mạnh: {strength_labels[strength - 1] if strength else 'Rất yếu'}")

    if st.button("Lưu mật khẩu (SHA-256)"):
        hashed = hashlib.sha256(password.encode()).hexdigest()
        with open("saved_passwords.txt", "a") as f:
            f.write(hashed + "\n")
        st.success("Đã lưu mật khẩu (dạng SHA-256) vào file.")


def calculate_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if any(c.islower() for c in password):
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in string.punctuation for c in password):
        strength += 1
    return strength

def password_strength_text(score):
    if score <= 2:
        return "❌ Yếu", "red"
    elif score == 3 or score == 4:
        return "⚠️ Trung bình", "orange"
    else:
        return "✅ Mạnh", "green"

st.title("🔐 Kiểm tra độ mạnh của mật khẩu")

password = st.text_input("Nhập mật khẩu:", type="password")

if password:
    score = calculate_strength(password)
    strength_text, color = password_strength_text(score)
    
    st.markdown(f"**Đánh giá:** <span style='color:{color}'>{strength_text}</span>", unsafe_allow_html=True)
    st.progress(score * 20)
