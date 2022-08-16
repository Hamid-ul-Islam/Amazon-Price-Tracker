from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from matplotlib.pyplot import title
import requests
import lxml
from bs4 import BeautifulSoup


class price_tracker:
    price = 0
    def product_price(self):
        url = "https://www.amazon.com/Apple-MacBook-Pro-Late-2021/dp/B0B62587S6/ref=sr_1_13?crid=339UUR0KTJIYH&keywords=macbook&qid=1657441932&sprefix=ma%2Caps%2C337&sr=8-13"
        self.url = url
        header = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
        }
        response = requests.get(url, headers=header)
        soup = BeautifulSoup(response.content, "lxml")
        title = soup.find('span', id='productTitle').text
        self.title = title
        try:
          price_text = soup.find('span', class_='a-offscreen').text
          without_currency = price_text.split('$')[1]
          replace_comma = without_currency.replace(',', '')
          price = float(replace_comma)
          self.price = price
        except:
          self.price = 0


    def daily_mail(self):
        sender_email = "Hamidchowdhury.anonymous@gmail.com"
        receiver_email = "hamidthedev@gmail.com"
        password = "clkpapvrhtckwfwm"

        message = MIMEMultipart("alternative")
        message["Subject"] = "Price Update"
        message["From"] = "Price Assistant <hamidthedev@gmail.com>"
        message["To"] = receiver_email

        # Create the plain-text and HTML version of your message
        html = """
        <html>
<body>
  <h1>Assalamu Alaikum Warahmatullah</h1>
  <h4>Hello Sir,<br>
    Your Product: "{name}"  from Amazon,<br>
    price is Now: ${tk}<br>
    Yo Can buy the product from this link now: <a href="{link}"><h3>Buy Now!</h3></a>
  </h4>
</body>
</html>
        """

        form = html.format(tk=self.price, name=self.title, link=self.url)
        # Turn these into html MIMEText objects
        msg = MIMEText(form, "html")

        # The email client will try to render the last part first
        message.attach(msg)

        # Create secure connection with server and send email
        connection = SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(sender_email, receiver_email, message.as_string())

    def dropped_mail(self):
        sender_email = "Hamidchowdhury.anonymous@gmail.com"
        receiver_email = "hamidthedev@gmail.com"
        password = "clkpapvrhtckwfwm"

        message = MIMEMultipart("alternative")
        message["Subject"] = "Price Dropped!!"
        message["From"] = "Price Assistant <hamidthedev@gmail.com>"
        message["To"] = receiver_email

        # Create the plain-text and HTML version of your message
        html = """
        <html>
<body>
  <h1>Assalamu Alaikum Warahmatullah</h1>
  <h4>Hello Sir,<br>
    Your Product: "{name}"  from Amazon,<br>
    price is Now Dropped to: ${tk}<br>
    Yo Can buy the product from this link now: <a href="{link}"><h3>Buy Now!</h3></a>
  </h4>
</body>
</html>
        """

        form = html.format(tk=self.price, name=self.title, link=self.url)
        # Turn these into html MIMEText objects
        msg = MIMEText(form, "html")

        # The email client will try to render the last part first
        message.attach(msg)

        # Create secure connection with server and send email
        connection = SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(sender_email, receiver_email, message.as_string())

obj = price_tracker()
obj.product_price()
price = obj.price
if price == 0:
  print("Price unavailable")
elif price == 2899:
    obj.daily_mail()
elif price<2899:
    obj.dropped_mail()
else:
    print("price is High")
