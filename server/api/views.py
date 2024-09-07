from rest_framework import viewsets
from django.shortcuts import render
from .models import *
from .serializers import *
from .permissions import *
from django.contrib.admin.views.decorators import staff_member_required
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsAdminOrReadOnly]

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

    def create(self, request, *args, **kwargs):
            if isinstance(request.data, list):
                serializer = self.get_serializer(data=request.data, many=True)
            else:
                serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    permission_classes = [AllowPostOnly]

    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [AllowPostOnly]

    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class BookingCheckViewSet(viewsets.ModelViewSet):
    queryset = BookingCheck.objects.all()
    serializer_class = BookingCheckSerializer
    permission_classes = [AllowPostOnly]

@staff_member_required
def show_filter_form(request):
    if request.method == 'POST':
        checkInDate = request.POST.get('checkInDate')
        checkOutDate = request.POST.get('checkOutDate')
        category = request.POST.get('category')
        isConfirmed = request.POST.get('isConfirmed')
        isPaid = request.POST.get('isPaid')
        isCancelled = request.POST.get('isCancelled')
        isRefund = request.POST.get('isRefund')

        filters = Q(checkInDate__lte=checkOutDate) & Q(checkOutDate__gte=checkInDate)
        
        if category != 'any':
            filters &= Q(category__categoryType__iexact=category)
        if isConfirmed.lower() != 'any':
            filters &= Q(isConfirmed=isConfirmed.lower() == 'true')
        if isPaid.lower() != 'any':
            filters &= Q(isPaid=isPaid.lower() == 'true')
        if isCancelled.lower() != 'any':
            filters &= Q(isCancelled=isCancelled.lower() == 'true')
        if isRefund.lower() != 'any':
            filters &= Q(isRefund=isRefund.lower() == 'true')

        filtered_bookings = Booking.objects.filter(filters)
        return render(request, 'filterResult.html', {'result': filtered_bookings} )

    return render(request, 'filterForm.html')