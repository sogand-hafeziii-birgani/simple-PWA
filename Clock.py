from tkinter import *
import time

# ایجاد پنجره اصلی
window = Tk()
window.title('Digital Clock')
window.geometry('600x400')

# تابع برای به‌روزرسانی زمان
def mytime():
    hour = time.strftime('%I')
    minute = time.strftime('%M')
    second = time.strftime('%S')
    am_pm = time.strftime("%p")  # باید از %p برای AM/PM استفاده شود
    day = time.strftime("%A")
    zone = time.strftime("%Z")
    myText = hour + ":" + minute + ":" + second + " " + am_pm
    mytext2 = day + " ," + zone
    mylabel.config(text=myText)  # اصلاح confing به config
    mylabel2.config(text=mytext2)
    mylabel.after(1000, mytime)

# ایجاد ویجت‌ها
mylabel = Label(window, text="", font=("Arial", 72), fg='white', bg='green')  # اضافه کردن ویرگول بین آرگومان‌ها
mylabel.pack()

mylabel2 = Label(window, text="", font=("Arial", 24))
mylabel2.pack()

# اجرای تابع برای نمایش زمان
mytime()

# اجرای حلقه اصلی
window.mainloop()