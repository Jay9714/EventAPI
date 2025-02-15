import io
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model
from rest_framework import generics
from event_api.serializer import RegisterSerializer, EventSerializer, TicketSerializer
from .models import Event
from datetime import datetime
from django.shortcuts import get_object_or_404
# Create your views here.

User = get_user_model()

"""
This API is used to register or create new user
"""
class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


"""
This API is used to handle both request post and get.
This API is used to create new event and also fetching all the event
"""
class EventView(APIView):
    # Apply JWT authentication and require the user to be authenticated
    authentication_classes = [JWTAuthentication] 
    permission_classes = [IsAuthenticated]

    def post(self, *args, **kwargs):
        try:
            if self.request.user.user_role != 'Admin':
                return Response({"msg": "You do not have permission to perform this action."})
            data = io.BytesIO(self.request.body)
            data = JSONParser().parse(data)
            try:
                data["date"] = datetime.strptime(data["date"], "%d-%m-%Y").date()
            except ValueError:
                    return Response({"msg": "Invalid date format. Please use 'DD-MM-YYYY'."}, status=status.HTTP_400_BAD_REQUEST)
            serializer = EventSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Event has been created."}, status=status.HTTP_201_CREATED)
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"msg": f"Something went wrong!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, *args, **kwargs):
        try:
            events = Event.objects.all()
            serializer = EventSerializer(events, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"msg": f"Something went wrong!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


"""
This API handle post request.
This API is used to book the ticket for the event.
"""
class TicketView(APIView):
    # Apply JWT authentication and require the user to be authenticated
    authentication_classes = [JWTAuthentication] 
    permission_classes = [IsAuthenticated]

    def post(self, *args, **kwargs):
        """
        Handles ticket booking for an event.

        - Only users with the 'User' role can purchase tickets.
        - Ensures the event ID is valid and exists in the database.
        - Validates the requested ticket quantity with sold ticket.
        - Saves the ticket booking and updates the event model tickets_sold count.
        """
        try:
            if self.request.user.user_role != 'User':
                return Response({"msg": "You do not have permission to perform this action."})

            event_id = kwargs.get("event_id", None)

            if not event_id:
                return Response({"msg": "Something went wrong!"}, status=status.HTTP_400_BAD_REQUEST)
            
            events = get_object_or_404(Event, id=event_id)
            data = io.BytesIO(self.request.body)
            data = JSONParser().parse(data)
            
            qty = data.get("quantity", None)
            if not qty or not isinstance(qty, int) or qty == 0:
                return Response({"msg": "Please enter valid quantity."}, status=status.HTTP_400_BAD_REQUEST)
            
            # Check if requested tickets is not more than the available tickets
            if events.tickets_sold + qty > events.total_tickets:
                return Response({"msg": "You are trying to purchase more tickets than are available."}, status=status.HTTP_400_BAD_REQUEST)
            
            data = {
                "user": self.request.user.id,
                "event": int(event_id),
                "quantity": int(qty)
            }
            serializer = TicketSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                events.tickets_sold += qty
                events.save()
                return Response({"msg": "Tickets has been booked."}, status=status.HTTP_200_OK)
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"msg": f"Something went wrong!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)