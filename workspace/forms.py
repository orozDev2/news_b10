from django import forms

from news.models import News


class NewsForm(forms.ModelForm):
    # content = forms.CharField(label='контент', validators=[min_max_length], widget=forms.Textarea(
    #     attrs={'class': 'form-control', 'placeholder': 'Контент', 'rows': 7}))

    class Meta:
        model = News
        # fields = (
        #     'name',
        #     'image',
        #     'description',
        #     'content',
        #     'author',
        #     'category',
        #     'tags',
        #     'is_published',
        # )

        # fields = '__all__'

        exclude = ('views', 'author')

        # labels = {
        #     'name': 'dsf dsf sdfsd'
        # }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание', 'rows': 7}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Контент', 'rows': 7}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'tags': forms.CheckboxSelectMultiple(),
        }

# class NewsForm(forms.Form):
#
#     CREATE = 'creation'
#     UPDATE = 'updating'
#
#     def __init__(self, action=CREATE, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#         self.action = action
#
#         if action == self.UPDATE:
#             self.fields['image'].required = False
#
#     name = forms.CharField(label='Название', max_length=100, widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Название'}))
#
#     image = forms.ImageField(label='Изображение', widget=forms.FileInput(attrs={
#         'class': 'form-control', 'accept': 'image/*'
#     }))
#
#     description = forms.CharField(label='Описание', max_length=300, widget=forms.Textarea(attrs={
#         'class': 'form-control', 'placeholder': 'Описание', 'rows': 7
#     }))
#
#     content = forms.CharField(label='Контент', widget=forms.Textarea(attrs={
#         'class': 'form-control', 'placeholder': 'Контент', 'rows': 7
#     }))
#
#     author = forms.CharField(label='Автор', max_length=100, widget=forms.TextInput(attrs={
#         'class': 'form-control', 'placeholder': 'Автор'
#     }))
#
#     category = forms.ModelChoiceField(label='Категория', queryset=Category.objects.all(), widget=forms.Select(attrs={
#         'class': 'form-select'
#     }))
#
#     tags = forms.ModelMultipleChoiceField(
#         label='Теги', queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple())
#
#     is_published = forms.BooleanField(label='Публичный', required=False)
#
#
# class UpdateNewsForm(forms.Form):
#     name = forms.CharField(label='Название', max_length=100, widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Название'}))
#
#     image = forms.ImageField(label='Изображение', required=False, widget=forms.FileInput(attrs={
#         'class': 'form-control', 'accept': 'image/*'
#     }))
#
#     description = forms.CharField(label='Описание', max_length=300, widget=forms.Textarea(attrs={
#         'class': 'form-control', 'placeholder': 'Описание', 'rows': 7
#     }))
#
#     content = forms.CharField(label='Контент', widget=forms.Textarea(attrs={
#         'class': 'form-control', 'placeholder': 'Контент', 'rows': 7
#     }))
#
#     author = forms.CharField(label='Автор', max_length=100, widget=forms.TextInput(attrs={
#         'class': 'form-control', 'placeholder': 'Автор'
#     }))
#
#     category = forms.ModelChoiceField(label='Категория', queryset=Category.objects.all(), widget=forms.Select(attrs={
#         'class': 'form-select'
#     }))
#
#     tags = forms.ModelMultipleChoiceField(
#         label='Теги', queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple())
#
#     is_published = forms.BooleanField(label='Публичный', required=False)
