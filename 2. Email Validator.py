import re
import json


class NameTooShortError(Exception):
    pass


class NameTooLongError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class InvalidNameError(Exception):
    pass


MIN_LENGHT = 4
MAX_LENGHT = 12
VALID_DOMAIN = (".com", ".bg", ".net", ".org")
valid_name_email = r'(\w+)'
valid_domain_email = r'(\..+)$'

flag = False
while True:
    email = input()

    if flag:
        break

    if email.count("@") > 1:
        raise MustContainAtSymbolError("Email should contain only one @ symbol!")

    email_name, domain = email.split("@")

    if len(email_name) < MIN_LENGHT:
        raise NameTooShortError("Name must be more than 4 characters")
    elif len(email_name) > MAX_LENGHT:
        raise NameTooLongError("Name must be less than 12 characters")

    matches_domain = re.findall(valid_domain_email, domain)
    if matches_domain[0] not in VALID_DOMAIN:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    matches = re.findall(valid_name_email, email_name)
    if matches[0] != email_name:
        raise InvalidNameError("Name can contain only letters, digits and underscores!")

    flag = True
    d = {"email": email}
    f = open("email.json", "w")
    json.dump(d, f)
    f.close()





