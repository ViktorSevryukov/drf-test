from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView

from apps.clients.forms import ClientCreateForm, ClientFilterForm
from apps.clients.models import Client


class ClientListView(LoginRequiredMixin, ListView):
    """
    List clients
    """

    model = Client
    template_name = 'clients/list.html'
    context_object_name = 'clients'
    paginate_by = 10

    def get_queryset(self):
        """
        Add filters and ordering
        """
        qs = self.model.objects.all()

        form = self.get_filter_form()
        if form.is_valid():
            name_filter = form.cleaned_data['full_name']
            order_val = form.cleaned_data['ordering']

            words = name_filter.split()  # get parts of query to filter
            for word in words:
                # filter clients by first or last name
                qs = qs.filter(
                    Q(first_name__icontains=word) | Q(
                        last_name__icontains=word)
                )

            if order_val:
                qs = qs.order_by(order_val)

        return qs

    def get_context_data(self, **kwargs):
        """
        Add filter and ordering values to context
        """
        context = super(ClientListView, self).get_context_data(**kwargs)

        context['filter_form'] = self.get_filter_form()
        return context

    def get_filter_form(self):
        """
        Get form with filters
        :return: 
        """
        return ClientFilterForm(self.request.GET)


class ClientDetailView(LoginRequiredMixin, DetailView):
    """
    Get detailed client info
    """
    model = Client
    template_name = 'clients/detail.html'


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    """
    Delete client
    """
    model = Client
    template_name = 'clients/confirm_delete.html'
    success_url = reverse_lazy('clients:list')


class ClientCreateView(LoginRequiredMixin, CreateView):
    """
    Create client
    """
    model = Client
    form_class = ClientCreateForm
    template_name = 'clients/create.html'
    success_url = reverse_lazy('clients:list')


class ClientVotingView(LoginRequiredMixin, ListView):
    """
    List clients for voting
    """
    model = Client
    queryset = Client.objects.filter(photo__isnull=False)
    template_name = 'clients/voting.html'
    context_object_name = 'clients'
    paginate_by = 10


