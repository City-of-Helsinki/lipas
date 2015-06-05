# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.contrib.gis.db import models


class Venue(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    wkb_geometry = models.GeometryField(srid=3067, blank=True, null=True)
    gml_id = models.CharField(max_length=-1, blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)
    tyyppikoodi = models.IntegerField(blank=True, null=True)
    tyyppi_nimi_fi = models.CharField(max_length=-1, blank=True, null=True)
    tyyppi_nimi_se = models.CharField(max_length=-1, blank=True, null=True)
    tyyppi_nimi_en = models.CharField(max_length=-1, blank=True, null=True)
    nimi_fi = models.CharField(max_length=-1, blank=True, null=True)
    nimi_se = models.CharField(max_length=-1, blank=True, null=True)
    sijainti_id = models.IntegerField(blank=True, null=True)
    www = models.CharField(max_length=-1, blank=True, null=True)
    sahkoposti = models.CharField(max_length=-1, blank=True, null=True)
    puhelinnumero = models.CharField(max_length=-1, blank=True, null=True)
    muokattu_viimeksi = models.CharField(max_length=-1, blank=True, null=True)
    omistaja = models.CharField(max_length=-1, blank=True, null=True)
    yllapitaja = models.CharField(max_length=-1, blank=True, null=True)
    katuosoite = models.CharField(max_length=-1, blank=True, null=True)
    postinumero = models.CharField(max_length=-1, blank=True, null=True)
    postitoimipaikka = models.CharField(max_length=-1, blank=True, null=True)
    kuntanumero = models.IntegerField(blank=True, null=True)
    kunta_nimi_fi = models.CharField(max_length=-1, blank=True, null=True)
    lisatieto_fi = models.CharField(max_length=-1, blank=True, null=True)
    piste_json = models.CharField(max_length=-1, blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'lipas'
