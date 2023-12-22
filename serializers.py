from rest_framework import serializers
import Usermodule
from Usermodule_app.models import  shortenedURl


class Userserializers(serializers.ModelSerializer):
    class Meta:
        model =Usermodule
        fields=['id','first_name','last_name','email,password']
        extra_kwargs={'password':{'write only':True}}
class shortURLSerializer(serializers.ModelSerializer):
    class Meta:
        model =shortenedURl
        fields=['id','orginal_urls','short_url','user']
        
