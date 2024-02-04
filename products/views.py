from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAdminUser
from .models import Category, Product, Brand
from .serializers import CategorySerializer, ProductSerializer, AttributeSerializer, BrandSerializer
from .filter import ProductFilter


@api_view(["POST"])
@permission_classes([IsAdminUser])
def add_category(request):
    name = request.data.get('category_name')
    banner = request.data.get('category_banner')
    icon = request.data.get('category_icon')

    try:
        new_category = Category.objects.create(
            name = name,
            banner = banner,
            icon = icon
        )
        new_category.save()
        return Response({'message': 'category saved'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_category(request, pk):
    try:
        category_to_be_deleted = Category.objects.get(id = pk)
        category_to_be_deleted.delete()
        return Response({"message": "Category Deleted"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'messsage': str(e)})
    
@api_view(['GET'])
def all_category(request):
    try:
        all_categories = Category.objects.all()
        serialized_data = CategorySerializer(all_categories, many=True).data
        return Response({"message": serialized_data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'messsage': str(e)})
    
@api_view(['GET'])
def all_brands(request):
    try:
        brands = Brand.objects.all()
        serialized_data = BrandSerializer(brands, many=True).data
        return Response({"message": serialized_data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'messsage': str(e)})
    
    
    
class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter