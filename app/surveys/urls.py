from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()

router.register('surveys', views.SurveyViewSet)
router.register(
    'surveys/(?P<id>\d+)/questions',
    views.QuestionViewSet,
    basename='questions'
)
router.register(
    'surveys/(?P<id>\d+)/questions/(?P<question_pk>\d+)/choices',
    views.ChoiceViewSet,
    basename='choices'
)
router.register(
    'active_surveys',
    views.ActiveSurveyListViewSet,
    basename='active_surveys'
)
router.register(
    'surveys/(?P<id>\d+)/questions/(?P<question_pk>\d+)/answers',
    views.AnswerCreateViewSet,
    basename='answers'
)
router.register(
    'my_surveys',
    views.UserIDSurveyListViewSet,
    basename='list_userid_surveys'
)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]