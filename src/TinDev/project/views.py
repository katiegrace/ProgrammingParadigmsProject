from django.shortcuts import render
from django.shortcuts import render, redirect
from project.forms import CandidateForm
from project.models import CandidateProfile
from project.forms import RecruiterForm
from django.views.generic import ListView, DetailView
from project.models import RecruiterProfile
from django.contrib.auth import login
from project.forms import Post
from .forms import Post
from .forms import PostForm
from django.db.models import Q
from project.forms import OfferForm
from project.models import Offer
#from .models import post
#from django.views.generic import ListView

#first page of webpage
def index(request):
    return render(request, 'project/index.html', {'title':'index'})
  
def login(request):
    if request.POST:
        #get the username and password 
        uname = request.POST["username"]
        pwd = request.POST["password"]
        cand = CandidateProfile.objects.filter(username=uname, password=pwd)
        #len(cand) will be 0 if no candidates found and we need to check recruiters
        if len(cand) == 0:
            recruiter = RecruiterProfile.objects.filter(username=uname, password=pwd)
            #len(recruiter) will be 0 if no recruiters found
            if len(recruiter) == 0:
                return render(request, 'project/login.html', {"error":"Incorrect username or password"})
            else:
                #We should have 0 or 1, never more
                assert len(recruiter) > 0
                request.session["logged_user"] = uname
                return redirect("/recruiterDashboard")
        else:
            #We should have 0 or 1 candidates, never more
            assert len(cand) > 0
                # the candidate authenticated
            request.session["logged_user"] = uname
                #redirect to candidate dashboard
            return redirect("/candidateDashboard")
    # shows a login form instead of error
    return render(request, 'project/login.html')
    

def logout(request):
    del request.session["logged_user"]
    return redirect("/login")

#creating a candidate profile
def candidateProfile(request):
    if request.POST:
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(login)
    return render(request, 'project/candidateProfile.html', {'form':CandidateForm}) 

#creating a recruiter profile
def recruiterProfile(request):
    if request.POST:
        form = RecruiterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(login)
    return render(request, 'project/recruiterProfile.html', {'form':RecruiterForm}) 

# added context for scaalbility, before it said {'title':'Candidate'} but added context dictionary
def candidateDashboard(request):
    context={
        'home_page': "active",
    }
    return render(request, 'project/candidateDashboard.html', {'title':'Candidate'} )

def recruiterDashboard(request):
    context={
        'home_page': "active",
    }
    return render(request, 'project/recruiterDashboard.html',{'title':'Recruiter'} )

#recruiter creating a post
def create_post(request):
    if request.POST:
        form = PostForm(request.POST)
        
        if form.is_valid():
            #set the recruiter of the post to the logged in recruiter 
            recruiter = RecruiterProfile.objects.filter(username=request.session['logged_user'])[0]
            form.instance.recruiter = recruiter
            form.save()
            
            print(form.instance)
            # filter returns an array either 
            return redirect("/recruiterViewAllPosts")
        else:
            #raise ValueError(f"Form is not valid, errors {form.errors}")
            return render(request, 'project/create_post.html', {'form':form,"error":"Form is invalid"})
        #if they create a post we want it to take them to view all posts 
    return render(request, 'project/create_post.html', {'form':PostForm}) 



class CandidateIndexView(ListView):
    template_name = 'project/candidateViewPosts.html'
    context_object_name = 'post_list'
    def get_queryset(self):
        print(Post.objects.all().order_by('-expiration_date'))
        return (Post.objects.all().order_by('-expiration_date'))

def candidate_filter(request):
    #filter all the post objects to only include those in which in recruiter's username matched the one logged in
    uname_id = CandidateProfile.objects.filter(username=request.session['logged_user'])[0]

    #automatically goes to all posts
    #q_set = Post.objects.filter(recruiter= uname_id).order_by('-expiration_date')
    q_set = Post.objects.all().order_by('-expiration_date')
    filt = request.GET.get('filter')
    user_keyword = request.GET.get('keywords') #keywords
    user_location = request.GET.get('location') #location
    # get rid of required 

    # do we need to have another variable and get for the other boxes
    #only changes if it is set to something else 
    if filt == 'active':
        q_set = Post.objects.filter(Q(status="Active") | Q(status="active"))
        #q_set = q_set.filter(status='Active')
    elif filt == 'inactive':
        q_set = Post.objects.filter(Q(status="Inactive") | Q(status="inactive")).order_by('-expiration_date')
        #q_set = q_set.filter(status='Inactive')
    if user_keyword: # location should be LC, 141 desciption not keyword, 
        q_set = q_set.filter(description__icontains=user_keyword).order_by('-expiration_date')
    if user_location:
        q_set = q_set.filter(location=user_location).order_by('-expiration_date').distinct()

# MAKE IT NOT REQUIRED

    return render(request, 'project/candidateViewPosts.html',{'post_list':q_set}) 


class RecruiterIndexView(ListView):
    template_name = 'project/recruiterViewAllPosts.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        #return posts by the logged in recruiter
        uname_id = RecruiterProfile.objects.filter(username=self.request.session['logged_user'])[0]
        return (Post.objects.filter(recruiter=uname_id).order_by('-expiration_date'))


def recruiter_filter(request):
    #filter all the post objects to only include those in which in recruiter's username matched the one logged in
    uname_id = RecruiterProfile.objects.filter(username=request.session['logged_user'])[0]

    #automatically goes to all posts
    q_set = Post.objects.filter(recruiter= uname_id).order_by('-expiration_date')

    filt = request.GET.get('filter')
    #only changes if it is set to something else 
    if filt == 'active':
        q_set = Post.objects.filter(Q(recruiter=uname_id, status="Active") | Q(recruiter=uname_id, status="active"))
        #q_set = q_set.filter(status='Active')
    elif filt == 'inactive':
        q_set = Post.objects.filter(Q(recruiter=uname_id, status="Inactive") | Q(recruiter=uname_id, status="inactive")).order_by('-expiration_date')
        #q_set = q_set.filter(status='Inactive')
    elif filt == 'interested_cands':
        q_set = Post.objects.filter(recruiter= uname_id, likes__gte=1).order_by('-expiration_date').distinct()

    return render(request, 'project/recruiterViewAllPosts.html',{'post_list':q_set})


class CandPostDetailView(DetailView):
    model = Post
    template_name = 'project/cand_post_detail.html'

class RecPostDetailView(DetailView):
    model = Post
    template_name = 'project/rec_post_detail.html'

#delete a post
def delete(request, id):
  #find the post from the id
  post = Post.objects.get(id=id)
  #delete it from the database
  post.delete()
  return redirect('/recruiterViewAllPosts')

#update a post
def edit(request, id):
    #find the post from the id
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        #create a filled out form to edit, fill it with this isntance of post
        form = PostForm(request.POST, instance = post)

        #if it is valid, save it
        if form.is_valid():
            form.save()
            return redirect("/recruiterViewAllPosts")
    else:
        form = PostForm(instance=post)
    #if they create a post we want it to take them to view all posts 
    return render(request, 'project/post_update.html', {'form':form})
    return redirect('')

#like a post
def interest(request, id):
    #get the specific post from the objects
    post = Post.objects.get(id=id)
    is_dislike = False
    #go through all the dislikes for the post
    for dislike in post.dislikes.all():
        #if the candidate disliked it
        if dislike == CandidateProfile.objects.filter(username=request.session['logged_user'])[0]:
            is_dislike = True
            break
    if is_dislike:
        #remove the dislike
        post.dislikes.remove(CandidateProfile.objects.filter(username=request.session['logged_user'])[0])

    is_like = False
    # go through all the likes
    for like in post.likes.all():
        #if the candidate liked it
        if like == CandidateProfile.objects.filter(username=request.session['logged_user'])[0]:
            is_like = True
            break
    #if not already liked, add like
    if not is_like: 
        post.likes.add(CandidateProfile.objects.filter(username=request.session['logged_user'])[0])
    
    #if liked, and clicked like again, remove like
    if is_like:
        post.likes.remove(CandidateProfile.objects.filter(username=request.session['logged_user'])[0])
    
    #maybe try not redirecting?
    return redirect('/candidateViewPosts')


#dislike a post
def not_interest(request, id):
    #get the specific post from the objects
    post = Post.objects.get(id=id)
    is_like = False
    #go through all the likes for this post
    for like in post.likes.all():
        #if the logged in candidate liked it, set is_like flag to true
        if like == CandidateProfile.objects.filter(username=request.session['logged_user'])[0]:
            is_like = True
            break
    #if the user already liked it and just clicked like again, unlike, so remove from likes
    if is_like:
        post.likes.remove(CandidateProfile.objects.filter(username=request.session['logged_user'])[0])

    is_dislike = False
    #go through all dislikes for this post
    for dislike in post.dislikes.all():
        #if the candidate disliked it
        if dislike == CandidateProfile.objects.filter(username=request.session['logged_user'])[0]:
            #set is_dislike flag to tru
            is_dislike = True
            break
    #if user hasn't disliked it yet, dislike it
    if not is_dislike: 
        post.dislikes.add(CandidateProfile.objects.filter(username=request.session['logged_user'])[0])
    
    #if they already disliked it, and click the button again, undo, so remove from dislikes
    if is_dislike:
        post.dislikes.remove(CandidateProfile.objects.filter(username=request.session['logged_user'])[0])
    
    #maybe don't redirect them?
    return redirect('/candidateViewPosts')

class candidate_likes(ListView):
    template_name = 'project/candidateLikedPosts.html'
    context_object_name = 'post_list'
    def get_queryset(self):
        #get the logged in candidate
        uname_id = CandidateProfile.objects.filter(username=self.request.session['logged_user'])[0]
        #filter posts objects to return posts that this user has liked
        return (Post.objects.filter(likes = uname_id).order_by('-expiration_date'))

def send_offer(request, id, pk):
    if request.POST:
        form = OfferForm(request.POST)
        
        if form.is_valid():
            #link recruiter
            recruiter = RecruiterProfile.objects.filter(username=request.session['logged_user'])[0]
            form.instance.recruiterOff = recruiter

            #link candidate based on the name they input
            candidateOff = CandidateProfile.objects.get(id = pk)
            form.instance.candidateOff = candidateOff

            #link post to this post id
            postOff = Post.objects.get(id=id)
            form.instance.postOff = postOff

            # same form
            form.save()
            
            return redirect("/recruiterViewAllPosts")
        else:
            #Add proper error reporting to the user
            #raise ValueError(f"Form is not valid, errors {form.errors}")
            return render(request, 'project/create_offer.html', {'form':form,"error":"Form is invalid", "post_id":id, "candidate_id":pk})
        #if they create a post we want it to take them to view all posts 
    return render(request, 'project/create_offer.html', {'form':OfferForm, "post_id":id, "candidate_id":pk}) 


class CandidateOffers(ListView):
    template_name = 'project/candidateOffers.html'
    context_object_name = 'offer_list'

    def get_queryset(self):
        #return all offers for this candidate
        #get the candidate id logged in
        uname_id = CandidateProfile.objects.filter(username=self.request.session['logged_user'])[0]
        #return all offers to that candidate
        return (Offer.objects.filter(candidateOff=uname_id).order_by('-due_date'))


class CandOfferDetailView(DetailView):
    model = Offer
    template_name = 'project/cand_offer_detail.html'

#candidate accept an offet
def accept(request, id):
    #find the offer object
    offer = Offer.objects.get(id=id)

    #update the response field to true
    offer.response = True

    return redirect("/candidateOffers")


#candidate decline an offer
def decline(request, id):
    #find the offer object
    offer = Offer.objects.get(id=id)

    #update the response field to false
    offer.response = False

    return redirect("/candidateOffers")