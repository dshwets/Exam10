from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Profile


class FriendsApi(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        profile_which_will_be_added = get_object_or_404(Profile, pk=kwargs.get('pk'))
        profile = self.request.user.profile
        if profile == profile_which_will_be_added:
            return Response({"message": "Нельзя добавить себя в друзья"}, status=400)
        else:
            # slr = ProfileSerializer(profile_which_will_be_added)
            profile.friends.add(profile_which_will_be_added)
            return Response({"message": "Друг был доавлен"}, status=200)
