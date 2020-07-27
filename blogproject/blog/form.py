from django import forms
from .models import Blog

class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'image', 'body']

        #기존에는 title, image, body로 필드 이름이 표시됐는데 라벨을 붙여서 좀 더 알아보기 쉽게함
        labels = {
            'title': '제목',
            'image': '이미지',
            'body': '내용'
        } 
