import tkinter as tk
from deep_translator import GoogleTranslator

def translate_text():
    text = input_text.get("1.0", tk.END).strip()
    dest = dest_lang.get()
    result = GoogleTranslator(source='auto', target=dest).translate(text)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)

window = tk.Tk()
window.title("Language Translator")
window.geometry("600x500")
window.configure(bg="#1e1e2e")

tk.Label(window, text="🌐 Language Translator", font=("Arial", 20, "bold"),bg="#1e1e2e", fg="#cba6f7").pack(pady=15)

tk.Label(window, text="Enter Text:", font=("Arial", 11),bg="#1e1e2e", fg="#cdd6f4").pack()
input_text = tk.Text(window, height=5, width=60, font=("Arial", 11), bg="#313244", fg="#cdd6f4", insertbackground="white")
input_text.pack(pady=5)

tk.Label(window, text="Target Language (e.g. fr, es, hi, te, ja):",font=("Arial", 11), bg="#1e1e2e", fg="#cdd6f4").pack()
dest_lang = tk.Entry(window, font=("Arial", 11), width=20,bg="#313244", fg="#cdd6f4", insertbackground="white")
dest_lang.pack(pady=5)

tk.Button(window, text="Translate 🚀", command=translate_text,font=("Arial", 12, "bold"), bg="#cba6f7", fg="#1e1e2e", padx=20, pady=5, relief="flat").pack(pady=10)

tk.Label(window, text="Translated Text:", font=("Arial", 11),bg="#1e1e2e", fg="#cdd6f4").pack()
output_text = tk.Text(window, height=5, width=60, font=("Arial", 11),bg="#313244", fg="#a6e3a1", insertbackground="white")
output_text.pack(pady=5)

window.mainloop()