from django.urls import path
from .views import hackathon_feed, hackathon_create, submission_create, user_registration, user_login, hackathon_enroll, hackathon_enrolled, submission_user,unauthorized


handler403 = 'api.views.unauthorized'

urlpatterns = [
    path('hackathons/', hackathon_feed, name='hackathon-feed'),
    path('hackathons/create/', hackathon_create, name='hackathon-create'),
    path('hackathons/enroll/<int:hackathon_id>/', hackathon_enroll, name='enroll-hackathon'),
    path('submissions/create/', submission_create, name='submission-create'),
    path('user/register/', user_registration, name='user-registration'),
    path('user/login/', user_login, name='user-login'),
    path('user/hackathons/enrolled/', hackathon_enrolled, name='enrolled-hackathons'),
    path('user/submissions/<int:user_id>/', submission_user, name='user-submissions'),
    path('unauthorized/', unauthorized, name='unauthorized')
]
