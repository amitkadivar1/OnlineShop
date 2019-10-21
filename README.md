demo like below mentiond site, 

amitkadivar.xyz


media file usefull links when 
DEBUG=False

https://stackoverflow.com/questions/44555187/django-media-files-not-showing-with-debug-false-on-production-django-1-10


how to connect django with dropbox 
install  
pip3 install dropbox django-storages
[create app](https://www.dropbox.com/developers/apps)
[FileStorege](https://stackoverflow.com/questions/17386741/how-to-use-dropbox-as-django-media-files-storage)

```
INSTALLED_APPS += ( 'storages', )

DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'

DROPBOX_OAUTH2_TOKEN='DropBox-access-key'
DROPBOX_ROOT_PATH='nameofyourapp'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')
```
[FieldMoreDetail](https://stackoverflow.com/questions/49715802/how-to-use-django-storages-for-media-storage-on-dropbox)


# models.py

```file = models.FileField(upload_to=some_path)

replace FileField to ImageField or any other field
```
# urls.py 
```urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

# Send mail using Gmail
use this [blog](https://medium.com/@_christopher/how-to-send-emails-with-python-django-through-google-smtp-server-for-free-22ea6ea0fb8e) for put settings

follow [this](https://www.codingforentrepreneurs.com/blog/use-gmail-for-email-in-django/) link for send mail if you got error in live 

# hosting and add custome domain in hroku
follow this [link](https://gist.github.com/mikestone14/11198630) to add custome domain 

heroku domains:add www.yourdomainname.com

add cname in godaddy 
Add
cname and put 
type :- cNAME
Host :-www
points to:- yourherokuapp.herokuapp.com

and type in cmd
host www.yourdomainname.com or any other doamin name

it's work for me 
more detail [here](https://devcenter.heroku.com/articles/custom-domains)


