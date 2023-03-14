from rest_framework.views import APIView
from rest_framework.response import Response
from .main import get_anime_url, get_anime_list
from rest_framework import status

# Create your views here.
class AnimeEpisodeView(APIView):
    def get(self, request):
        anime_name = request.query_params.get('anime_name')
        episode_number = request.query_params.get('episode_number')
        if not anime_name:
            # return error response if anime_name is missing
            return Response({'error': 'anime_name is required'}, status=status.HTTP_400_BAD_REQUEST)

        print("Checking",anime_name)
        print(episode_number)
        if episode_number:

            if int(episode_number) < 0:
                episode_list = get_anime_list(anime_name)
                if len(episode_list):
                    episode_number = episode_list[-1]
            url = get_anime_url(anime_name, episode_number)
            return Response({'anime_name': anime_name, 'episode_number': episode_number, 'data':url})
        else:
            urls = get_anime_list(anime_name)
            return Response({'anime_name': anime_name, 'data':urls})
