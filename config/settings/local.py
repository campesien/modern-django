from .base import *
SECRET_KEY = env('DJANGO_SECRET_KEY', default='8wos(qcf*s(zj=*#qku-u&o9v=sf@iok+d&+im#s@sndtnq_tr')
DEBUG = env.bool('DJANGO_DEBUG', default=True)

