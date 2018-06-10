# _*_ encode:utf-8 _*_

from django import forms


# from users.models import RedisConf

class RedisForm(forms.ModelForm):
    name = forms.CharField(max_length=10, required=True)
    host = forms.CharField(max_length=15, required=True)
    port = forms.IntegerField(default=6379, required=True)
    password = forms.CharField(null=True, blank=True, max_length=30)
    database = forms.IntegerField(default=16, required=True)
    # class Meta:
    #     model = RedisConf
    #     fields = '__all__'
