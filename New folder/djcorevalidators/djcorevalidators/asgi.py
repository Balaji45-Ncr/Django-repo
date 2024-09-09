"""
ASGI config for djcorevalidators project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djcorevalidators.settings')

application = get_asgi_application()

'''
list methods
.append
.clear
.copy
.extends
.index
.insert
.reverse
.sort
.remove
.count
.pop


set methods
.add
.difference
.difference_update
.copy
.discard
.remove
.intersection
.intersection_update
.symmetric_difference
.symmetric_difference_update
.update
.union
.isdisjoint
.issubset
.issuperset
.pop
.clear


'''



