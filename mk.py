import tkinter as tk
from tkinter import messagebox, ttk
import random
import string
import hashlib
# Hàm tạo mật khẩu mạnh
def generate_password():
    try:
        length = int(entry_length.get())
        if length < 6:
            messagebox.showwarning("Cảnh báo", "Độ dài tối thiểu là 6 ký tự.")
            return
    except ValueError:
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập số hợp lệ cho độ dài.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)
    update_strength_bar(password)

# Hàm kiểm tra độ mạnh của mật khẩu
def check_password_strength():
    password = entry_password.get()
    strength = calculate_strength(password)

    if strength <= 2:
        result = "Yếu"
    elif strength == 3 or strength == 4:
        result = "Trung bình"
    else:
        result = "Mạnh"

    messagebox.showinfo("Kết quả", f"Độ an toàn mật khẩu: {result}")

# Tính toán điểm mạnh mật khẩu
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

# Cập nhật thanh strength bar
def update_strength_bar(password):
    strength = calculate_strength(password)
    progress_strength['value'] = strength * 20

# Lưu mật khẩu (dạng băm SHA-256) vào file
def save_password():
    password = entry_password.get()
    if not password:
        messagebox.showwarning("Cảnh báo", "Không có mật khẩu để lưu.")
        return

    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    with open("saved_passwords.txt", "a") as f:
        f.write(hashed_password + "\n")

    messagebox.showinfo("Lưu thành công", "Mật khẩu đã được lưu (dạng băm SHA-256).")

# Giao diện Tkinter
window = tk.Tk()
window.title("Trình tạo & kiểm tra mật khẩu nâng cao")
window.geometry("400x300")

frame = tk.Frame(window)
frame.pack(pady=10)

label_length = tk.Label(frame, text="Độ dài mật khẩu:")
label_length.grid(row=0, column=0, padx=5)

entry_length = tk.Entry(frame, width=5)
entry_length.insert(0, "12")
entry_length.grid(row=0, column=1, padx=5)

label_password = tk.Label(window, text="Mật khẩu:")
label_password.pack(pady=5)

entry_password = tk.Entry(window, width=40)
entry_password.pack()

progress_strength = ttk.Progressbar(window, length=300, maximum=100)
progress_strength.pack(pady=5)

btn_generate = tk.Button(window, text="Tạo mật khẩu mạnh", command=generate_password)
btn_generate.pack(pady=5)

btn_check = tk.Button(window, text="Kiểm tra độ an toàn", command=check_password_strength)
btn_check.pack(pady=5)

btn_save = tk.Button(window, text="Lưu mật khẩu (Lưu MK)", command=save_password)
btn_save.pack(pady=5)

window.mainloop()
