from django import forms
from .models import Board, Column, Card, Comment


from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'



class BoardForm(forms.ModelForm):
	class Meta:
		model = Board
		fields = [
			"title",
			"image",
		]

class ColumnForm(forms.ModelForm):
	class Meta:
		model = Column
		fields = '__all__'

		# fields = [
		# 	"title",
		# ]


class CardForm(forms.ModelForm):
	class Meta:
		model = Card
		fields = '__all__'
