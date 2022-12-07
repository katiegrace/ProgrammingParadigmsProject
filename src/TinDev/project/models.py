from django.db import models

# Create your models here.


def remove_stopWords(str):
    k = []
    words = str.split()
    z = words
    with open('/Users/celinaryan/Documents/GitHub/ProgrammingParadigmsProject/src/TinDev/project/templates/project/stopwords.txt', 'r') as f:
        for word in f:
            word = word.split('\n')
            k.append(word[0])

        p = [t for t in z if t not in k]
    return p

def compatabilityScore(post):
    likes = post.likes # list of cands that liked the post
#     #from the post
    preferred_skills = post.preferred_skills
    position_title = post.position_title
    description = post.description
    post_str_list= position_title + preferred_skills + description
    post_SW = remove_stopWords(post_str_list) # SW = stopwords

    scores={} # our scores dict that we will return

#     #from cand

    for cand in likes.all():
        skills = cand.skills
        bio = cand.bio
        cand_str_list = bio + skills
        cand_SW = remove_stopWords(cand_str_list)
        lenTotal= len(post_SW) + len(cand_SW)
        counter=0
        for word in post_SW:
            for skill in cand_SW:
                if word==skill:
                    counter+=1
                score = round((counter + 7 / lenTotal) * 100,2) # this is an arbitrary multiplication so the number isn't tiny
                scores[cand]=(score, cand.name)

    return scores

class CandidateProfile(models.Model):

    name = models.CharField(max_length=200)
    bio = models.CharField(max_length=300) # added
    zipcode = models.CharField(max_length=10)
    skills = models.CharField(max_length=300)
    git_username = models.CharField(max_length=200) # added
    years_exp = models.CharField(max_length=3)
    username =  models.CharField(max_length=200)
    password = models.CharField(max_length=200)
   
class RecruiterProfile(models.Model):

    name = models.CharField(max_length=200)
    company = models.CharField(max_length=300)
    zipcode = models.CharField(max_length=10)
    username =  models.CharField(max_length=200)
    password = models.CharField(max_length=200)


class Post(models.Model):
    position_title = models.CharField(max_length=200)
    position_type = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    preferred_skills = models.TextField(max_length=200)
    description = models.TextField(max_length=200)
    company = models.CharField(max_length=200)
    expiration_date = models.DateTimeField()
    status = models.CharField(max_length=200)
    #num_interested = models.CharField(max_length=100)
    recruiter= models.ForeignKey(RecruiterProfile, on_delete=models.CASCADE, default="")
    #for interested v. not
    likes = models.ManyToManyField(CandidateProfile, blank=True,related_name='likes')
    dislikes = models.ManyToManyField(CandidateProfile, blank=True, related_name='dislikes')
    #score = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE, default="")

    @property
    def scores(self):
        scr = compatabilityScore(self)
        #raise NotImplementedError(scr)
        return scr


class Offer(models.Model):
    #a offer is linked to a post, sent from a recruiter, to a candidate
    recruiterOff = models.ForeignKey(RecruiterProfile, on_delete=models.CASCADE, default="")
    candidateOff = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE, default="")
    postOff = models.ForeignKey(Post, on_delete=models.CASCADE, default="")
    salary_info = models.CharField(max_length=200)
    due_date = models.DateTimeField()
    # to see if the offer has expired
    expired = models.BooleanField(default=False)
    #to accept/deny
    #will either be "accept" or "decline"
    response = models.CharField(max_length=200)