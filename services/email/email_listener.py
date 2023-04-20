"""Package manages the email services
email_listener - uses the email_listener PYPI package
EmailService - class abstracting the email services """
from email_listener import EmailListener
from decouple import config

class EmailService:
    """Service class managing all functionalities relating to the email service
    """
    def __init__(self, email: str = None, password: str = None, folder: str = None, attachment_dest: str = None, read_dest: str = None, timeout: int = None) -> None:
        """constructor
        """
        self.__email: str = email if email else config("Email") 
        self.__password: str = password if password else config("Password")
        self.__folder: str = folder if folder else config("Folder")
        self.__attachment_dest: str = attachment_dest if attachment_dest else config("Attachment_dest")
        self.__read_dest: str = read_dest if read_dest else config("Read_dest")
        self.__timeout: str = timeout if timeout else int(config("Timeout"))
        self.__listener: str = self.__emailListener()
        
    def __emailListener(self) -> EmailListener:
        """Creates an EmailListener Object

        Returns:
            EmailListener: EmailListener Object Created
        """
        return EmailListener(self.__email, self.__password, self.__folder, self.__attachment_dest)
    
    def login(self):
        """logs into the EmailService - IMAP
        """
        self.__listener.login()
    
    def read(self) -> dict:
        """Read the mailbox for unread messages and move to the read destination folder

        Returns:
            dict: A Dict of the mail retrieved and read
        """
        return self.__listener.scrape(move=self.__read_dest, unread=True)

    
    def listen(self):
        """Listens for incoming mails on the IMAP server 
        """
        self.__listener.listen(self.__timeout)
        

if __name__ == "__main__":
    None