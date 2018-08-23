from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        gender_value = (('1', '女性',),('2', '男性',),('0', 'その他',))
        model = Member
        fields = ('loginid','nick_name','mail_address','password','gender','area','junle','time_range')
        widgets = {
            #'gender': forms.RadioSelect(choices=gender_value),
            'gender': forms.RadioSelect(choices=gender_value),
        }