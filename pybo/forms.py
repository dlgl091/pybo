from django import forms
from pybo.models import Question, Answer, Comment, Document

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']

        labels = {
            'subject' : '제목',
            'content' : '내용'
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content' : '답변내용'
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {'content':'댓글내용'}

class DocumentForm(forms.ModelForm):
    upload = forms.FileField(label='첨부 파일', required=False,
                             widget=forms.FileInput(attrs={'class':'form'}))
    class Meta:
        model = Document
        exclude = ['attached']
