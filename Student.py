### Changes to this file is NOT allowed!
### Submission of this file will be IGNROED by the autograder!

class Student(object):
    def __init__(self, name, student_id, height, dorm):
        if not isinstance(student_id, int):
            raise ValueError('student_id must be an integer')
        if not isinstance(height, int):
            raise ValueError('height must be an integer')
        if not isinstance(dorm, int):
            raise ValueError('dorm must be an integer')

        self.name = name
        self.student_id = student_id
        self.height = height
        self.dorm = dorm

    def __str__(self):
        return f"Student {self.name}, Student ID: {self.student_id}, Height: {self.height}, Dorm: {self.dorm}"



class StudentNode(object):
    def __init__(self, name, student_id, height, dorm):
        self.student = Student(name, student_id, height, dorm)
        self.next = None

    def getNext(self):
        """
        Get the next student node in the LL
        :return:
        """
        return self.next

    def getStudent(self):
        """
        Get the student instance in the node
        :return:
        """
        return self.student

    def setNext(self, new_next):
        """
        Set the next student node for the current node
        :param new_next:
        :return:
        """
        self.next = new_next

    def replicate(self):
        """
        Create a replicate node with the same student object.
        The new node will have the reference to the same student object.
        Note: the replicated node will have next pointer points to None.
        :return: The replicated node
        """
        rep = StudentNode("", 0, 0, 0)
        new_instances = rep.student
        rep.student = self.student
        del new_instances
        return rep

    def __str__(self):
        return str(self.student)


if __name__ == '__main__':
    node = StudentNode("test", 1, 1, 1)
    rep_node = node.replicate()

    assert rep_node.next is None
    assert rep_node.getStudent() is node.getStudent()

