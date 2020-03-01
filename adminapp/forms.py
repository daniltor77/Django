from django.forms import ModelForm
from authnapp.forms import ShopUserEditForm
from authnapp.models import ShopUser
from mainapp.models import Product, ProductCategory

class ShopUserAdminEditForm(ShopUserEditForm):
    class Meta:
        model=ShopUser
        fields="__all__"


class ProductCategoryEditForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"]="form-control"
            field.help_text=""

    class Meta:
        model=ProductCategory
        fields="__all__"

class ProductEditForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"]="form-control"
            field.help_text=""
    
    class Meta:
        model=Product
        fields="__all__"