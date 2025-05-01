import tkinter as tk

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Ứng dụng Tkinter")
window.geometry("400x300")

# Thêm nhãn
label = tk.Label(window, text="Chào mừng bạn đến với ứng dụng Tkinter!", font=("Arial", 14))
label.pack(pady=20)

# Thêm nút bấm
button = tk.Button(window, text="Nhấn vào đây", font=("Arial", 12), command=lambda: print("Nút đã được nhấn"))
button.pack(pady=10)

# Chạy vòng lặp chính
window.mainloop()
