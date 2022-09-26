from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Brands(models.Model):
    brand_id = models.AutoField(unique=True, db_column='brand_id', primary_key=True)
    brand_name = models.CharField(max_length=70, blank=True, null=True)
    brand_image = models.CharField(max_length=700, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'brands'


class CarImage(models.Model):
    car_image_id = models.AutoField(unique=True, db_column='car_image_id', primary_key=True)
    version = models.ForeignKey('Version', on_delete=models.CASCADE, blank=True, null=True)
    car_image_1 = models.CharField(max_length=700, blank=True, null=True)
    car_image_2 = models.CharField(max_length=700, blank=True, null=True)
    car_image_3 = models.CharField(max_length=700, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'car_image'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Model(models.Model):
    model_id = models.AutoField(unique=True, db_column='model_id',primary_key=True)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE, blank=True, null=True)
    segment = models.ForeignKey('Segment', on_delete=models.CASCADE, blank=True, null=True)
    model_name = models.CharField(max_length=70, blank=True, null=True)
    model_image = models.CharField(max_length=700, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'model'


class Segment(models.Model):
    segment_id = models.AutoField(unique=True, db_column='segmnet_id', primary_key=True)
    segment_name = models.CharField(max_length=70, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'segment'


class Version(models.Model):
    version_id = models.AutoField(unique=True, db_column='version_id', primary_key=True)
    model = models.ForeignKey(Model, models.DO_NOTHING, blank=True, null=True)
    version_name = models.CharField(max_length=70, blank=True, null=True)
    year = models.TextField(blank=True, null=True)  # This field type is a guess.
    power_hp = models.IntegerField(blank=True, null=True)
    torque = models.IntegerField(blank=True, null=True)
    traction = models.CharField(max_length=70, blank=True, null=True)
    automatic = models.IntegerField(blank=True, null=True)
    good_capacity = models.IntegerField(blank=True, null=True)
    autonomy = models.IntegerField(blank=True, null=True)
    low_gas_use = models.IntegerField(blank=True, null=True)
    screen = models.IntegerField(blank=True, null=True)
    fiability = models.IntegerField(blank=True, null=True)
    interior_space = models.CharField(max_length=70, blank=True, null=True)
    spacious = models.IntegerField(blank=True, null=True)
    interiors = models.CharField(max_length=60, blank=True, null=True)
    secure = models.IntegerField(blank=True, null=True)
    passengers = models.IntegerField(blank=True, null=True)
    is_comfortable = models.IntegerField(blank=True, null=True)
    sunroof = models.IntegerField(blank=True, null=True)
    is_functional = models.IntegerField(blank=True, null=True)
    stetic = models.IntegerField(blank=True, null=True)
    attractive = models.IntegerField(blank=True, null=True)
    rims = models.CharField(max_length=70, blank=True, null=True)
    color_hexa = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'version'