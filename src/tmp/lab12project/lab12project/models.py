import boto3
from dynamorm import DynaModel
from marshmallow import fields
from django.conf import settings


class MyUserTable(DynaModel):
	class Table:
		resource_kwargs = {
			'endpoint_url': settings.DB_ENDPOINT
		}
		name = settings.DB_USERTABLE
		hash_key = 'email'
		read = 25
		write = 5

	class Schema:
		name = fields.String()
		role = fields.String()
		email = fields.Email()
		created_on = fields.DateTime()

ROLE_CHOICES = [('', 'choose role'), ('admin', 'Admin'), ('teacher', 'Teacher'), ('student', 'Student')]
