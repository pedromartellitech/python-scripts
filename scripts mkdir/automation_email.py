import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body, to_email):
    """Enviar um e-mail simples usando smtplib."""
    from_email = "youremail@example.com"
    password = "yourpassword"
    
    # Configurar o servidor SMTP
    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login(from_email, password)
    
    # Configurar o e-mail
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    # Enviar o e-mail
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

# Exemplo de uso
if __name__ == "__main__":
    send_email("Assunto do E-mail", "Corpo do e-mail", "destinatario@example.com")

