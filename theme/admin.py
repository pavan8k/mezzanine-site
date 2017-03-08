from django.contrib import admin
from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin
from .models import HomePage

class SlideInline(TabularDynamicInlineAdmin):
	model = Slide

class IconBlurbline(TabularDynamicInlineAdmin):
	model = IconBlurb

class HomePageAdmin(PageAdmin):
	inlines = (SlideInline, IconBlurbline)
	admin.site.register(HomePage, HomePageAdmin)
	admin.site.register(Portfolio, PageAdmin)