from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        gender_value = (('1', '女性',),('2', '男性',),('0', 'その他',))
        weekday_value = (('-', '--',),('0', '日',),('1', '月',),('2', '火',),('3', '水',),('4', '木',),('5', '金',),('6', '土',))
        model = Member
        fields = ('loginid','nick_name','mail_address','password','gender',\
                  'area1','area2','area3','junle1','junle2','junle3',\
                  'weekday1','weekday2','weekday3','time_from1','time_from2','time_from3','time_to1','time_to2','time_to3')
        widgets = {
            #'gender': forms.RadioSelect(choices=gender_value),
            'gender': forms.RadioSelect(choices=gender_value),
            'weekday1': forms.Select(choices=weekday_value),
            'weekday2': forms.Select(choices=weekday_value),
            'weekday3': forms.Select(choices=weekday_value),
            'time_from1':forms.TimeInput(attrs={'class':'timeClass',}),
            'time_from2':forms.TimeInput(attrs={'class':'timeClass',}),
            'time_from3':forms.TimeInput(attrs={'class':'timeClass',}),
            'time_to1':forms.TimeInput(attrs={'class':'timeClass',}),
            'time_to2':forms.TimeInput(attrs={'class':'timeClass',}),
            'time_to3':forms.TimeInput(attrs={'class':'timeClass',}),
        }