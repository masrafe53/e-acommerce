from app.models import Category


def categorys(request):
    return{"categorys": Category.objects.all()}
