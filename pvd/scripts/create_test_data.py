from access.models.access import Access, Accessory, Grade, Student, ClassRoom, Computer


def run():  
    try:
        classroom = ClassRoom(name='Entrenamiento')
        classroom.save()

        grade = Grade(name='602')
        grade.save()

        pc = Computer(name='E02', classroom=classroom)
        pc.save()
        
        accessory = Accessory(name='Gafas 3D')
        accessory.save()

        student = Student(
            document='1019026756',
            first_name='Miguel',
            last_name_1='Mesa',
            last_name_2='Salazar',
            grade=grade)
        student.save()

        access = Access(
            student=student,
            classroom=classroom,
            computer=pc,   
        )
        access.save()
    except Exception as err:
        return f'Ocurrio un error {err}'
