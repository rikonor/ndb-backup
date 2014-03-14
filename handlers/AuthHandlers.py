# These handlers take care of Authenticating users using cookies,
# as well as Logins, Logouts and Signups.

import os, sys, time, datetime

from handlers.BaseHandler import BaseHandler
from models.models import User
from security import hashes
from security.data_validation import *

#--------------------------------------------------------------
# User handlers
#--------------------------------------------------------------
def Authenticate(request):
    h = request.cookies.get('name')
    user_id = hashes.check_secure_val(h)
    if user_id:
        user = User.get_by_id(int(user_id))
        return user
#--------------------------------------------------------------
def SetLoginCookies(request, user):
    user_id = str(user.key.id())
    secure_val = hashes.make_secure_val(user_id)
    request.response.headers.add_header('Set-Cookie', str("name=%s; Path=/" % secure_val))
#--------------------------------------------------------------
def ClearLoginCookies(request):
    request.response.headers.add_header("Set-Cookie", "name=; Path=/")
#--------------------------------------------------------------
class LogoutHandler(BaseHandler):

    def get(self):
        ClearLoginCookies(self)
        return self.redirect("/")
#--------------------------------------------------------------