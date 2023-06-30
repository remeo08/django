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
from rest_framework.exceptions import NotAuthenticated
from rest_framework.status import HTTP_204_NO_CONTENT


# GET:전체 게시글 불러오기
# POST: 게시글 작성하기(create)
class Boards(APIView):
    def get(self,request):

        boards = Board.objects.all()  # 장고의 객체

        # 장고의 객체를 바로 react로 바꾸면 못 알아먹음.
        # 장고 객체 -> JSON(리액트 객체, Serializer로 변환)
        serializer = BoardSerializer(boards, many=True)

        return Response(serializer.data)   
    


    def post(self, request):
        # 장고 객체 -> JSON
        # 리액트가 보내주는 데이터: JSON -> 장곡객체(역직렬화)
        if request.user.is_authenticated:
            serializer = BoardSerializer(data=request.data)  # JSON을 objects(객체)로

            if serializer.is_valid():
                board = serializer.save(users=request.user)   # 데이터 저장
                serializer = BoardSerializer(board)   # 직렬화(Objects -> JSON)

                return Response(serializer.data)
        
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated


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
    


    def put(self, request, board_id):
        board = Board.objects.get(id = board_id)

        if request.user != board.users:
            raise PermissionError
        
        serializer = BoardSerializer(
            board,
            data=request.data,
            context={"request":request},
            partial=True
        )

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)



    
    def delete(self, request, board_id):
        board = Board.objects.get(id=board_id)

        # if request.user.is_authenticated:
        #     raise NotAuthenticated
        
        if request.user != board.users:   # 로그인한 유저랑 글을 작성한 유저가 다르면
            raise PermissionError
        
        board.delete()

        return Response(status=HTTP_204_NO_CONTENT)

        # 지운다.
        # 본인이 작성한 게시글만 지울 수 있다.
        # 로그인 하지 않은 사용자도 해당 api도 사용할 수 없다.




# api

