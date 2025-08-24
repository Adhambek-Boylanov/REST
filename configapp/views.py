from rest_framework.views import APIView
import json
from rest_framework.response import Response
class Hello(APIView):
    def get(self,request):
        with open('student.json','r') as f:
            data= json.load(f)
        return Response(data= data)

    def post(self, request):
        name = request.data['name',"nomer"]
        context = {
            "response":f"salom {name}"
        }
        return Response(data=context)


