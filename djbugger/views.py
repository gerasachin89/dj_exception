from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from djbugger.models import ExceptionsHistory
from djbugger.middleware import format_exception
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.urlresolvers import reverse
from django.db.models import Q

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
        object_list = ExceptionsHistory.objects.filter(Q(status="Pending") | Q(status="Hold"))
        paginator = Paginator(object_list, 5) # Show 25 contacts per page

        page = self.request.GET.get('page')
        try:
            exceptions = paginator.page(page)
        except PageNotAnInteger:
            exceptions = paginator.page(1)
        except EmptyPage:
            exceptions = paginator.page(paginator.num_pages)
        context['total_count'] = object_list.count()
        context['object_list'] = exceptions
        return context

class ExceptionDetail(DetailView):
    model = ExceptionsHistory
    template_name = 'exception_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ExceptionDetail,self).get_context_data(**kwargs)
        exception_obj = ExceptionsHistory.objects.get(id=self.kwargs['pk'])
        context['object'] = exception_obj
        return context

def resolved(request, pk):
    if request.method == 'POST':
        print("APPPPPPPPPPPPPPPPPPPPPPPPP", request.POST.get('status'))
        exception_object = ExceptionsHistory.objects.get(id=pk)
        exception_object.status = request.POST.get('status')
        exception_object.save()
    return HttpResponseRedirect('/')
