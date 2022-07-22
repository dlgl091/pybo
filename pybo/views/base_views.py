from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count
import logging

from ..models import Question

logger = logging.getLogger('pybo')
def index(request):
    logger.info("INFO 레벨로 출력")
    """
    pybo 목록 출력
    """
    # 입력 인자
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw','') # 검색어
    so = request.GET.get('so', 'recent') # 정렬 기준

    # 정렬
    if so == 'recommend':
        question_list = Question.objects.annotate(
            num_voter=Count('voter')).order_by('-num_voter', '-create_date') # -는 역순이라는 의미
    elif so == 'popular':
        question_list = Question.objects.annotate(
            num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else: # recent
        question_list = Question.objects.order_by('-create_date')

    # 조회
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) | # 제목 검색
            Q(content__icontains=kw) | # 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw) # 답변 글쓴이 검색
        ).distinct()
    # 페이징 처리
    paginator = Paginator(question_list, 10)
    # question_list를 페이징 객체 paginator로 변환. 10은 페이지당 보여줄 게시물 개수
    page_obj = paginator.get_page(page)
    context = {'question_list' : page_obj, 'page':page, 'kw':kw, 'so':so} # 검색 기능을 위해 page와 kw 추가됨
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id) # pk에 해당하는 건이 없으면 오류 대신 404 페이지 반환
    context = {'question' : question}
    return render(request, 'pybo/question_detail.html', context)



