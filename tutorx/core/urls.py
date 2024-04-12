# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('api/client/dashboard/', ClientDashboardAPIView.as_view(), name='client-dashboard'),
    path('api/client/dashboard/<int:pk>', TutorDetailView.as_view(), name='tutor-list'),
    path('api/client/dashboard/<int:client_id>/client-notifications/', ClientNotificationListView.as_view(), name='tutor-list'),
    path('api/tutor/dashboard/<int:tutor_id>/', TutorDashboardAPIView.as_view(), name='tutor-dashboard'),
    path('api/tutor-profile/<int:pk>/', TutorProfileView.as_view(), name='tutor_profile_update'),
    path('api/tutor-profile/update/<int:pk>/', TutorProfileUpdateView.as_view(), name='tutor_profile_update'),
    path('api/tutor/<int:tutor_id>/booking/', TutorBookingCreateView.as_view(), name='book-tutor'),
    path('api/tutor/<int:client_id>/requests/', TutorRequestListView.as_view(), name='tutor-request-list'),
    path('api/rating/<int:tutorbooking_id>', TutorRatingCreateView.as_view(), name = 'rating'),
    path('api/tutor/dashboard/<int:tutor_id>/tutor-notifications/', TutorNotificationListView.as_view(), name='notification-list'),
    path('api/tutor/dashboard/<int:tutor_id>/tutor-notifications/<int:pk>/', TutorNotificationDetailView.as_view(), name='notification-detail'),
    path('api/ongoing-jobs/', OngoingJobListView.as_view(), name='ongoing-job-list'),
    path('api/completed-jobs/', CompletedJobListView.as_view(), name='completed-job-list'),
    path('api/ongoing-jobs/<int:pk>/complete/', OngoingJobCompleteView.as_view(), name='ongoing-job-complete'),
    #path('api/send-tutor-request/', TutorRequestCreateView.as_view(), name='send-tutor-request'),
    #path('api/rating', TutorRating.as_view(), name = 'rating'),
]
