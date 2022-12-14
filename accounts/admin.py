from turtle import color
from django.contrib import admin
from .models import Candidate
from django.utils.html import format_html

# Register your models here.

class CandidateAdmin(admin.ModelAdmin):
    list_filter = ['situation']
    list_display = ['id','first_name','last_name','job','age','email','phone', 'message', 'status', '_']

    #Function to change the icons
    def _(self, obj):
        if obj.situation == 'Approved':
            return True
        elif obj.situation == 'Pending':
            return None
        else:
            return False
    _.boolean = True

    #Function to colour the text
    def status(self, obj):
        if obj.situation == 'Approved':
            color = '#28a745'
        elif obj.situation == 'Pending':
            color = '#fea95e'
        else:
            color = 'red'
        return format_html('<strong> <p style="color: {}"> {} </p> </strong>'.format(color, obj.situation))
    status.allow_tags = True

admin.site.register(Candidate, CandidateAdmin)