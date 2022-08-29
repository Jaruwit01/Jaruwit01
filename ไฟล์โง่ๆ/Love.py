import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
def a():
    
    # s = ["ไง.....เด็กน้อยย","วันนี้ฉันมีอะไรจะบอกเธอด้วย...","อยากรู้ไหมว่าจะบอกอะไร","มันอาจจะไม่หวาน หรือ อาจจะเสี่่ยว หรือ เข้าใจยาก","แต่ว่าเป็นข้อความที่ฉันบอกแค่เธอคนเดียวนะ"
    #      ,"อยากรู้แล้วยังงง", "ฮั่นแหนะ.....คิดว่าจะได้รู้แล้วอะดิ",  "หน้าถัดไปบอกจริงๆละ","รู้ไหม......ว่าตั้งแต่ที่ได้รู้จักเธออะ",
    #      "โลกของฉันก็สดใสขึ้นเรื่อยๆเลยนะ", "ขอบคุณนะ.....ที่เข้ามาเป็นความสุขให้กับฉัน", "แหนะ.....คิดว่าหมดแล้วอะดิ",
    #       "อ่ะๆ.....สุดท้ายจริงๆละ", "You are an ordinary person who looks special to me. นะ :)"]\
    # s = ["ไง.....เด็กน้อยย","วันนี้ฉันมีอะไรจะบอกเธอด้วย...","อยากรู้ไหมว่าจะบอกอะไร","มันอาจจะไม่หวาน หรือ อาจจะเสี่่ยว หรือ เข้าใจยาก","แต่ว่าเป็นข้อความที่ฉันบอกแค่เธอคนเดียวนะ"
    #      ,"อยากรู้แล้วยังงง", "ฮั่นแหนะ.....คิดว่าจะได้รู้แล้วอะดิ",  "หน้าถัดไปบอกจริงๆละ","ฮั่นนะ........ยังๆ","ใกล้ละๆ......ห้าถัดไปนี้แหละ",
    #      "เดี๋ยววๆๆๆ.......รู้ว่าอยากดูแล้ว",  "อุ้ยยย........เขินน", "มาา..ถ้าพร้อมแล้ววก็...." ,  "เอ้า!!!...ผิดไฟล์..แฮร่!!"]
    # for i in s:
    #     messagebox.showinfo("LOVE 3000", i)
    
    t = np.arange(0,2*np.pi, 0.1)
    x = 16*np.sin(t)**3
    y = 13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)
    plt.grid(False)
    plt.axis('off')
    plt.plot(x,y,'r-')
    messagebox.showinfo("", "นีๆๆ......")
    messagebox.showinfo("", "เรามีอะไรจะให้เธอด้วย.....")
    
    plt.mainloop()
    
window = tk.Tk()
window.option_add('*font', 'consolas 10')
window.title("ฮั่นแหน่!!")
window.geometry('200x100')
f = tk.Frame(window, bd=10, height=1000, width=1000, cursor="heart")
f.pack(expand=True)
label = tk.Label(f, text= "Gift to You").pack(expand=True)
botton1 = tk.Button(f,text = 'ลองกดดูดิ....', command=a).pack(expand=True) 
window.mainloop()
