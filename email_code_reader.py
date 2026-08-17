 
import imaplib
import email
import re
from email.header import decode_header
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()


class EmailCodeReader:
    def __init__(self, email_address, password, imap_server="imap.gmail.com", imap_port=993):
        self.email_address = email_address
        self.password = password
        self.imap_server = imap_server
        self.imap_port = imap_port

    def get_code(self, to_email, minutes=30, code_length=6):
        try:
            mail = imaplib.IMAP4_SSL(self.imap_server, self.imap_port)
            mail.login(self.email_address, self.password)
            mail.select('INBOX')

            date_limit = (datetime.now() - timedelta(minutes=minutes)).strftime("%d-%b-%Y")
            status, messages = mail.search(None, f'(TO "{to_email}" SINCE "{date_limit}")')

            if status != 'OK' or not messages[0]:
                mail.close()
                mail.logout()
                return None

            message_ids = messages[0].split()
            latest_id = message_ids[-1]
            status, msg_data = mail.fetch(latest_id, '(RFC822)')

            if status != 'OK':
                mail.close()
                mail.logout()
                return None

            msg = email.message_from_bytes(msg_data[0][1])

            subject = decode_header(msg.get('Subject', ''))[0][0]
            if isinstance(subject, bytes):
                subject = subject.decode('utf-8', errors='ignore')

            code_match = re.search(rf'\b(\d{{{code_length}}})\b', subject)
            if code_match:
                code = code_match.group(1)
                mail.close()
                mail.logout()
                return code

            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.get_payload(decode=True).decode('utf-8', errors='ignore')
                        break
            else:
                body = msg.get_payload(decode=True).decode('utf-8', errors='ignore')

            code_match = re.search(rf'\b(\d{{{code_length}}})\b', body)
            if code_match:
                code = code_match.group(1)
                mail.close()
                mail.logout()
                return code

            mail.close()
            mail.logout()
            return None

        except Exception as e:
            print(f"Error: {e}")
            return None


if __name__ == "__main__":
    reader = EmailCodeReader(
        email_address=os.getenv("EMAIL_USER"),
        password=os.getenv("EMAIL_PASSWORD"),
        imap_server=os.getenv("EMAIL_IMAP_SERVER", "imap.gmail.com")
    )

    code = reader.get_code(
        to_email=os.getenv("TARGET_EMAIL"),
        minutes=30,
        code_length=6
    )

    if code:
        print(f"Code: {code}")
    else:
        print("Code not found")