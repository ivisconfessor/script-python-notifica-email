import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_notificacao_email(email_remetente, senha_remetente, email_destinatario, assunto_email, caminho_arquivo_html_template_email):
    msg = MIMEMultipart()
    msg['From'] = email_remetente
    msg['To'] = email_destinatario
    msg['Subject'] = assunto_email

    with open(caminho_arquivo_html_template_email, 'r', encoding='utf-8') as arquivo:
        conteudo_html_template_email = arquivo.read()

    msg.attach(MIMEText(conteudo_html_template_email, 'html'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        server.login(email_remetente, senha_remetente)

        textoEmail = msg.as_string();
        server.sendmail(email_remetente, email_destinatario, textoEmail)

        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro na tentativa de envio da notificação por e-mail: {e}")
    finally:
        server.quit();

# Exemplo Teste de Uso
email_remetente = '[SEU E-MAIL]'
senha_remetente = '[SENHA DO SEU E-MAIL]'
email_destinatario = '[E-MAIL DO DESTINATÁRIO]'
assunto_email = 'Envio de E-mail usando Python com Template HTML'
caminho_arquivo_html_template_email = 'TemplateEmail.html'

enviar_notificacao_email(email_remetente, senha_remetente, email_destinatario, assunto_email, caminho_arquivo_html_template_email)
