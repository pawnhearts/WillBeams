from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from webm.models import Webm, Tag

class LastWebmsView(ListView):
    model = Webm
    template_name = 'webm/webm_list.html'
    ordering = ['-added']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(LastWebmsView, self).get_context_data(**kwargs)
        context['top_tags'] = Tag.get_top_tags()
        return context

class LastWebmsByTagView(LastWebmsView):
    model = Webm
    template_name = 'webm/webm_list.html'
    paginate_by = 10

    def get_queryset(self):
        tag = get_object_or_404(Tag, name=self.args[0])
        print(tag)
        return tag.webm_set.all()

