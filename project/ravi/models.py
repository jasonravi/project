from django.db import models
from .tests import *
# Create your models here.


class User(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50,unique=True)
	created_on = UnixTimestampField(auto_now_add=True)
	updated_on = UnixTimestampField(auto_now=True)
	created_by = models.CharField(max_length=50, blank=True,null=True)
	class Meta:
		managed = False
		db_table = 'user'

	def __unicode__(self):
		return unicode(self.name) 

	def save(self, *args, **kwargs):
		if not self.created_on:
			self.created_on = datetime.now()
		super(User, self).save(*args, **kwargs)

class Role(models.Model):
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=50,unique=True)
   created_on = UnixTimestampField(auto_now_add=True)
   updated_on = UnixTimestampField(auto_now=True)
   created_by = models.CharField(max_length=50, blank=True,null=True)
   user = models.ForeignKey(User, blank=True, null=True,db_column='user_id')
   class Meta:
	  managed = False
	  db_table = 'role'

   def __unicode__(self):
	   return unicode(self.name) 

   def save(self, *args, **kwargs):
		if not self.created_on:
			self.created_on = datetime.now()
		super(Role, self).save(*args, **kwargs)


class Permission(models.Model):
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=50,unique=True)
   created_on = UnixTimestampField(auto_now_add=True)
   updated_on = UnixTimestampField(auto_now=True)
   created_by = models.CharField(max_length=50, blank=True,null=True)
   user = models.ForeignKey(Role, blank=True, null=True,db_column='role_id')
   class Meta:
	  managed = False
	  db_table = 'permission'

   def __unicode__(self):
	   return unicode(self.name) 

   def save(self, *args, **kwargs):
		if not self.created_on:
			self.created_on = datetime.now()
			super(Permission, self).save(*args, **kwargs)

