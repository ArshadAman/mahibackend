from django.contrib.auth.models import User
from .models import Customer, Address, Cart, CartItem, Wishlist
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, api_view
from .serializers import CustomerSerializer, UpdateProfileSerializer, AddressSerializer, WishlistSerializer
from datetime import datetime
from products.models import Product

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
    user = request.user
    customer = Customer.objects.filter(user = user).first()

    serializer = UpdateProfileSerializer(customer, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_address(request):
    user = request.user
    name = request.data.get('name')
    phone_number = request.data.get('phone_number')
    alternate_phone_number = request.data.get("phone_number")
    city = request.data.get('city')
    area = request.data.get('area')
    pincode = request.data.get('pincode')
    building_name = request.data.get('building_name')
    landmark = request.data.get('landmark')
    address_type = request.data.get('address_type')
    
    if name is None or phone_number is None or alternate_phone_number is None or city is None or area is None or pincode is None or building_name is None or landmark is None or address_type is None:
        return Response({"message": "Please ensure all the fields are filled properly"}, status=status.HTTP_406_NOT_ACCEPTABLE)

    try:
        customer = Customer.objects.filter(user = user).first()
        if customer:
            new_address = Address.objects.create(
                customer = customer,
                name = name,
                phone_number = phone_number,
                alternate_phone_number = alternate_phone_number,
                city = city,
                area = area,
                pincode = pincode,
                building_name = building_name,
                landmark = landmark,
                address_type = address_type
            )
            new_address.save()
            return Response({"message": "Address saved"}, status=status.HTTP_201_CREATED)
        return Response({"message": "No such account found"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response({"message": str(error)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def view_all_addresses(request):
    user = request.user
    try:
        customer = Customer.objects.filter(user = user).first()
        addresses = Address.objects.filter(customer = customer)
        serialized_data = AddressSerializer(addresses, many = True).data
        return Response(serialized_data, status=status.HTTP_200_OK)
    except Exception as error:
        return Response({"message": str(error)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
@permission_classes[IsAuthenticated]
def update_address(request, pk):
    user = request.user
    try:
        address = Address.objects.get(id = pk)
        if user == address.customer.user:
            serializer = AddressSerializer(address, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Sorry you are not allowed to change someone else address'}, status=400)
    except Exception as error:
        return Response({'message': str(error)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_wishlist(request, product_id):
    user = request.user
    customer = Customer.objects.filter(user = user).first()
    product = Product.objects.get(id = product_id)
    try:
        wishlist = Wishlist.objects.create(
            customer = customer,
            product = product,
            date_added = datetime.now()
        )
        wishlist.save()
        return Response({'message': 'added to wishlist'}, status=status.HTTP_201_CREATED)
    except Exception as error:
        return Response({'message': str(error)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_wishlist(request):
    user = request.user
    customer = Customer.objects.filter(user = user).first()
    try:
        wishlist_items = Wishlist.objects.filter(customer = customer)
        serializer = WishlistSerializer(wishlist_items, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as error:
        return Response({'message': str(error)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])    
def remove_from_wishlist(request, pk):
    user = request.user
    customer = Customer.objects.filter(user = user)
    try:
        if(user == customer.user):
            wishlist_item = Wishlist.objects.get(id = pk)
            wishlist_item.delete()
            return Response({"message": "item removed from the wishlist"}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Sorry you are not allowed to change someone else wishlist'}, status=400)
    except Exception as error:
        return Response({'message': str(error)}, status=status.HTTP_400_BAD_REQUEST)    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request, product_id):
    customer = Customer.objects.filter(user = request.user).first()
    product = Product.objects.get(id = product_id)
    cart = Cart.objects.get_or_create(customer = customer)
    # we have initialized a cart for the user
    cartItem = CartItem.objects.create(
        cart = cart,
        product = product,
        quantity = 1,
        additional_price = 0,
    )
    cartItem.save()
    return Response({"message": "Item added to the cart"}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def increase_cart_count(request, product_id):
    user = request.user
    customer = Customer.objects.filter(user = user).first()
    product = Product.objects.get(id = product_id)
    cart = Cart.objects.filter(customer = customer).first()
    if customer != cart.customer:
        return Response({"message": "You are not allowed to change someones cart"}, status=status.HTTP_401_UNAUTHORIZED)
    cartItem = CartItem.objects.filter(product = product).first()
    if cartItem.quantity < product.quantity:
        cartItem.quantity += 1
        cartItem.save()
        return Response({"message": "quantity increased"}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Cart Quantity cannot exceeds the product quantity"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def decrease_cart_count(request, product_id):
    user = request.user
    customer = Customer.objects.filter(user = user).first()
    product = Product.objects.get(id = product_id)
    cart = Cart.objects.filter(customer = customer).first()
    if customer != cart.customer:
        return Response({"message": "You are not allowed to change someones cart"}, status=status.HTTP_401_UNAUTHORIZED)
    cartItem = CartItem.objects.filter(product = product).first()
    if cartItem.quantity > 1:
        cartItem.quantity -= 1
        cartItem.save()
        return Response({"message": "quantity decreased"}, status=status.HTTP_200_OK)
    elif cartItem.quantity == 0:
        cartItem.delete()
        cartItem.save()
        return Response({"message": "item removed"}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Cart Quantity cannot exceeds the product quantity"})

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def buy_from_cart(request):
    pass

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def buy_individual(request):
    pass

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def cancel_order(request):
    pass

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def return_order(request):
    pass

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def change_password(request):
    pass

@api_view(["POST"])
def forgot_password(request):
    pass
