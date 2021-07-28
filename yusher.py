import tkinter as tk
import webbrowser

# Some website links for search button
def todo(TODO):
    try:
        if TODO == 'google':
            webbrowser.open("https://www.google.com")
        elif 'chrome' in TODO:
            webbrowser.open('https://www.google.com/chrome')
        elif 'firefox' in TODO:
            webbrowser.open("https://www.firefox.com")
        elif 'youtube' in TODO:
            webbrowser.open("https://www.youtube.com")
        elif 'github' in TODO:
            webbrowser.open('https://github.com')
        elif 'stackoverflow' in TODO:
            webbrowser.open('https://stackoverflow.com')
        elif 'facebook' in TODO:
            webbrowser.open('https://www.facebook.com')
        elif 'instagram' in TODO:
            webbrowser.open('https://www.instagram.com')
        elif 'linkedin' in TODO:
            webbrowser.open('https://www.linkedin.com')
        elif 'whatsapp' in TODO:
            webbrowser.open('https://www.whatsapp.com')
        else:
            pass
    except:
        pass

root = tk.Tk()
root.geometry("1500x1000")
root.title("yusher.com")

frame = tk.Frame(root, bg="#FFFEF7", bd=5)
frame.place(relwidth=2, relheight=2)

textfield = tk.Label(text="Y",fg="#7b5cc7", bg="#FFFEF7",font=("PT Serif", 145))
textfield.place(relx=0.319, rely=0.17)

textfield = tk.Label(text="USHER", fg="#9a82d4", bg="#FFFEF7",font=("PT Serif", 145))
textfield.place(relx=0.389, rely=0.17)

entry = tk.Entry(frame, font=("Gill Sans", 20))
entry.place(relx=0.17, rely=0.24, relheight=0.025, relwidth=0.2)
entry.focus()

search = tk.Button(frame,text='Search', font=("Gill Sans", 26), command=lambda: todo(entry.get()))
search.place(relx=0.13, rely=0.24, relwidth=0.04, relheight=0.025)

# Little decoration:)
d1 = tk.Label(frame, text='☁︎', fg="#7b5cc7", bg="#FFFEF7")
d1.place(relx=0.05, rely=0.07)
d2 = tk.Label(frame, text='☁︎', fg="#7b5cc7", bg="#FFFEF7")
d2.place(relx=0.063, rely=0.37)
d3 = tk.Label(frame, text='☁︎', fg="#7b5cc7", bg="#FFFEF7")
d3.place(relx=0.305, rely=0.21)
d4 = tk.Label(frame, text='☁︎', fg="#7b5cc7", bg="#FFFEF7")
d4.place(relx=0.39, rely=0.39)
d5 = tk.Label(frame, text='☁︎', fg="#b1abf1", bg="#FFFEF7")
d5.place(relx=0.2, rely=0.05)
d6 = tk.Label(frame, text='☁︎', fg="#b1abf1", bg="#FFFEF7")
d6.place(relx=0.106, rely=0.18)
d7 = tk.Label(frame, text='☁︎', fg="#b1abf1", bg="#FFFEF7")
d7.place(relx=0.4, rely=0.073)
d8 = tk.Label(frame, text='☁︎', fg="#b1abf1", bg="#FFFEF7")
d8.place(relx=0.2, rely=0.44)
d9 = tk.Label(frame, text='☁︎', fg="#b1abf1", bg="#FFFEF7")
d9.place(relx=0.44, rely=0.235)
d10 = tk.Label(frame, text='☁︎', fg="#b1abf1", bg="#FFFEF7")
d10.place(relx=0.18, rely=0.3)

# Here are some web browser buttons
google_btn = tk.Button(frame,text ="G",fg="green", font=("Gill Sans", 34))
google_btn.place(relx=0.165 , rely=0.35, relwidth=0.03, relheight=0.035)
go = tk.Label(text="Google", font=("Gill Sans", 20),bg="#FFFEF7")
go.place(relx=0.34, rely=0.77)

github_btn = tk.Button(frame, text="G", fg="purple", font=("Gill Sans", 34))
github_btn.place(relx=0.215, rely=0.35, relwidth=0.03, relheight=0.035)
gh = tk.Label(text="Github", font=("Gill Sans", 20), bg="#FFFEF7")
gh.place(relx=0.44, rely=0.77)

youtube_btn = tk.Button(frame, text="Y", fg="red", font=("Gill Sans", 34))
youtube_btn.place(relx=0.265 , rely=0.35, relwidth=0.03, relheight=0.035)
yt = tk.Label(text="Youtube", font=("Gill Sans", 20), bg="#FFFEF7")
yt.place(relx=0.535, rely=0.77)

stackoverflow_btn = tk.Button(frame, text="S", fg="orange", font=("Gill Sans", 34))
stackoverflow_btn.place(relx=0.315 , rely=0.35, relwidth=0.03, relheight=0.035)
so = tk.Label(text="Stackoverflow", font=("Gill Sans", 20), bg="#FFFEF7")
so.place(relx=0.620, rely=0.77)

root.mainloop()
