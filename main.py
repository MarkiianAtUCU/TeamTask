import smtplib

from email.mime.text import MIMEText


class Client:
    id_counter = 0

    def __init__(self, name, age, sex, email, other_information):
        """
        Initialize Client object with such parameters:
        :param name: string
        :param age: int
        :param sex: string
        :param email: string
        :param other_information: string
        """
        Client.id_counter += 1
        self.id = Client.id_counter
        self.name = name
        if 0 < age < 110:
            self.age = age
        else:
            raise AttributeError
        if sex == "male" or sex == "female":
            self.sex = sex
        else:
            raise AttributeError
        self.email = email
        self.other_information = other_information

    def __str__(self):
        """
        Returns Client object information in easy to read format
        """
        return "Name: {}\nAge: {}\nSex: {}\nE-mail: {}\nOther: {}".format(
            self.name, self.age, self.sex, self.email,
            self.other_information)

    def less_info(self):
        return "{}".format(self.name)


class MailInfo:
    def __init__(self, client, mail_code, message):
        """
        Initialize MailInfo object with such parameters
        :param client: Client
        :param mail_code: string
        :param message: string
        """
        self.client = client
        self.mail_code = mail_code
        self.message = message

    def __str__(self):
        """
        Returns MailInfo object name
        """
        return self.client.name


class MailBox:
    def __init__(self):
        """
        Initialize MailBox object with informartion list
        """
        self.inf = []

    def add_mail_info(self, mail):
        """
        Function adds mail to MailBox object information
        :param mail: string
        """
        self.inf.append(mail)

    def send_all(self, login_yours, password_yours):
        """
        This function sends all the mails
        """
        for i in self.inf:
            MailSender(i, login_yours, password_yours).send_mail()


class MailSender:
    mail_code_type = {"1": "Birthday", "2": "Work_mail", "3": "Sail"}

    def __init__(self, mail_info, login_yours, password_yours):
        """
        Initialize MailSender object with such parameters:
        :param mail_info: string
        :param login_yours: string
        :param password_yours: string
        """
        self.mail_info = mail_info
        self.login_yours = login_yours
        self.password_yours = password_yours

    def send_mail(self):
        """
        Sends mail to users
        """
        to = self.mail_info.client.email
        msg = MIMEText(self.mail_info.message)
        try:
            msg['Subject'] = MailSender.mail_code_type[self.mail_info.mail_code]
        except KeyError:
            msg['Subject'] = "Default"
        msg['From'] = self.login_yours
        msg['To'] = to
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.ehlo()
        server.login(self.login_yours, self.password_yours)
        server.sendmail(self.login_yours, to, msg.as_string())
        server.quit()
