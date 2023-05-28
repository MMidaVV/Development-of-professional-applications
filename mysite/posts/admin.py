from django.contrib import admin
from .models import Likes
from .models import Users
from .models import Images
from .models import Subscribes
from .models import Posts


admin.site.register(Users)
admin.site.register(Likes)
admin.site.register(Subscribes)
admin.site.register(Images)
admin.site.register(Posts)

