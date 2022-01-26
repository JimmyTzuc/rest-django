from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Populate Database'

    def seeder_database(self):
        User = get_user_model()

        admin = User.objects.create_user('admin', 'admin@admin.com', 'admin', **{"is_active": True, "is_staff": True, "is_superuser": True})
        staff = User.objects.create_user('staff', 'staff@staff.com', 'staff', **{"is_active": True, "is_staff": True})
        user = User.objects.create_user('user', 'user@user.com', 'user', **{"is_active": True})
        nora = User.objects.create_user('nora', 'nora@norashop.com', 'norashop', **{"is_active": True, "is_staff": True, "is_superuser": True})
        employee = User.objects.create_user('employee', 'employee@user.com', 'employee', **{"is_active": True})
        
        
        
       

    def handle(self, *args, **options):
        self.seeder_database()