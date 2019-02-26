import os
from django.core.management.base import BaseCommand


class Command(BaseCommand):
	help = "Renames a django project"

	def add_arguments(self, parser):
		parser.add_argument('new_project_name', type=str, help='The new project Name')

	def handle(self, *args, **kwargs):
		new_project_name = kwargs['new_project_name']
		current_project_name = str(os.environ.get("DJANGO_SETTINGS_MODULE")
			.split('.')[0])
		files_to_rename = [f'{current_project_name}/settings/development.py', 
							f'{current_project_name}/wsgi.py', 'manage.py' ]
		folder_to_rename = current_project_name

		for f in files_to_rename:
			with open(f, 'r') as file:
				filedata = file.read()
			filedata = filedata.replace(current_project_name, new_project_name)

			with open(f, 'w') as file:
				file.write(filedata)
		os.rename(folder_to_rename, new_project_name)
		self.stdout.write(self.style.SUCCESS(
			f'Project has been renamed to {new_project_name}'))
