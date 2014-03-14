import re
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
EMAIL_RE= re.compile(r"^[\S]+@[\S]+\.[\S]+$")

def valid_username(username):
     return USER_RE.match(username)

def valid_email(email):
     return email=="" or EMAIL_RE.match(email)

def valid_password(password):
     return PASS_RE.match(password)