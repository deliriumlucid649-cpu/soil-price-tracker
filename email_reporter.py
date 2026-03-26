import smtplib  
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  
import datetime  

class EmailReporter:  
    def __init__(self, smtp_server, smtp_port, username, password):  
        self.smtp_server = smtp_server  
        self.smtp_port = smtp_port  
        self.username = username  
        self.password = password  

    def generate_html_report(self, price_data):  
        # Generate an HTML report comparing prices across retailers and soil types  
        html = '<html><body>'  
        html += '<h1>Soil Price Report</h1>'  
        html += '<table border="1"><tr><th>Retailer</th><th>Soil Type</th><th>Current Price</th><th>Historical Trend</th></tr>'  

        for data in price_data:  
            trend = "Increasing" if data['trend'] else "Decreasing"  
            html += f'<tr><td>{data['retailer']}</td><td>{data['soil_type']}</td><td>{data['current_price']}</td><td>{trend}</td></tr>'  

        html += '</table>'  
        html += f'<p>Report generated on {datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")}</p>'  
        html += '</body></html>'  
        return html  

    def send_email(self, to_email, subject, html_body):  
        # Send the email report  
        message = MIMEMultipart()  
        message['From'] = self.username  
        message['To'] = to_email  
        message['Subject'] = subject  

        message.attach(MIMEText(html_body, 'html'))  

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:  
            server.starttls()  
            server.login(self.username, self.password)  
            server.send_message(message)  

# Example usage  
# price_data = [  
#     {'retailer': 'Retailer A', 'soil_type': 'Loam', 'current_price': '$10', 'trend': True},  
#     {'retailer': 'Retailer B', 'soil_type': 'Clay', 'current_price': '$12', 'trend': False},  
# ]  
# reporter = EmailReporter('smtp.yourserver.com', 587, 'your_email@example.com', 'yourpassword')  
# html_report = reporter.generate_html_report(price_data)  
# reporter.send_email('recipient@example.com', 'Soil Price Report', html_report)  
