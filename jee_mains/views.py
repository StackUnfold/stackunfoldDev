from django.shortcuts import render

# Create your views here.
# class SingleQuestionView()

from jee_mains.models import jee_mains, TestSeriesMap
from jee_mains.serializers import JeeSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer


class JeeMainsList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        jee_mains_all_obj = jee_mains.objects.all()
        serializer = JeeSerializer(jee_mains_all_obj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = JeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JeeMainsDetail(APIView):

    """
    Retrieve, update or delete a snippet instance.
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "home/jee-qna-new.html"

    def get_object(self, url):
        try:
            return jee_mains.objects.get(url=url)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, url, format=None):
        jee_mains_obj = self.get_object(url)
        serializer = JeeSerializer(jee_mains_obj)
        return Response(
            {
                "data": serializer.data,
            },
            template_name="home/jee-qna-new.html",
        )

        return Response(serializer.data)

    def put(self, request, url, format=None):
        jee_mains_obj = self.get_object(url)
        serializer = JeeSerializer(jee_mains_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, url, format=None):
        snippet = self.get_object(url)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class RenderTestSeriesQuestion(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "home/jee_test_series.html"

    def get(self, request, test_series_id ,ques_id):
        get_test_series_questions = TestSeriesMap.objects.filter(id=int(test_series_id))
        print("get_test_series_questions ",get_test_series_questions)
        if int(ques_id)<31:
            question_id_jee = list(get_test_series_questions.values('physics_ques_map'))[0]['physics_ques_map'][int(ques_id)]
            print("question_id_jee ",question_id_jee)
            jee_mains_obj = jee_mains.objects.get(id = question_id_jee)
            serializer = JeeSerializer(jee_mains_obj)
            return Response(
                {   "range": range(1,16),
                    "data": serializer.data,
                },
                template_name='home/jee_test_series.html'
            )


