from openpyxl.styles.builtins import total
from twisted.python.util import nameToLabel

from Student import StudentNode, Student

class StudentList(object):
    def __init__(self):
        self.head = None   # You have to store the head pointer in ``head'' variable.

    def loadFromFile(self, filename):
        """

        :param filename:
        :return:
        """
        with open(filename, 'r') as file:
            prev = None

            for line in file:
                # Remove any leading/trailing whitespace characters like newlines
                line = line.strip()

                # Split the line by the | delimiter
                name, student_id, height, dorm = line.split('|')

                # Convert student_id, height, dorm to integers
                student_id = int(student_id)
                height = int(height)
                dorm = int(dorm)

                new_student = StudentNode(name, student_id, height, dorm)

                if not self.head:
                    self.head = new_student
                else:
                    prev.setNext(new_student)

                prev = new_student

    def averageHeight(self):
        """

        :return:
        """
        if not self.head:
            return - 1

        cnt = 0
        curr = self.head
        total_height = 0

        while curr:
            total_height += curr.getStudent().height
            cnt += 1
            curr = curr.next

        return total_height / cnt

    def getStudentHeight(self, name):
        """

        :param name:
        :return:
        """
        curr = self.head

        while curr:
            if curr.getStudent().name == name:
                return curr.getStudent().height

            curr = curr.getNext()
        return - 1

    def getDormStudents(self, dorm):
        """

        :param dorm:
        :return:
        """
        new_ll = StudentList()
        prev_new = None
        curr = self.head

        while curr:
            if curr.getStudent().dorm == dorm:
                tmp = curr.getStudent()
                if not new_ll.head:
                    new_ll.head = tmp
                else:
                    prev_new.setNext(tmp)

                prev_new = tmp
            curr = curr.getNext()




if __name__ == '__main__':
    pass