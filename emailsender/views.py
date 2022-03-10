from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.shortcuts import redirect
from api.models import *
from decouple import config
import api.emailpatteren as verfied
import api.sms as sm
from passlib.hash import django_pbkdf2_sha256 as handler
import jwt
import re
from api.serilizer import *
import datetime
from emailsender.task import *


tokenkey = config('clientjwt')

##Token Expire check for user
def tokenauth(tokencatch):

    try:
        my_token = jwt.decode(tokencatch,tokenkey, algorithms=["HS256"])
        obj = UserSignup.objects.get(uid = my_token['uid'])
        if obj.account_Status == "True" and my_token['pwd'] == obj.password[-10:]:
            return my_token
        else:
            return False
      


    except jwt.ExpiredSignatureError:
        return False

    except:
        return False



####### validate an Email #############

def checkemailforamt(email):
    emailregix = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if(re.match(emailregix, email)):

        return email

    else:
       return False


####For Scripting######

class emailSender(APIView):
    def post(self,request):
        try:
            emailObj = request.data
            if emailObj:
                for j in emailObj:
                    checkalreadyExist = emailRecord.objects.filter(Email = j['email'] )
                    if not checkalreadyExist:
                        data = emailRecord(Fname = j['fname'],Lname = j['lname'],Email = j['email'],mobile = j['mobile'])
                        data.save()

                    

                ####Sending a email######
                mobilelist = list()
                clickstatus = emailRecord.objects.filter(sendstatus = "False")
                if clickstatus:
                    for e in clickstatus:
                        
                        emailstatus = verfied.publicity('Promotion',config('EMAIL_HOST_USER'),e.Email,request.META['HTTP_HOST'])
                        mobilelist.append({'id':e.id,'mobile':e.mobile})

                    return Response({'status':True,'message':"Email send Successful",'users':mobilelist})


                
                else:
                    return Response({'status':False,'message':"Email Already send for this users"})
                



            else:
                return Response({'status':False,'message':'Array is empty'})

        except Exception as e:
            return Response({'status':False,'message':str(e)})


#####for testing emails
class testingemailSender(APIView):
    def post(self,request):
        try:
         
                    

            ####Sending a email######
            mobilelist = list()
            clickstatus = emailRecord.objects.filter(sendstatus = "Beta")
            if clickstatus:
                for e in clickstatus:
                    
                    emailstatus = verfied.publicity('Promotion',config('EMAIL_HOST_USER'),e.Email,request.META['HTTP_HOST'])
                    mobilelist.append({'id':e.id,'mobile':e.mobile})

                return Response({'status':True,'message':"Email send Successful",'users':mobilelist})


            
            else:
                return Response({'status':False,'message':"Email Already send for this users"})
                



        except Exception as e:
            return Response({'status':False,'message':str(e)})




class emailconfirmation(APIView):
    def get(self,request,email):
        try:
            data = emailRecord.objects.get(Email = email )
            data.sendstatus = "True"
            data.save()
            return redirect('https://evolutionmc.com.au')

        except:
            return redirect('https://evolutionmc.com.au')


       


class smsVerification(APIView):
    def get(self,request,emailid):
        try:
            data = emailRecord.objects.get(id = emailid )
            data.sendstatus = "True"
            data.save()
            return redirect('https://evolutionmc.com.au')

        except:
            return redirect('https://evolutionmc.com.au')
    


####For React####

class signup(APIView):
    def post(self,request):
        try:
            fname = request.data.get('fname')
            lname = request.data.get('lname')
            email = request.data.get('email')
            password = request.data.get('password')
            mobile = request.data.get('mobile')
            
                    
            ####All keys required validation
            if not 'email' in request.data or not 'password' in request.data or not 'fname' in request.data or not 'lname' in request.data or not 'mobile' in request.data:

                return Response({'status':False,'message':"fname,lname,email or password or mobile key is required"})

            ###Validation all fields are required
            if len(fname) == 0 or len(lname) == 0 or len(email) == 0 or len(password) == 0 or len(mobile) == 0:
                return Response({'status':False,'message':'All Fields are required'})


            ####Email validator
            email = checkemailforamt(email)
            if not email:
                return Response({'status':False,'message':'Email format is incorrect'})


            ###Minimum Password Length check
            if len(password) < 8:
                return Response({'status':False,'message':'Password Shoud be Minimum 8 Length'})




            checkexist = UserSignup.objects.filter(email = email)
            if checkexist:
                return Response({'status':False,'message':"Email already exist try another email"})


            else:
                UserSignup(fname = fname,lname = lname,email = email,mobile=mobile,password = handler.hash(password)).save()
                verfied.registrationEmail("Registration",fname,lname,config('EMAIL_HOST_USER'),email)
                return Response({'status':True,'message':"Account Created Successful"})

        except Exception as e:
            return Response({'status':False,'message':str(e)})



class login(APIView):
    def post(self,request):
        try:
            email = request.data.get('email')
            password = request.data.get('password')

            ####All keys required validation
            if not 'email' in request.data or not 'password' in request.data:
                return Response({'status':False,'message':"email or password key is required"})
            
            ###Validation all fields are required
    
            if len(email) == 0 or len(password) == 0:
                return Response({'status':False,'message':'Email or Password Required'})



            checkexist = UserSignup.objects.filter(email = email)
            if checkexist and handler.verify(password,checkexist[0].password):
                access_token_payload = {'uid':checkexist[0].uid,
                'fname':checkexist[0].fname,
                'lname':checkexist[0].lname,
                'mobile':checkexist[0].mobile,
                'email':checkexist[0].email,
                'profileimage':checkexist[0].profile.url,
                'pwd':checkexist[0].password[-10:],

                
                }
                
                access_token = jwt.encode(access_token_payload,tokenkey, algorithm='HS256').decode('utf-8')
                return Response({'status':True,'message':"Login Successful",'user':access_token_payload,'token':access_token})

            else:
                return Response({'status':False,'message':"Invalid Credential"})


        except Exception as e:
            return Response({'status':True,'message':str(e)})


class updateProfile(APIView):
    def get(self,request):
        try:
            head = request.META['HTTP_AUTHORIZATION']
            head = head[7:]
            token = tokenauth(head)
            if token:
                userObj = UserSignup.objects.get(uid = token['uid'])
                return Response({'status':True,'data':{

                        'fname':userObj.fname,
                        'lname':userObj.lname,
                        'mobile':userObj.mobile,
                        'email':userObj.email,
                        'profileimage':userObj.profile.url
                    }})

            else:
                return Response({
                    'status':False,
                    'message':'tokenexpire'
                })


        except Exception as e:
            return Response({'status':True,'message':str(e)})


    def post(self,request):
        try:
            head = request.META['HTTP_AUTHORIZATION']
            head = head[7:]
            token = tokenauth(head)
            if token:
                fname = request.data.get('fname')
                lname = request.data.get('lname')
                mobile = request.data.get('mobile')
                profile = request.FILES.get('profile',False)

                ####All keys required validation
                if not 'fname' in request.data or not 'lname' in request.data or not 'mobile' in request.data or not 'profile' in request.data:

                    return Response({'status':False,'message':"fname or lname or mobile or profile key is required"})
            
                ###Validation all fields are required
                
                if len(fname) == 0 or len(lname) == 0 or len(mobile) == 0:
                    return Response({'status':False,'message':'All Fields are required'})


                userObj = UserSignup.objects.get(uid = token['uid'])
                userObj.fname = fname
                userObj.lname = lname
                userObj.mobile = mobile
                if profile:
                    userObj.profile = profile

                userObj.save()

                return Response({'status':True,'message':'Update Profile Successful','user':{

                    'fname':userObj.fname,
                    'lname':userObj.lname,
                    'mobile':userObj.mobile,
                    'profileimage':userObj.profile.url
                }})

                

            else:
                return Response({
                    'status':False,
                    'message':'tokenexpire'
                })

        except Exception as e:
            return Response({'status':True,'message':str(e)})


class changePassword(APIView):
    def post(self,request):
        try:
            head = request.META['HTTP_AUTHORIZATION']
            head = head[7:]
            token = tokenauth(head)
            if token:
                password = request.data.get('password')
                oldpassword = request.data.get('oldpassword')

                ###Key Validation
                if not 'password' in request.data or not 'oldpassword' in request.data:
                    return Response({'status':False,'message':'Password & oldpassword Key is required'})




                ###Minimum Password Length check
                if len(password) < 8:
                    return Response({'status':False,'message':'Password Shoud be Minimum 8 Length'})

                else:
                    obj = UserSignup.objects.get(uid = token['uid'])
                    if handler.verify(oldpassword,obj.password):
                        obj.password = handler.hash(password)
                        obj.save()
                        return Response({'status':True,'message':'Password Update Successful'})

                    else:
                        return Response({'status':False,'message':'Your old password is incorrect'})



                    



            else:
                return Response({
                        'status':False,
                        'message':'tokenexpire'
                })




        except Exception as e:
            return Response({'status':False,'message':str(e)})
    



class referencelink(APIView):
    def get(self,request,ref,click):

        try:
            head = request.META['HTTP_AUTHORIZATION']
            head = head[7:]
            token = tokenauth(head)
            if token:

                ###check if both id is same
                if ref == click:
                    return Response({'status':False,'message':'You dont have right to use this reward'})
                ###check already reward

                data = UserReferalRecord.objects.filter(userReferenceId = ref,userClickId = click)
                if data:
                    return Response({'status':True,'link':f'{data[0].discountlink}'})



                else:
                    price = DiscountPrice.objects.all().first()
                    userRefObj = UserSignup.objects.get(uid = ref)
                    userClickObj = UserSignup.objects.get(uid = click)
                    UserReferalRecord(userReferenceId = userRefObj,userClickId = userClickObj,discountprice = price.price,discountlink = price.discountlink).save()
                    return Response({'status':True,'link':f'{price.discountlink}'})


            else:
                return Response({
                        'status':False,
                        'message':'tokenexpire'
                })



        except Exception as e:
            return Response({'status':False,'message':str(e)})
    


class changeReferStatus(APIView):
    def get(self,request):
        try:
            head = request.META['HTTP_AUTHORIZATION']
            head = head[7:]
            token = tokenauth(head)
            if token:
                fetchdata = UserReferalRecord.objects.filter(userReferenceId = token['uid'])
                fetchdata = SerUserReferalRecord(fetchdata,many=True).data
                return Response({'status':True,'data':fetchdata})
                


            else:
                return Response({
                        'status':False,
                        'message':'tokenexpire'
                })

        except Exception as e:
            return Response({'status':False,'message':str(e)})



    def post(self,request):
        try:
            email = request.POST['email']
            fetchdata = UserReferalRecord.objects.filter(userClickId__email = email,status = "pending")
            if fetchdata:
                for e in fetchdata:
                    e.status = "done"
                    e.save()

                ##first appointment count is add
                data = UserSignup.objects.get(email = email)
                if data.totalnoofappointment == 0:
                    data.totalnoofappointment = 1
                    data.save()


                emailstatus = verfied.statusDoneEmail('Refer Confirm',config('EMAIL_HOST_USER'),fetchdata[0].userReferenceId.email,fetchdata[0].userReferenceId.fname ,fetchdata[0].userReferenceId.lname)
                return Response({'status':True,'message':f'you win reward of {fetchdata[0].discountprice} but after admin approve this a confirmation email will be sent to you'})


            else:
                return Response({'status':False,'message':'record not match'})
        
        except Exception as e:
            return Response({'status':False,'message':str(e)})

class pendingreferUsers(APIView):
    def get(self,request):
        if not request.GET['all']:
         
            fetchdata = UserReferalRecord.objects.filter(status = "pending").values_list('userClickId__email', flat=True)

            if fetchdata:
                return Response({'status':True,'data':fetchdata})


            else:
                return Response({'status':False,'message':'No record found'})


        else:
            fetchdata = UserReferalRecord.objects.all().values_list('userClickId__email', flat=True)

            if fetchdata:
                return Response({'status':True,'data':list(set(fetchdata))})


            else:
                return Response({'status':False,'message':'No record found'})
            
     


class ratingEmail(APIView):
    def post(self,request):
        try:
            email = request.POST['email']

            ####Email validator
            email = checkemailforamt(email)
            if not email:
                return Response({'status':False,'message':'Email format is incorrect'})

            else:
                already = Rating.objects.filter(author__email = email)
                if not already:
                    emailstatus = verfied.review('Promotion',config('EMAIL_HOST_USER'),email,"https://pycare.co/rating")

                    if emailstatus:
                        return Response({'status':True,'message':'Email sent successfully'})


                    else:
                        return Response({'status':False,'message':'Email not sent successfully'})


                else:
                    return Response({'status':False,'message':'Already rated'})



        except Exception as e:
            return Response({'status':False,'message':str(e)})



class landingpageData(APIView):
    def get(self,request):
        try:
            price = DiscountPrice.objects.all().first()
            return Response({'status':True,'data':price.price})

        except Exception as e:
            return Response({'status':False,'message':str(e)})


class addRating(APIView):
    def get(self,request):
        try:
            adminStatus = request.GET['adminStatus']
            
            if adminStatus:
                ratingId = request.GET['id']
                data = Rating.objects.get(id = ratingId)
                return Response({'status':True,'data':{'ratingId':ratingId,'stars':data.stars,'review':data.review,'date':data.datetime.date(),'time':data.datetime.time().strftime("%H:%M:%S")}})


            else:
                token = tokenauth(request.META['HTTP_AUTHORIZATION'][7:])
                data = Rating.objects.filter(author = token['uid'])
                if data:
                    return Response({'status':True,'data':{'stars':data[0].stars,'review':data[0].review,'date':data[0].datetime.date(),'time':data[0].datetime.time().strftime("%H:%M:%S")}})
                
                else:
                    return Response({'status':False,'message':"You are not rated"})

        except Exception as e:
            return Response({'status':False,'message':str(e)})



    def post(self,request):
        try:
            token = tokenauth(request.META['HTTP_AUTHORIZATION'][7:])
            if token:
                stars = request.data.get('stars',False)
                review = request.data.get('review',False)
                siteHost = request.data.get('host',False)

                ###Key Validation
                if not 'stars' in request.data or not 'review' in request.data or not 'host' in request.data:
                    return Response({'status':False,'message':'stars,review,host keys is required'})

                ##Required fields validation
                if not stars or not review or not siteHost:
                    return Response({'status':False,'message':"stars,review,host field is required"})
                




                ##Already exist validation
                already = Rating.objects.filter(author = token['uid'] )
                if not already :
                    data = Rating(stars = stars,review = review,author = UserSignup.objects.get(uid = token['uid']))
                    data.save()
                    if int(stars) < 5:
                        emailstatus = verfied.reviewsendtoEmail('Promotion',config('EMAIL_HOST_USER'),"shakeebanwar250@gmail.com",siteHost+ f"/{data.id}",token['fname'].title() + " "+token['lname'].title(),"Recorded a new feedback so click on the button and view the response")
                        return Response({'status':True,'message':"Add Rating Successful"})

                    
                    else:
                        emailstatus = verfied.reviewsendtoEmail('Promotion',config('EMAIL_HOST_USER'),token['email'],"https://qrco.de/bc8rI5",token['fname'].title() + " "+token['lname'].title(),"Thanks for your feedback please click the below button and rating to the hospital")
                        return Response({'status':True,'message':"Add Rating Successful",'link':'https://qrco.de/bc8rI5'})
            
                else:
                    return Response({'status':False,'message':"You Already Rated"})



            else:
                return Response({
                            'status':False,
                            'message':'tokenexpire'
                    })


        except Exception as e:
            return Response({'status':False,'message':str(e)})




class thankyouemail(APIView):
    def post(self,request):
        try:
            fetchdata = UserSignup.objects.filter(email = request.data['email'])
            if fetchdata:
                if not fetchdata[0].totalnoofappointment == request.data['no_of_appointments']:
                    caldiff = request.data['no_of_appointments'] - fetchdata[0].totalnoofappointment
                
                    if caldiff == 4 or request.data['no_of_appointments'] == 3:
                    
                        fetchdata[0].totalnoofappointment = request.data['no_of_appointments']
                        fetchdata[0].save()
                        verfied.thankyouEmail('Thankyou',config('EMAIL_HOST_USER'),request.data['email'])
                        return Response({'status':True,'message':f'Add Total Apppointments Successful {fetchdata[0].email}'})

                    else:
                        return Response({'status':False,'message':'No of Appointments is not enough to send the thankyou email'})


                else:
                    return Response({'status':False,'message':'No of Appointments is not enough to send the thankyou email'})


            else:
                return Response({'status':False,'message':'Email not found'})   


        except Exception as e:
            return Response({'status':False,'message':str(e)})


class referalemail(APIView):
  
    def post(self,request):
        try:
            fetchdata = UserSignup.objects.filter(email = request.data['email'])
            if fetchdata:
                ##check if user already record feedback
                checkalready = Rating.objects.filter(author__email = fetchdata[0].email)
                if checkalready:
                    return Response({'status':False,'message':'This Person already record response'})

                valideCritarea = [5,9,13]
                if not request.data['no_of_appointments'] % 2 == 0:
                    if request.data['no_of_appointments'] in valideCritarea:
                        emailstatus = verfied.reviewsendtoEmail('Promotion',config('EMAIL_HOST_USER'),request.data['email'],"https://pycare.co/rating",fetchdata[0].fname.title() + " "+fetchdata[0].lname.title(),"Thankyou so much click the below button and record the feedback")
                        fetchdata[0].totalnoofappointment = request.data['no_of_appointments']
                        fetchdata[0].save()
                        return Response({'status':True,'message':f'Feedback email sent to {fetchdata[0].email}'})

                    else:
                        return Response({'status':False,'message':'No of Appointments is not enough to send the feedback email'})


                else:
                    return Response({'status':False,'message':'No of Appointments is not enough to send the feedback email'})
            
            
            else:
                return Response({'status':False,'message':'No of Appointments is not enough to send the feedback email'})



                
        except Exception as e:
            return Response({'status':False,'message':str(e)})      

  
        


class referalCompaign(APIView):
    def post(self,request):
        try:
            token = tokenauth(request.META['HTTP_AUTHORIZATION'][7:])
            if token:
                fname = request.data.get('fname',False)
                email = request.data.get('email',False)
                link = request.data.get('link',False)
                

                ###Key Validation
                if not 'fname' in request.data or not 'email' in request.data or not 'link' in request.data:
                    return Response({'status':False,'message':'fname,email,link keys is required'})

                ##Required fields validation
                if not fname or not email or not link:
                    return Response({'status':False,'message':"fname,email,link field is required"})
                        

                email = checkemailforamt(email)
                if email:
                    # verfied.referalCompaign("Share the ❤️ Friend! Refer & EARN NOW 😊",fname,config('EMAIL_HOST_USER'),email,link)

                    ##check if user is not refer
                    already = emailReferalrecord.objects.filter(userRecieve = email)
                    if not already:
                        ##Create User Record
                        data = emailReferalrecord(userReference = token['email'],userRecieve = email,recieverFirstname = fname,referFirstname = token['fname'],creation = datetime.datetime.now().date())
                        data.save()

                        verfied.referalCompaignEmailSend("Share the ❤️ Friend! Refer & EARN NOW 😊",config('EMAIL_HOST_USER'),email,3,token['fname'],fname)
                        return Response({'status':True,'message':'Invitation Sent Successful'})


                    else:
                        return Response({'status':False,'message':'You Already refer this Person'})

                else:
                    return Response({'status':False,'message':'Email Pattern is incorrect'})  

            else:
                return Response({'status':False,'message':'token is expire'})


        except Exception as e:
            return Response({'status':False,'message':str(e)})      



class referalCompaignCronJob(APIView):
    def get(self,request):
        try:
            todayDate = datetime.datetime.now().date()
            previousTwoDay = datetime.timedelta(days=2)
            previousTwoDay = todayDate - previousTwoDay
            previousTwoDay = emailReferalrecord.objects.filter(creation = previousTwoDay)
            
            userobj = list()
            if previousTwoDay:
                for j in previousTwoDay:
                    userobj.append({'reciever':j.userRecieve,'referFirstname':j.referFirstname,'recieverFirstname':j.recieverFirstname})

                

            previousThreeDays = datetime.timedelta(days=3)
            previousThreeDays = todayDate - previousThreeDays
            previousThreeDays = emailReferalrecord.objects.filter(creation = previousThreeDays)
            if previousThreeDays:
                for j in previousThreeDays:
                    userobj.append({'reciever':j.userRecieve,'referFirstname':j.referFirstname,'recieverFirstname':j.recieverFirstname})

                


            if len(userobj) > 0:
                referalCompaignEmailSend.delay("Share the ❤️ Friend! Refer & EARN NOW 😊",config('EMAIL_HOST_USER'),9,userobj)
                return Response({'status':True,'message':'Email sent successfully'})

            else:
                return Response({'status':False,'message':'No User is found'})


        except Exception as e:
            return Response({'status':False,'message':str(e)})      




class screenshotdetail(APIView):
    def post(self,request):
        emailstatus = verfied.screenshot("Schedule",config('EMAIL_HOST_USER'),"shakeebanwar250@gmail.com",eval(request.data['data']))
        if emailstatus:
            return Response({"status":True,'message':'Email send successfully'})

        else:
            return Response({'status':False,'message':"Email not send"})




#referalCompaignCronJOB

class referalCompaignCron(APIView):
    def post(self,request):
        try:
            # emailList = ["jawadsheikh224@gmail.com","test@evolutionmc.com.au","test1@evolutionmc.com.au","test2@evolutionmc.com.au","test3@evolutionmc.com.au","Shabih_haider1@outlook.com","shakeebanwar250@gmail.com","shoaibbilal101@gmail.com","mf4639@gmail.com"]

            emailList = ["shakeebanwar250@gmail.com"]

            fetchPattern = referalTemplate.objects.all().first()
            if fetchPattern:
               

                verfied.referalCronjobTemplate("Share the ❤️ Friend! Refer & EARN NOW 😊",config('EMAIL_HOST_USER'),emailList,fetchPattern.content)
                return Response({'status':True,'message':'Email Sent Successful'})

            else:
                return Response({"status":False,"message":"Email template not exist"})


        except Exception as e:
            return Response({'status':False,'message':str(e)})





class fetchAllUsers(APIView):
    def get(self,request):
        try:
            data = UserSignup.objects.all().values_list('email', flat=True)
            return Response({'status':True,'data':data})
        
        
        except Exception as e:
            return Response({'status':False,'message':str(e)})


class referalCompaignEmail(APIView):
    def post(self,request):
        try:
            email = request.data['email']
            count = request.data['no']
            data = UserReferalRecord.objects.filter(userClickId__email = email,status = "done").first()
            
            if int(count) == 5:
                if data:
                    clientName = data.userClickId.fname + " " + data.userClickId.lname
                    sendStatus = sm.sendsms(clientName.title(),data.userClickId.mobile)
                    if sendStatus:
                        return Response({'status':True,'message':sendStatus})
                    else:
                        return Response({'status':False,'message':'Phone number is invalid'})

                else:
                    return Response({'status':False,'message':'Not a Referal User'})

            else:
                
                if data:
                    referalFullname = data.userReferenceId.fname + " " + data.userReferenceId.lname 
                    clientName = data.userClickId.fname + " " + data.userClickId.lname
                    verfied.referalCompaignEmailSend("Referal Compaigns",config('EMAIL_HOST_USER'),email,count,referalFullname.title(),clientName.title())
                    return Response({'status':True,'message':'Email sent successfully'})

                else:
                    return Response({'status':False,'message':'Not a Referal User'})    



        except Exception as e:
            return Response({'status':False,'message':str(e)})



class refersmsSend(APIView):
    def post(self,request):
        try:
            name = request.data.get('name',False)
            number = request.data.get('number',False)
            
            
            ###Key Validation
            if not 'name' in request.data or not 'number' in request.data:
                return Response({'status':False,'message':'name,number keys is required'})

            ##Required fields validation
            if not name or not number:
                return Response({'status':False,'message':"name,number field is required"})
            
            
            smsStatus = sm.sendsms(name,number,True)
            if smsStatus:
                return Response({'status':True,'message':smsStatus})

            else:
                return Response({'status':False,'message':'Number is Invalid'})


        except Exception as e:
            return Response({'status':False,'message':str(e)})





class landingpage(APIView):
    def get(self,request):
        data = landingContent.objects.all().first()
        return HttpResponse(data.content,content_type='application/json')
       
  