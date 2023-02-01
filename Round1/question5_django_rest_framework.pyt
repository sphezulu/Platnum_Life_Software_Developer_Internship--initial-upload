from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_params(name, surname):
    """
    Fetches  data using an api view and displays the results
    """
    #stores the data from the api view
    content = {
        "name": name,
        "surname": surname
    }
    return Response(content, status=status.HTTP_200_OK)