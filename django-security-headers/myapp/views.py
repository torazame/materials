from django.http import HttpResponse


def index(request):
    return HttpResponse(
        """\
<!DOCTYPE html>
<html lang="en-US">
  <head><meta charset="utf-8"><title>My secure app</title></head>
  <body><p>Now this is some sweet HTML!</p></body>
</html>"""
    )
