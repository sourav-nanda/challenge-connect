
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Hackathon, Submission
from .serializers import HackathonSerializer, SubmissionSerializer, UserSerializer
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated



@api_view(['GET'])
def hackathon_feed(request):
    hackathons = Hackathon.get_all_hackathons()
    serializer = HackathonSerializer(hackathons, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def hackathon_create(request):
    if not request.user.is_staff:  # staff are superusers/admins
        return Response({'message': 'You are not authorized to create hackathons.'}, status=status.HTTP_403_FORBIDDEN)

    serializer = HackathonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def hackathon_enroll(request, hackathon_id):
    try:
        hackathon = Hackathon.objects.get(pk=hackathon_id)
        user = request.user
        # Check if the user is already enrolled in the hackathon
        if hackathon.submissions.filter(user=user).exists():
            return Response({'message': 'You are already enrolled in this hackathon.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create an empty submission for the user and enroll in the hackathon
        Submission.objects.create(hackathon=hackathon, user=user)
        return Response({'message': 'Enrollment successful!'}, status=status.HTTP_201_CREATED)
    except Hackathon.DoesNotExist:
        return Response({'message': 'Hackathon not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def hackathon_enrolled(request):
    user = request.user
    enrolled_hackathons = Hackathon.objects.filter(submissions__user=user)
    serializer = HackathonSerializer(enrolled_hackathons, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def submission_create(request, hackathon_id):
    try:
        hackathon = Hackathon.objects.get(pk=hackathon_id)
        user = request.user

        # Check if the user is enrolled in the hackathon before allowing submission
        if not hackathon.enrolled_users.filter(pk=user.pk).exists():
            return Response({'message': 'You are not enrolled in this hackathon.'}, status=status.HTTP_403_FORBIDDEN)

        serializer = SubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(hackathon=hackathon, user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Hackathon.DoesNotExist:
        return Response({'message': 'Hackathon not found'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def submission_user(request, user_id):
    user_submissions = Submission.get_user_submissions(user_id)
    serializer = SubmissionSerializer(user_submissions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def unauthorized(request):
    return Response(status=status.HTTP_403_FORBIDDEN)