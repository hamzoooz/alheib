from django.shortcuts import render
import pandas as pd
from core.models import Student

# Create your views here.
def index(request):
    return render(request , 'index.html')


def add_Student(request):

    # Load the Excel file into a DataFrame
    df = pd.read_excel('students.xlsx')

    # Iterate over the rows in the DataFrame
    for index, row in df.iterrows():
    # Create a Student instance for each row
        student = Student(
            arabic_name=row['الاسم عربي'],
            name=row['الاسم إنجليزي'],
            level=row['CLASS'],
            dormitory=row['السكن'],
            sponsor_no=row['رقم المكفول'],
            sponsorship_source=row['جهة الكفالة'],
            sponsorship_status=row['حالة الكفالة'],
            registrar_notes=row['ملاحظات1'],
            director_notes=row['ملاحظات2'],
            school_notes=row['ملاحظات']
        )
        # Save the Student instance to the database
        student.save()

    return render(request, 'add_student.html')