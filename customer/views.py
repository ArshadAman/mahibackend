from django.contrib.auth.models import User
from .models import Customer, Address, Cart, CartItem, Wishlist
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, api_view
from .serializers import CustomerSerializer, UpdateProfileSerializer, AddressSerializer

# Create your views here.

@api_view(["POST"])
def signup(request):
    if request.method == "POST":
        username = request.data.get('username'),
        email = request.data.get('email'),
        first_name = request.data.get('first_name'),
        last_name = request.data.get('last_name'),
        phone_number = request.data.get('phone_number'),
        password = request.data.get('password'),
        
        # Create User
        
        if User.objects.filter(username = username).first():
            return Response({"message": "Username already exists"}, status=status.HTTP_406_NOT_ACCEPTABLE)
        elif User.objects.filter(email = email).first():
            return Response({"message": "email already exists"}, status=status.HTTP_406_NOT_ACCEPTABLE)
        
        new_user = User.objects.create(
            username = username,
            email = email,
            first_name = first_name,
            last_name = last_name,
            phone_number = phone_number,
            password = password
        )
        new_user.save() #User created
        
        # Create Customer account
        if Customer.objects.filter(user = new_user).first():
            return Response({"message": "User already exists"}, status=status.HTTP_406_NOT_ACCEPTABLE)
        new_customer = Customer.objects.create(
            user = new_user,
            phone_number = phone_number
        )
        new_customer.save()
        
        return Response({"message": "successfully sigined up"}, status=status.HTTP_201_CREATED)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_profile(request):
    user = request.user
    if user:
        try:
            customer = Customer.objects.filter(user = user).first()
            serialized_data = CustomerSerializer(customer).data
            return Response(serialized_data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response({"message": str(error)}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_profile(request):
    customer = request.user.customer  # Assuming each user has a corresponding customer profile

    serializer = UpdateProfileSerializer(customer, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def add_address(request):
    customer = request.user.customer
    

def update_address(request):
    pass

def view_all_addresses(request):
    pass

def add_to_cart(request):
    pass

def increase_cart_count(request):
    pass

def decrease_cart_count(request):
    pass

def add_to_wishlist(request):
    pass

def remove_from_wishlist(request):
    pass

def buy_from_cart(request):
    pass

def buy_individual(request):
    pass

def cancel_order(request):
    pass

def return_order(request):
    pass


def change_password(request):
    pass

def forgot_password(request):
    pass
