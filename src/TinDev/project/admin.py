from django.contrib import admin

# Register your models here.

from .models import CandidateProfile
from .models import RecruiterProfile
from .models import Post
from .models import Offer

admin.site.register(CandidateProfile)
admin.site.register(RecruiterProfile)
admin.site.register(Post)
admin.site.register(Offer)

