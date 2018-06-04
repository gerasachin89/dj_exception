from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from djbugger.models import ExceptionsHistory
from djbugger.middleware import format_exception
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def success(request):
    object_list = ExceptionsHistory.objects.all()
    return render(request, 'exception_list.html',{'object_list':object_list})

class ExceptionList(ListView):
    model = ExceptionsHistory
    template_name = 'exception_list.html'
    #paginate_by = 10  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super(ExceptionList,self).get_context_data(**kwargs)
        object_list = ExceptionsHistory.objects.filter(status="Pending")
        paginator = Paginator(object_list, 5) # Show 25 contacts per page

        page = self.request.GET.get('page')
        try:
            exceptions = paginator.page(page)
        except PageNotAnInteger:
            exceptions = paginator.page(1)
        except EmptyPage:
            exceptions = paginator.page(paginator.num_pages)
        context['object_list'] = exceptions
        return context

class ExceptionDetail(DetailView):
    model = ExceptionsHistory
    template_name = 'exception_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ExceptionDetail,self).get_context_data(**kwargs)
        exception_obj = ExceptionsHistory.objects.get(id=self.kwargs['pk'])
        print("AAAAAAAAAAAAAAAAAa", exception_obj.detail)
        # exception_detail = format_exception(exception_obj.detail)
        context['object'] = exception_obj
        return context
