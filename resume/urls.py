from django.conf.urls import include, url

urlpatterns = [

	url(r'^upload', 'resume.views.upload', name='upload'),
	url(r'^all/$', 'resume.views.resumes'),
	url(r'^get/(?P<resume_id>\d+)/$', 'resume.views.resume'),
	]