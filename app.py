from flask import Flask, request
import smtplib
from email.mime.text import MIMEText # Προσθήκη για ελληνικά
from email.header import Header      # Προσθήκη για ελληνικά

app = Flask(__name__)

@app.route('/send_protocol', methods=['POST'])
def send_email():
    name = request.form.get('name')
    user_email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')

    # Σύνθεση του κειμένου
    email_body = f"Client Name: {name}\n" \
                 f"Client Email: {user_email}\n" \
                 f"Phone Number: {phone}\n\n" \
                 f"Project Details:\n{message}"

    # Ρύθμιση του email για υποστήριξη Ελληνικών (UTF-8)
    msg = MIMEText(email_body, 'plain', 'utf-8')
    msg['Subject'] = Header("RELIΛS - NEW PROJECT INQUIRY", 'utf-8')
    msg['From'] = "nektarios.relias@gmail.com"
    msg['To'] = "nektarios.relias@gmail.com"

    MY_EMAIL = "nektarios.relias@gmail.com"
    MY_PASSWORD ="siip cgfv sjav tshc" 

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(MY_EMAIL, MY_PASSWORD)
            server.sendmail(MY_EMAIL, MY_EMAIL, msg.as_string()) # Αποστολή ως string
        
        return f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>RELIAS</title>
            
            <style>
                body {{ background-color: #05001b; color: #00d4ff; font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }}
                .success {{ border: 2px solid #00d4ff; padding: 40px; text-align: center; box-shadow: 0 0 20px #00d4ff; }}
                button {{ margin-top: 20px; padding: 10px 20px; border: 1px solid #00d4ff; background: none; color: #00d4ff; cursor: pointer; }}
            </style>
        </head>
        <body>
            <div class="success">
                <h1>Your message has been sent</h1>
                <p>Thank you, {name}.</p>
                <button onclick="window.close()">CLOSE TAB</button>
            </div>

            @media (max-width: 768px) {
                .success{
                    height: 90vh;
                }
            }
        </body>
        </html>
        '''
    except Exception as e:
        return f"<h1 style='color:red;'>Error: {e}</h1>"

if __name__ == "__main__":
    app.run(debug=True, port=5000)