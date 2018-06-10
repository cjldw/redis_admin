# _*_ encode:utf-8 _*_

from django import forms


# from users.models import RedisConf

class RedisForm(forms.ModelForm):
    name = forms.CharField(max_length=10, verbose_name=u"名称")
    host = forms.CharField(max_length=15, verbose_name=u"IP地址")
    port = forms.IntegerField(default=6379, verbose_name=u"端口")
    password = forms.CharField(null=True, blank=True, max_length=30, verbose_name=u"密码")
    database = forms.IntegerField(default=16, verbose_name=u"db数")
    # class Meta:
    #     model = RedisConf
    #     fields = '__all__'
