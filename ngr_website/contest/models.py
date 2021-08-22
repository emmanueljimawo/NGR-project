from django.core.validators import RegexValidator
from django.db import models
from django.utils.text import slugify
from .model_choices import SEX, STATES_IN_NIGERIA
from .paystack import Paystack
import base64
from io import BytesIO
from PIL import Image

# Create your models here.

class TimeStampModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        abstract = True

class Contest(TimeStampModel):
    title = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    registration_fee_amount = models.IntegerField()
    voting_fee_amount = models.IntegerField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_created']


class Contestant(TimeStampModel):
    _Phone_number_regex = RegexValidator(regex=r'^0\d{1}0\d{8}$', message="Phone number must be 11 digits and entered in the format: '080**'.")

    contest = models.ForeignKey(Contest, related_name='contestant', on_delete=models.CASCADE)
    ref_number = models.CharField(max_length=200)
    payment_verified = models.BooleanField(default=False)
    last_name = models.CharField(max_length=100)
    other_names = models.CharField(max_length=300)
    age = models.IntegerField()
    sex = models.CharField(max_length=10, choices=SEX, default='female')
    facebook = models.URLField(max_length=200, blank=True, null=True)
    instagram = models.URLField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(validators=[_Phone_number_regex], max_length=20)
    email = models.EmailField(max_length=200)
    state = models.CharField(max_length=200, choices=STATES_IN_NIGERIA, default='Lagos')
    photograph = models.ImageField(upload_to="photograph/", blank=False)
    thumbnail=models.ImageField(upload_to='thumbnail/', null=True, blank=True)
    profession = models.CharField(max_length=200)
    about = models.TextField(max_length=1500)
    agree_to_the_terms_and_conditions = models.BooleanField(blank=False)
    agree_to_pay_the_registration_fee = models.BooleanField(blank=False)
    agree_that_the_information_provided_is_accurate = models.BooleanField(blank=False)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return f'{self.last_name} {self.other_names}' 

    def verify_payment(self):
        paystack = Paystack()
        status, result = paystack.verify_payment(self.ref_number, self.contest.registration_fee_amount)
        if status:
            if result['amount'] / 100 == self.contest.registration_fee_amount:
                self.payment_verified = True
            self.save()
        if self.payment_verified:
            return True
        return False
    
    def count_votes(self):
        votes_count = Vote.objects.filter(payment_verified=True, contestant=self).count()
        return votes_count


    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            slug = slugify(f'{self.last_name} {self.other_names}')
            slug_exists = True
            counter = 1
            self.slug = slug
            while slug_exists:
                try:
                    slug_exits = Contestant.objects.get(slug=slug)
                    if slug_exits:
                        slug = self.slug + '-' + str(counter)
                        counter += 1
                except Contestant.DoesNotExist:
                    self.slug = slug
                    break
        if not self.photograph:
            self.thumbnail = None
        else:
            thumbnail_size = 320, 320
            data_img = BytesIO()
            tiny_img = Image.open(self.photograph)
            tiny_img.thumbnail(thumbnail_size)
            tiny_img.save(data_img, format="BMP")
            tiny_img.close()
            try:
                self.thumbnail = "data:image/jpg;base64,{}".format(
                    base64.b64encode(data_img.getvalue()).decode("utf-8")
                )
            except UnicodeDecodeError:
                self.blurred_image = None

        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date_created']

class Vote(TimeStampModel):
    contestant = models.ForeignKey(Contestant, related_name="vote", on_delete=models.CASCADE)
    ref_number = models.CharField(max_length=200)
    payment_verified = models.BooleanField(default=False)

    def verify_payment(self):
        paystack = Paystack()
        status, result = paystack.verify_payment(self.ref_number, self.contestant.contest.voting_fee_amount)
        if status:
            if result['amount'] / 100 == self.contestant.contest.voting_fee_amount:
                self.payment_verified = True
            self.save()
        if self.payment_verified:
            return True
        return False
   

    def __str__(self):
        return f'{self.contestant.last_name} {self.contestant.other_names}'

    class Meta:
        ordering = ['-date_created']
