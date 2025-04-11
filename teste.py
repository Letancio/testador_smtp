import smtplib
from email.mime.text import MIMEText  # <- Import correto aqui!

def testar_smtp_zoho_tls():
    servidor = "smtp.zoho.com"
    porta = 587
    email_origem = "compras@imcompras.org"
    senha = "impublicacoes*2022"
    email_destino = "letanciomarinho@gmail.com"

    try:
        msg = MIMEText("Este é um e-mail de teste via TLS.")
        msg["Subject"] = "Teste Zoho SMTP com TLS"
        msg["From"] = email_origem
        msg["To"] = email_destino

        smtp = smtplib.SMTP(servidor, porta)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(email_origem, senha)
        smtp.send_message(msg)
        smtp.quit()

        print("✅ Email enviado com sucesso via TLS!")
    except Exception as e:
        print(f"❌ Falha ao enviar: {e}")

if __name__ == "__main__":
    testar_smtp_zoho_tls()
