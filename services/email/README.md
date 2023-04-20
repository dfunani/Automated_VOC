# Email Services

A Python Package that is an abstraction of the Email_Listener Library,
used as an Email Service package for the Automated VOC process.

```EmailService
from email_listener import EmailListener # Used to interface with an Email-Box

```

## EmailService Class

The Service's base/main class encapsulating and abstracting the basic functionalities of the service.

1. Login (login) - encapsulates the process of accessing the Mailbox using the IMAP protocols.
2. Read (read) - encapsulates the process of reading the given folder for any unread Emails.
3. Listen (listen) - encapsulates the mailbox listener, which establishes a service connection for interfacing with the mailbox.

## Dependencies

1. email_listener
2. python-decouple

## Usage

```usage
from services.email.email_listener import EmailService

emailService = EmailService(self.email, self.password, self.folder, self.attachment_dest, self.read_dest, self.timeout)
emailService.login()
emailService.read() # Returns Dictionary of the Email Object (Refer to Returns below)
emailService.listen()
```

## Returns
![Emails Dictionary]('/Users/delalifunani/Documents/Github/Automated_VOC/services/email/visualize-json-data-graph.jpeg')
