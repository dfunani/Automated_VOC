"""args_parser module
Abstracts and encapsulates the management/parsing of program arguments (sys.args)

ArgsParse - Encapsulates the internal workings of ArgsParse
parse(self) - Returns the args as key/value pair
"""

import argparse


class ArgsParse:
    """Abstraction of the arg management
    """
    def __init__(self) -> None:
        """Constructor
        """
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-e", "--email", type=str, help="Email Address for the Email to be Scraped")
        self.parser.add_argument("-p", "--password", type=str, help="Password to the Email to be Scraped")
        self.parser.add_argument("-f", "--folder", type=str, help="Email Folder to be Scraped")
        self.parser.add_argument("-ad", "--attachment_dest", type=str, help="Destination Folder of the Email Attachments")
        self.parser.add_argument("-rd", "--read_dest", type=str, help="Destination Folder of the Email(s) Read")
        self.parser.add_argument("-t", "--timeout", type=int, help="Number of minutes to Timeout in")
        
    def parse(self, ) -> dict:
        """parses the system arguments

        Returns:
            dict: representation of the email read
        """
        argsDict: dict = {}
        args: list = self.parser.parse_args()

        if args.email:
            argsDict["email"] = args.email    
        if args.password:
            argsDict["password"] = args.password
        
        if args.folder:
            argsDict["folder"] = args.folder
        
        if args.attachment_dest:
            argsDict["attachment_dest"] = args.attachment_dest
        if args.read_dest:
            argsDict["read_dest"] = args.read_dest

        if args.timeout:
            argsDict["timeout"] = args.timeout
        
        return argsDict