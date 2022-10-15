from jee_mains.models import jee_mains
import random
from rest_framework.views import APIView
from rest_framework.response import Response
import numpy as np

class CreateTestSeries(APIView):
	def get(self, request, *args, **kwargs):
		physics_questions = list(jee_mains.objects.filter(subject='P').exclude(id__in=[10000,20000,30000,40000]).exclude(id__gt=900).values_list('id', flat=True))
		chemistry_questions = list(jee_mains.objects.filter(subject='C').exclude(id__in=[10000,20000,30000,40000]).exclude(id__gt=900).values_list('id', flat=True))
		maths_questions = list(jee_mains.objects.filter(subject='M').exclude(id__in=[10000,20000,30000,40000]).exclude(id__gt=900).values_list('id', flat=True))

		random.shuffle(physics_questions)
		random.shuffle(chemistry_questions)
		random.shuffle(maths_questions)

		splitted_physics_questions = np.array_split(physics_questions, 11)
		splitted_chemistry_questions = np.array_split(chemistry_questions, 11)
		splitted_maths_questions = np.array_split(maths_questions, 11)

		# print("splitted_physics_questions >> ",splitted_physics_questions)
		# print("splitted_chemistry_questions >> ",splitted_chemistry_questions)
		# print("splitted_maths_questions >> ",splitted_maths_questions)
		for splitted_questions_set in splitted_physics_questions:
			TestSeriesMap.objects.create()
		for splitted_questions_set in splitted_chemistry_questions:
			TestSeriesMap.objects.create()
		for splitted_questions_set in splitted_maths_questions:
			TestSeriesMap.objects.create()

		return Response({"splitted_physics_questions": splitted_physics_questions, "splitted_chemistry_questions": splitted_chemistry_questions,
						"splitted_maths_questions": splitted_maths_questions
					 })


