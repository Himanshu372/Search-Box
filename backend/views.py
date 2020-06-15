from rest_framework import viewsets
from rest_framework.response import Response

from backend.models import Reviews

class HomeView(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()

    def create(self, request, *args, **kwargs):
        keyword = request.POST['keyword']
        result_set = self.queryset.filter(text__icontains=keyword).order_by('-prod_score', '-prod_helpfulness')
        result = [{'text': each.text, 'score': each.prod_score, 'helpfulness': each.prod_helpfulness}
                  for each in result_set]
        return Response(result)
