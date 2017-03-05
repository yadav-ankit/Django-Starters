from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from userprofile.forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django import forms

global user

@login_required
def user_profile(request):
    if request.method== 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        form.save()
    else:
       # user:request.user
       # profile =user.profile
        form = UserProfileForm(instance =request.user.profile)

    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('user.html', args)
