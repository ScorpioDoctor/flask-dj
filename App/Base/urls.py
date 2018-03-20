
from .views import *

urls = [
    ('/sendsms', sendsms, ['POST']),
    ('/apply', apply, ['POST'])
]

