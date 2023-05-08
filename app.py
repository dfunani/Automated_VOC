"""Program to automate the Vetting, Onboarding and Compliance
    app.py - main entry
    services package - provides packages utilized by the main program
    email package - exposes the email_listener library/package """
    
from services.email.email_listener import EmailService
from services.args.args_parser import ArgsParse
from services.strapi.service import strapi
import re
import json

class Application:
    """Abstraction of the main application
    """
    Emails: list[dict] = list([])
    
    def __init__(self,  email: str = None, password: str = None, folder: str = None, attachment_dest: str = None, read_dest: str = None, timeout: int = 60) -> None:
        """Constructor
        """
        self.email = email
        self.password = password
        self.folder = folder
        self.attachment_dest = attachment_dest 
        self.read_dest = read_dest
        self.timeout = timeout
    
    def MainLoop(self):
        """Email Services Infinite loop to timeout on
        """
        emailService = EmailService(self.email, self.password, self.folder, self.attachment_dest, self.read_dest, self.timeout)
        emailService.login()
        mail = emailService.read()
        # Mail service returns an email
        if mail:
            for sender in mail:
                # Only if Subject matches standard structure
                subject = re.match(r".*(Ayoba Developer Portal).*", mail[sender].get('Subject'), re.IGNORECASE)
                if subject:
                    # Iterate through the body to regex multilines
                    for line in mail[sender].get('Plain_Text').split('\n'):
                        micro_app_id = re.match(r".* MicroApp Id: ([\d]+) .*", line, re.IGNORECASE)
                        if micro_app_id and micro_app_id.groups() and micro_app_id.groups()[0].isnumeric():
                            print(json.dumps(strapi(int(micro_app_id.groups()[0]))))
        
        
        
if __name__ == "__main__":
    argsParse = ArgsParse()
    app = Application(**argsParse.parse())
    while True:
        try:
            app.MainLoop()
        except KeyboardInterrupt:
            print(Application.Emails)