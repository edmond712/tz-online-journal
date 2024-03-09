from rest_framework import status, viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Recipe
from .serializers import RecipeSerializer

from .permissions import IsAdminOrReadOnly, IsAuthenticatedOrReadOnly, IsGuestOrReadOnly

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    content = {
        'user': str(request.user),
        'auth': str(request.auth),
    }
    return Response(content)

class AdminViewSet(viewsets.ModelViewSet):
    recipes = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_permissions(self):
        if self.request.user.is_authenticated:
            return [IsAdminOrReadOnly()]
        else:
            return [IsGuestOrReadOnly()]


@api_view(['GET'])
def view_recipe(request):

    if request.method == 'GET':
        recipes = Recipe.objects.all()

        serializer = RecipeSerializer(recipes, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def recipe_list(request):

    if request.method == 'GET':
        recipes = Recipe.objects.all()

        serializer = RecipeSerializer(recipes, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def create_recipe(request):

    if request.method == 'GET':
        recipes = Recipe.objects.all()

        serializer = RecipeSerializer(recipes, many=True)

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    if request.method == 'POST':
        serializer = RecipeSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'UPDATE'])
def update_recipe(request, pk):

    if request.method == 'GET':
        recipes = Recipe.objects.all()

        serializer = RecipeSerializer(recipes, many=True)

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    if request.method == 'PATCH':
        recipe = Recipe.objects.get(pk=pk)
        serializer = RecipeSerializer(recipe, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(serializer.data)

@api_view(['GET', 'DELETE'])
def delete_recipe(request, pk):

    if request.method == 'GET':
        recipes = Recipe.objects.all()

        serializer = RecipeSerializer(recipes, many=True)

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    if request.method == 'DELETE':
        recipe = Recipe.objects.get(pk=pk)
        recipe.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
