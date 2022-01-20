"""
Prototype Design Pattern (Creational)
Use for cloning objects.

Sometimes we may want to copy an object. One way to do this is to reconstruct the object.
    And all new object fields must be set to the original object fields.
    But this is troublesome. Because we need to know all the main object fields,
    and on the other hand, some main object fields may be private,
    and we may not have access to their values. So the method of object
    reconstruction does not make sense. So to reproduce
    we have to be able to copy the original object.

Example :
    In this example we are going to duplicate an exam sheet with questions along with the student's name

"""

import copy


class Prototype:
    def __init__(self):
        """ set objects by empty dict """
        self.__objects = {}

    def register_object(self, name, obj):
        """ register object in objects dictionary """
        self.__objects[name] = obj

    def remove_object(self, name):
        """ remove object from objects dictionary """
        if name in self.__objects.keys():
            del self.__objects[name]

    def clone(self, name, **attr):
        """  get key of object in objects dictionary and clone this object and update object attribute by attr """
        if name in self.__objects.keys():
            duplicate_object = copy.deepcopy(self.__objects[name])
            duplicate_object.__dict__.update(attr)
            return duplicate_object


class Question:
    """ Question class with title and content of question """

    def __init__(self, title, content):
        self.title = title
        self.content = content


class ExamSheet:
    """ ExamSheet class with list of questions and student name """

    def __init__(self, questions, student_name):
        self.questions = questions
        self.student_name = student_name

    def __str__(self):
        return f"{self.student_name} - {id(self)}"

    def clone(self, student_name):
        """ Clone ExamSheet by using prototype class """
        prototype_instance = Prototype()
        prototype_instance.register_object('exam_sheet', self)
        return prototype_instance.clone('exam_sheet', student_name=student_name)


if __name__ == '__main__':
    # Create questions
    q1 = Question('question1', 'what is ...')
    q2 = Question('question2', 'what is ...')
    q3 = Question('question3', 'what is ...')

    # students name
    students_list = ['Gloria Cantu', 'Winston Cardenas', 'Konner Coleman', 'Stella Cuevas']

    """ Create ExamSheet instance"""
    exam_sheet = ExamSheet([q1, q2, q3], 'Amir Mohtasham')

    for student in students_list:
        exam = exam_sheet.clone(student)
        print(exam)
