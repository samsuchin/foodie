from django.contrib.auth.base_user import BaseUserManager


# Custom user manager
class CustomUserManager(BaseUserManager):

    # When a user is created. Fetch the username and set password. Save it
    def create_user(self, username, password, **extra_fields):

        if not username:
            raise ValueError('The username must be set')
        username = self.model.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    # When a superuser is created, create user and set permissions to True
    def create_superuser(self, username, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(username, password, **extra_fields)

