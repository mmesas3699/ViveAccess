from django.contrib import admin

# Register your models here.
from access.models import Access, Accessory, Classroom, Computer, Grade, Student


@admin.register(Access)
class AccessAdmin(admin.ModelAdmin):
	list_display = ['date',
					'entry',
					'student',
					'departure',
					'computer',
					'accessory',
					'observation']


@admin.register(Accessory)
class AccessAdmin(admin.ModelAdmin):
	pass


@admin.register(Classroom)
class AccessAdmin(admin.ModelAdmin):
	pass


@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
	list_display = ('name', 'classroom')


@admin.register(Grade)
class AccessAdmin(admin.ModelAdmin):
	pass


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display = ('document',
					'first_name',
					'last_name_1',
					'last_name_2',
					'grade')
