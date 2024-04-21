from django.shortcuts import render
import pandas as pd
from core.models import Student

# Create your views here.
def index(request):
    return render(request , 'index.html')

def add_Student(request):
    # Load the Excel file into a DataFrame
    df = pd.read_excel('students.xlsx')

    # Track the number of new students added
    new_students_added = 0

    # Iterate over the rows in the DataFrame
    for index, row in df.iterrows():
        # Check if a student with the same details already exists
 
        existing_student = Student.objects.filter(
            arabic_name=row['الاسم عربي'],
            name=row['الاسم إنجليزي'],
            residence_status=row['حالة السكن'],
            level=row['CLASS'],
            dormitory=row['السكن'],
            sponsor_no=row['رقم المكفول'],
            sponsorship_source=row['جهة الكفالة'],
            sponsorship_status=row['حالة الكفالة'],
            registrar_notes=row['ملاحظات1'],
            director_notes=row['ملاحظات2'],
            school_notes=row['ملاحظات'],
        ).exists()

        # If the student does not exist, create a new Student instance and save it
        if not existing_student:
            student = Student(
                arabic_name=row['الاسم عربي'],
                name=row['الاسم إنجليزي'],
                level=row['CLASS'],
                residence_status=row['حالة السكن'],
                dormitory=row['السكن'],
                sponsor_no=row['رقم المكفول'],
                sponsorship_source=row['جهة الكفالة'],
                sponsorship_status=row['حالة الكفالة'],
                registrar_notes=row['ملاحظات1'],
                director_notes=row['ملاحظات2'],
                school_notes=row['ملاحظات'],
                # residence_status=row['حالة السكن'],
            )
 
            student.save()
            new_students_added += 1

    # Render the template with a message indicating the number of new students added
    return render(request, 'add_student.html', {'new_students_added': new_students_added})



def add_Student_outer(request):
    # Load the Excel file into a DataFrame
    df = pd.read_excel('students-outer.xlsx')

    # Track the number of new students added
    new_students_added = 0

    # Iterate over the rows in the DataFrame
    for index, row in df.iterrows():
        # Check if a student with the same details already exists
        full_name = f"{row['SURNAME']} {row['OTHER NAME']}"
        
        existing_student = Student.objects.filter(
                arabic_name=row['اسم عربي'],
                name=full_name, 
                level=row['CLASS'],
                system=row['النظام'],
                registrar_notes=row['ملاحظة'],
                dormitory=row['السكن'], 
                
        ).exists()

        # If the student does not exist, create a new Student instance and save it
        if not existing_student:
            student = Student(
                arabic_name=row['اسم عربي'],
                name=full_name, 
                system=row['النظام'],
    
                level=row['CLASS'],
                registrar_notes=row['ملاحظة'],
                dormitory=row['السكن'], 
            )
 
            student.save()
            new_students_added += 1

    # Render the template with a message indicating the number of new students added
    return render(request, 'add_student.html', {'new_students_added': new_students_added})




# def add_Student(request):

#     # Load the Excel file into a DataFrame
#     df = pd.read_excel('students.xlsx')

#     # Iterate over the rows in the DataFrame
#     for index, row in df.iterrows():
#     # Create a Student instance for each row
#         student = Student(
#             arabic_name=row['الاسم عربي'],
#             name=row['الاسم إنجليزي'],
#             level=row['CLASS'],
#             dormitory=row['السكن'],
#             sponsor_no=row['رقم المكفول'],
#             sponsorship_source=row['جهة الكفالة'],
#             sponsorship_status=row['حالة الكفالة'],
#             registrar_notes=row['ملاحظات1'],
#             director_notes=row['ملاحظات2'],
#             school_notes=row['ملاحظات']
#         )
#         # Save the Student instance to the database
#         student.save()

#     return render(request, 'add_student.html')



