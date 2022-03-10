from django.contrib import admin
from django.urls import path,include
from emailsender.views import *

#for images
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('tinymce/', include('tinymce.urls')),
    path('admin/', admin.site.urls),
    path('emailSender',emailSender.as_view()),
    path('testingemailSender',testingemailSender.as_view()),
    path('smsVerification/<int:emailid>',smsVerification.as_view()),
    path('emailconfirmation/<str:email>',emailconfirmation.as_view()),
    path('signup',signup.as_view()),
    path('login',login.as_view()),
    path('changePassword',changePassword.as_view()),
    path('updateProfile',updateProfile.as_view()),
    path('referencelink/<int:ref>/<int:click>',referencelink.as_view()),
    path('changeReferStatus',changeReferStatus.as_view()),
    path('pendingreferUsers',pendingreferUsers.as_view()),
    path('ratingEmail',ratingEmail.as_view()),
    path('landingpageData',landingpageData.as_view()),
    path('addRating',addRating.as_view()),
    path('thankyouemail',thankyouemail.as_view()),
    path('referalemail',referalemail.as_view()),
    path('referalCompaign',referalCompaign.as_view()),
    path('referalCompaignCronJob',referalCompaignCronJob.as_view()),
    path('screenshotdetail',screenshotdetail.as_view()),
    path('referalCompaignCron',referalCompaignCron.as_view()),
    path('fetchAllUsers',fetchAllUsers.as_view()),
    path('referalCompaignEmail',referalCompaignEmail.as_view()),
    path('refersmsSend',refersmsSend.as_view()),
    path('landingpage',landingpage.as_view()),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



admin.site.site_header = "Admin"
admin.site.site_title = "Shakeeb Admin Portal"
admin.site.index_title = "Welcome to Evalutional medical center"