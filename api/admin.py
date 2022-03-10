from django.contrib import admin
from api.models import *
# Register your models here.

class AdminemailRecord(admin.ModelAdmin):
    
    list_display=('Fname','Lname','Email','mobile','sendstatus')
 

class combine(AdminemailRecord,adminemailRecord):
    pass
     

class AdminReferalLink(admin.ModelAdmin):
    list_display = ('userReferenceId','userClickId','discountprice','status')


class combineReference(AdminReferalLink,adminUserReference):
    pass



class AdminUserSignup(admin.ModelAdmin):
    list_display = ('fname','lname','email','mobile')


class combineUsers(AdminUserSignup,adminUserSignup):
    pass



class AdminShowRating(admin.ModelAdmin):
    list_display = ('author','stars','datetime')


class combineAdminShowRating(AdminShowRating,adminRating):
    pass




admin.site.register(emailRecord,combine)
admin.site.register(UserSignup,combineUsers)
admin.site.register(UserReferalRecord,combineReference)
admin.site.register(DiscountPrice)
admin.site.register(Rating,combineAdminShowRating)
admin.site.register(landingContent)
admin.site.register(emailReferalrecord)
admin.site.register(referalCompaign)






