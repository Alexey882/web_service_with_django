from django.db import models
class Parser(models.Model):
    id_parse_page = models.AutoField(primary_key=True)
    json_res = models.TextField()