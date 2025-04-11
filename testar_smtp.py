import threading
import customtkinter as ctk
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText

# Configuração do tema
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

def testar_smtp():
    servidor = entry_servidor.get()
    porta = entry_porta.get()
    email = entry_email.get()
    senha = entry_senha.get()
    destino = entry_destino.get()
    usar_ssl = checkbox_ssl.get()  # True ou False
    
    try:
        msg = MIMEText("Este é um e-mail de teste via SMTP.")
        msg['Subject'] = 'Teste de SMTP'
        msg['From'] = email
        msg['To'] = destino

        if usar_ssl:
            smtp = smtplib.SMTP_SSL(servidor, int(porta))
        else:
            smtp = smtplib.SMTP(servidor, int(porta))
            smtp.ehlo()
            smtp.starttls()
        
        smtp.login(email, senha)
        smtp.send_message(msg)
        smtp.quit()

        messagebox.showinfo("Sucesso", "✅ E-mail enviado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"❌ Falha ao enviar e-mail:\n{e}")

# Janela principal
app = ctk.CTk()
app.geometry("500x500")
app.title("Testador de SMTP")

ctk.CTkLabel(app, text="Servidor SMTP").pack(pady=5)
entry_servidor = ctk.CTkEntry(app, width=400)
entry_servidor.pack()

ctk.CTkLabel(app, text="Porta").pack(pady=5)
entry_porta = ctk.CTkEntry(app, width=400)
entry_porta.pack()

ctk.CTkLabel(app, text="E-mail de envio").pack(pady=5)
entry_email = ctk.CTkEntry(app, width=400)
entry_email.pack()

ctk.CTkLabel(app, text="Senha").pack(pady=5)
entry_senha = ctk.CTkEntry(app, show="*", width=400)
entry_senha.pack()

ctk.CTkLabel(app, text="E-mail de destino").pack(pady=5)
entry_destino = ctk.CTkEntry(app, width=400)
entry_destino.pack()

checkbox_ssl = ctk.CTkCheckBox(app, text="Usar SSL (em vez de TLS)")
checkbox_ssl.pack(pady=10)

def iniciar_teste():
    thread = threading.Thread(target=testar_smtp)
    thread.start()

ctk.CTkButton(app, text="Testar Envio", command=iniciar_teste).pack(pady=20)

rodape = ctk.CTkLabel(app, text="Desenvolvido por Letancio Álvaro Marinho Junior", font=("Arial", 10))
rodape.pack(side="bottom", pady=10)

app.mainloop()
