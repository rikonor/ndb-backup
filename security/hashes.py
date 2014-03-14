import hashlib
import hmac
import random
import string

SECRET = "laura"

def hash_str(s):
	# return hashlib.md5(s).hexdigest()
	return hmac.new(SECRET, s).hexdigest()

def make_secure_val(s):
	return "%s|%s" % (s, hash_str(s))

def check_secure_val(h):
	if h:
		val = h.split('|')[0]
		if h == make_secure_val(val):
			return val

def make_salt():
	return ''.join(random.choice(string.letters) for x in xrange(5))

# Make a password hash of the format H(name+pw+salt),salt
def make_pw_hash(name, pw, salt = None):
    if not salt:
    	salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return "%s|%s" % (h, salt)

def valid_pw(name, pw, h):
	salt = h.split('|')[1]
	return h == make_pw_hash(name, pw, salt)