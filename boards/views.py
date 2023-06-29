# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Board
# from reviews.models import Review

# def show_board(request):
#     return HttpResponse("show board")


# def all_board(request):
#     boards = Board.objects.all()

#     return HttpResponse("All board")

# def make_board(request, board_id, board_content):

#     return HttpResponse(f"Make board / id: {board_id} / content: {board_content}")

# # rendering
# def show_all_board(request):
#     boards = Board.objects.all()
#     return render(request, "all_boards.html", {"datas": boards, "status": "success"})


# # rendering
# def show_board_reviews(request):
#     reviews = Review.objects.all()
#     return render(request, "reviews.html", {"datas": reviews, "status":"success" })


################################분리######################################
# views.py
# 클라이언트(대개 react)에서 보낸 데이터를 받아서 처리해주는 부분
# http method
from rest_framework.views import APIView
from rest_framework.response import Response  # 클라이언트로 데이터를 내려주는 부분
from rest_framework.exceptions import NotFound   # 데이터가 찾지 못한 경우 내려주는 거
from .models import Board
from .serializers import BoardSerializer

# GET:전체 게시글 불러오기
class Boards(APIView):
    def get(self,request):

        boards = Board.objects.all()  # 장고의 객체

        # 장고의 객체를 바로 react로 바꾸면 못 알아먹음.
        # 장고 객체 -> JSON(리액트 객체, Serializer로 변환)
        serializer = BoardSerializer(boards, many=True)

        return Response(serializer.data)   
    


# GET: 유저로부터 입력바든 id 값의 게시글 데이터 불러오기
class BoardDetail(APIView):
    def get(self, request, board_id):
        # request: react에서 데이터를 담아서 보내준 부분
        # board_id: URL을 통해서 데이터를 전달받는 부분
        try:
            board = Board.objects.get(id=board_id)   # board 변수는 장고 객체 -> JSON으로 변환(serializer)
        except Board.DoesNotExist:
            raise "Not Found"

        serializer = BoardSerializer(board)
        print(serializer)

        return Response(serializer.data)


