import re

def main():
    subject = "Fwd: Attention: Ayoba Developer Portal"
    body = """To *Ayoba team*,
This is an automatically generated email to notify you that a new
publication request has been created on Ayoba Developer Portal: Developer
Name: Katlego MicroApp Id: 584 Kindly add the microApp on the onboarding
process sheet and provide you with feedback on the outcome of the Vetting
and Compliance checks. Kind Regards, Ayoba team."""
    message = re.match(r".* MicroApp Id: ([\d]+) .*", body, re.IGNORECASE|re.MULTILINE)
    print(message)
    if message:
        print(message.groups())

if __name__ == "__main__":
    main()