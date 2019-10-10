from hashlib import md5
grav_url = 'https://www.gravatar.com/avatar/' + md5(b'gregdelozier@mac.com').hexdigest()
print(grav_url)