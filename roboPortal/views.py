from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from .models import portalUser, Team
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import portalUserSerializer, teamserializer


subject_roboPortalVerification = 'Verify your Robo Portal Email Address. '
message_verification = ' it  means a world to us '
subject_robathon = 'Robo Portal Selection'
message_robathon = ' Congrats.You have been selected for the hackathon.'
email_from = settings.EMAIL_HOST_USER

import random
import string

User = settings.AUTH_USER_MODEL


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

@login_required(login_url='/rest-auth/login/')
def home(request):
    if request.user.portal.is_complete:
        if request.user.portal.joined_team == False:
            if 'create' in request.POST:
                name = request.POST['teamName']
                team = Team(admin = request.user,name = name)
                team.save()
                team.member.add(request.user)
                token = randomString(15)
                token += str(team.id)
                temp_id = team.id
                team.token = token
                team.save()
                portal_user = portalUser.objects.get(user = request.user)
                portal_user.joined_team = True
                portal_user.user_team_id = int(temp_id)
                portal_user.is_admin = True
                portal_user.save()
                message = "Team has been created"
                return render(request,'team.html',{'team':team,'message':message})
            if 'join' in request.POST:
                token = request.POST['token']
                try:
                    team = Team.objects.get(token = token)
                    team.member.add(request.user)
                    portal = portalUser.objects.get(user = request.user)
                    portal.joined_team = True
                    portal.user_team_id = team.id
                    portal.save()
                    message = "Sucessfully added to team " + team.name
                    return render(request,'team.html',{'team':team,'message':message})
                except Team.DoesNotExist:
                    message = "Invalid Team Token"
                    return render(request,'joinCreate.html',{'message':message})
            return render(request,'joinCreate.html')
        else:
            team = Team.objects.get(id = request.user.portal.user_team_id)
            return render(request,'team.html',{'team':team})
    else:
        if 'create' in request.POST:
            portal = portalUser.objects.get(user = request.user)
            resume = None
            if 'resume' in request.FILES:
                resume = request.FILES['resume']
            description = request.POST['description']
            college = request.POST['college']
            branch = request.POST['branch']
            semester = request.POST['semester']
            portal.description = description
            portal.resume = resume
            portal.college = college
            portal.branch = branch
            portal.semester = semester
            portal.is_complete = True
            portal.save()
            redirect('/robothon/')

        return render(request,'createProfile.html',{'message':"Please complete your details first"})


@api_view(['GET','POST'])
@login_required(login_url='/rest-auth/login/')
def home_api(request):
    if request.user.portal.joined_team == False:
        if 'create' in request.POST:
            name = request.POST['teamName']
            team = Team(admin = request.user,name = name)
            team.save()
            team.member.add(request.user)
            token = randomString(15)
            token += str(team.id)
            temp_id = team.id
            team.token = token
            team.save()
            portal_user = portalUser.objects.get(user = request.user)
            portal_user.joined_team = True
            portal_user.user_team_id = int(temp_id)
            portal_user.is_admin = True
            portal_user.save()
            message = "Team has been created"
            dict = {'data':request.data,'message':message,'token':team.token}
            return Response(dict)
            # return render(request,'team.html',{'team':team,'message':message})

        if 'join' in request.POST:
            token = request.POST['token']
            try:
                team = Team.objects.get(token = token)
                team.member.add(request.user)
                portal = portalUser.objects.get(user = request.user)
                portal.joined_team = True
                portal.user_team_id = team.id
                portal.save()
                message = "Sucessfully added to team " + team.name
                serializer = teamserializer(team)
                # print(serializer1.data)
                print(team.member.count())
                dict = {'datasss':serializer.data}
                return Response(dict)
                # return render(request,'team.html',{'team':team,'message':message})
            except Team.DoesNotExist:
                message = "Invalid Team Token"
                dict = {'datasssqq':request.data,'message':message}
                return Response(dict)
                # return render(request,'joinCreate.html',{'message':message})
        return render(request,'joinCreate.html')
    else:
        team = Team.objects.get(id = request.user.portal.user_team_id)
        print(team.member)
        serializer = teamserializer(team)
        dict = {'dataqqqqq':serializer.data}
        return Response(dict)
        # return render(request,'team.html',{'team':team})

# def register(request):
#     global subject_roboPortalVerification, message_verification, email_from
#     if 'register' in request.POST:
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         username = request.POST['username']
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#         """
#             elif User.objects.filter(email = email).exists():
#                 return render(request,'register.html',{'error_message':"Email already taken"})
#             """
#         if password1 == password2:
#             if User.objects.filter(username = username).exists():
#                 return render(request,'register.html',{'error_message':"Username already taken"})
#             else:
#                 # user= User.objects.create_user(username = username, password = password1, email = email, first_name= first_name, last_name = last_name)
#                 # user.save()
#                 a= portalUser(user = user)
#                 a.save()
#                 recipient_list = [user.email,]
#                 random_string = randomString(25)
#                 random_string += str(user.id)
#                 token = Token(token = random_string)
#                 token.save()
#                 email_verify_html = "<a href = 'http://127.0.0.1:8000/roboPortal/verify/" +random_string + "/"+ str(user.id) + "'> Verify</a>"
#                 send_mail( subject_roboPortalVerification, message_verification, email_from,recipient_list,fail_silently=False,html_message= email_verify_html  )
#                 return redirect('/roboPortal/login/')
#         else:
#             return render(request,'register.html',{'error_message':"Password does not match"})
#     return render(request,'register.html')
#
#
# def login(request):
#     if 'login' in request.POST:
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(username = username, password = password)
#         if user != None:
#             if user.portal.verified == True:
#                 auth.login(request,user)
#                 return redirect('/')
#             else:
#                 raise Http404("You are not verified yet.")
#         else:
#             return render(request, 'login.html', {'error_message': "Invalid Credentials"})
#     return render(request, 'login.html')


# def email(request):
#     subject = 'Thank you for registering to our site'
#     message = ' it  means a world to us '
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = ['tuhina840@gmail.com',]
#     send_mail( subject, message, email_from, recipient_list,html_message= email_verify_html ,fail_silently=True )
#     return HttpResponse("views used and email sent attempted")


# def verify(request,token,id):
#     if Token.objects.filter(token = token).exists() == False:
#         raise Http404("Invalid Token.")
#     else:
#         user = User.objects.get(id = id)
#         if user.portal.verified == True:
#             raise Http404("Already verified")
#         else:
#             a = portalUser.objects.get(user = user)
#             a.verified = True
#             a.save()
#             print(user.portal.verified)
#             return HttpResponse("You have now been verified.")

@login_required
def createProfile(request):
    if 'create' in request.POST:
        portal = portalUser.objects.get(user = request.user)
        resume = None
        if 'resume' in request.FILES:
            resume = request.FILES['resume']
        description = request.POST['description']
        portal.description = description
        portal.resume = resume
        portal.save()
        return HttpResponse("Updated")

    return render(request,'createProfile.html')
@login_required
def adminView(request):
    if request.user.portal.is_member == True:
        all_team = Team.objects.all()
        return render(request,'adminView.html',{'all_team':all_team})
    else:
        raise Http404("You are not authorized as you are not robotix club member")

@login_required
def profileView(request,user_id):
    user = User.objects.get(id = user_id)
    return render(request,'profile.html',{'profile_user':user})

@login_required
def select(request,team_id):
    global subject_robathon,message_robathon
    team = Team.objects.get(id = team_id)
    team.selected = True
    team.save()
    email_from = settings.EMAIL_HOST_USER
    recipient_list = []
    for user in team.member.all():
        recipient_list.append(user.email)
    send_mail( subject_robathon, message_robathon, email_from, recipient_list ,fail_silently=False )
    return HttpResponse("ok")
"""
def create(request):
    team = Team(admin = request.user)
    team.save()
    return HttpResponse("hiiii")
"""
