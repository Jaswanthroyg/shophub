from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from .models import Payment
from .serializers import PaymentSerializer
from .models import Order
import razorpay
from django.conf import settings


Client=razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,
                             settings.RAZORPAY_KEY_SECRET
                             ))
