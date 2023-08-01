# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

AGE_RANGE_CHOICES = [
    ('below 18', 'Below 18'),
    ('18 to 24', '18 to 24'),
    ('25 to 34', '25 to 34'),
    ('35 to 44', '35 to 44'),
    ('45 to 54', '45 to 54'),
    ('55 to 64', '55 to 64'),
    ('65 or over', '65 or over'),
]

GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
]


class QoeVideo(models.Model):
    video_id = models.AutoField(primary_key=True)
    video_name = models.CharField(max_length=45)
    packet_loss_value = models.FloatField()
    rtt_value = models.FloatField()
    network = models.CharField(max_length=45)
    video_file_path = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'qoe_video'

    def __str__(self):
        return str(self.video_id)


class QoeRating(models.Model):
    qoe_rating_id = models.AutoField(
        primary_key=True)  # The composite primary key (qoe_rating_id, video_id, respondent_id) found, that is not supported. The first column is selected.
    qoe_rating_value = models.IntegerField()
    qoe_rating_perception = models.CharField(max_length=300)
    validation_video_path = models.CharField(max_length=300)
    respondent_validation_video_anwer = models.CharField(max_length=300)
    video = models.ForeignKey('QoeVideo', on_delete=models.CASCADE)
    respondent = models.ForeignKey('Respondent', on_delete=models.CASCADE) #, related_name='respondent'

    class Meta:
        managed = False
        db_table = 'qoe_rating'
        unique_together = (('qoe_rating_id', 'video', 'respondent'),)

    def __str__(self):
        return self.qoe_rating_id
        # return f'{self.qoe_rating_id}-{self.qoe_rating_value}'


class Respondent(models.Model):
    respondent_id = models.AutoField(primary_key=True)
    age_range = models.CharField(max_length=200, choices=AGE_RANGE_CHOICES, blank=False, default='Unspecified')
    gender = models.CharField(max_length=45, choices=GENDER_CHOICES,
                              default='None')  # blank=False, default='Unspecified'

    class Meta:
        managed = False
        db_table = 'respondent'

    def __str__(self):
        return str(self.respondent_id)


class ValidationVideo(models.Model):
    validation_video_id = models.IntegerField(primary_key=True)
    validation_video_name = models.CharField(max_length=45)
    validation_video_file_path = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'validation_video'

    def __str__(self):
        return str(self.validation_video_id)
