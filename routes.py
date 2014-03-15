#!/usr/bin/env python
# -*- coding: utf-8 -*-

from handlers import *
from handlers.MainHandlers import *
from handlers.ndbBackup import *
from handlers.ndbRecover import *

#This is the place where all of your URL mapping goes
route_list = [
	('/', MainPage),
	('/signup', SignupPageHandler),
	('/login', LoginPageHandler),
	('/logout', LogoutPageHandler),
	('/new', AddPageHandler),
	('/history', HistoryPageHandler),
	('/remove', RemoveHandler),
	('/ndbbackup', ndbBackup),
	('/ndbrecover', ndbRecover),
	('/ndbrecoverupload', ndbRecoverUpload),
]