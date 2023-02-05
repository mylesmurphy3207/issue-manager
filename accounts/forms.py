from django.contrib.auth.forms import UserCreationform, UserChangeForm
from. models import CustomUser


class CustomUserCreationForm(UserCreationform):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.meta.fields + ('role', 'team')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = UserChangeForm.Meta.fields

