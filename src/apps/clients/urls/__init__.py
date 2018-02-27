from django.urls import path

from apps.clients.views import ClientListView, ClientDetailView, \
    ClientDeleteView, ClientCreateView, ClientVotingView

app_name = 'clients'

urlpatterns = [
    path('', ClientListView.as_view(), name='list'),
    path('<int:pk>/', ClientDetailView.as_view(), name='detail'),
    path('create/', ClientCreateView.as_view(), name='create'),
    path('<int:pk>/delete/', ClientDeleteView.as_view(), name='delete'),
    path('voting/', ClientVotingView.as_view(), name='voting')
]
