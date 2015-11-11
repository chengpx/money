from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'library.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^/$','allbook.views.index'),
    url(r'^$','allbook.views.index'),
    url(r'^index/$','allbook.views.index'),
    url(r'^add_book/$','allbook.views.add_book'),
    url(r'^add_author/$','allbook.views.add_author'),
    url(r'^insert_author/$','allbook.views.insert_author'),
    url(r'^insert_book/$','allbook.views.insert_book'),
    url(r'^delete/$','allbook.views.delete'),
    url(r'^search_book/$','allbook.views.search_book'),
    url(r'^search_form/$','allbook.views.search_form'),
    url(r'^search_author/$','allbook.views.search_author'),
    url(r'^delete_form/$','allbook.views.delete_form'),
    url(r'^update_book/$','allbook.views.update_book'),
    url(r'^update/$','allbook.views.update'),
    url(r'^success/$','allbook.views.success'),
    url(r'^instruction/$','allbook.views.instruction'),
)
