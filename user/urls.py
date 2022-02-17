from django.urls import path,include
from django.views.decorators.csrf import csrf_exempt
from rest_framework.routers import DefaultRouter
from .views import *

r = DefaultRouter()

r.register('',User_Class)
r.register('roles/permissions',RolePermsAPI,basename='roleperms')
r.register('advertisements/', AdvertisementsView,basename='advertisements')
r.register('news/', NewsList,basename='news')

urlpatterns = [
    path('',include(r.urls)),
    path('select/gym/',Selected_gym.as_view()),
    path('subscribed/userslist/',SubscribedUserList.as_view()),
    path('history/userhistory/<str:pk>/',UserHistoryDetail.as_view()),  

    # Class Booking
    path('bookclass/list/',BookClass.as_view()),
    path('subscription/user/',subscription.as_view()),

    path('class/Bookings/',Bookings.as_view()),
    path('upcomingclass/list/',UpcomingBookClass.as_view()),

    path('admin/create/',AdminCreateList.as_view()),
    path('admin/action/<str:pk>/',AdminAction.as_view()),
    path('admin/login/',csrf_exempt(AdminLoginView.as_view())),
    path('export/csv/',user_data_async),

    # Course Booking
    path('bookcourse/list/',BookCourse.as_view()),
    path('course/Bookings/',CourseBookings.as_view()),
    path('upcomingcourse/list/',UpcomingBookCourse.as_view()),
     
    path('home/user_profile/',UserProfile.as_view()),
    path('home/schedule/',GetSchedules.as_view()),
    path('home/course_schedule/',GetCourseSchedules.as_view()),
     
    path('home/cancel_class/',CancelClass.as_view()),
    path('home/cancel_course/',CancelCourse.as_view()),
    path('home/get-header/', GetHeader.as_view(), name='get-header'),

    path('Favourite/',FavouriteGymview.as_view()),

]