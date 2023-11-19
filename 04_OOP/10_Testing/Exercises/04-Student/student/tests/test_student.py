from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.beginner = Student("Asd")
        self.advanced = Student("Sam", {"phyton": ['a', 'b', 'c']})

    def test_correct_initialization(self):
        self.assertEqual("Asd", self.beginner.name)
        self.assertEqual({}, self.beginner.courses)

        self.assertEqual("Sam", self.advanced.name)
        self.assertEqual({"phyton": ['a', 'b', 'c']}, self.advanced.courses)

    def test_enroll_if_course_in_courses(self):
        res = self.advanced.enroll("phyton", ['d'])
        self.assertEqual({"phyton": ['a', 'b', 'c', 'd']}, self.advanced.courses)

        self.assertEqual("Course already added. Notes have been updated.", res)

    def test_enroll_if_new_course_and_add_course_notes_is_y(self):
        res = self.beginner.enroll("java", ['a'], "Y")
        self.assertEqual({"java": ['a']}, self.beginner.courses)
        self.assertEqual("Course and course notes have been added.", res)

    def test_enroll_if_new_course_and_add_course_notes_is_empty_str(self):
        res = self.beginner.enroll("java", ['a'], "")
        self.assertEqual({"java": ['a']}, self.beginner.courses)
        self.assertEqual("Course and course notes have been added.", res)

    def test_enroll_if_new_course_and_add_course_notes_diff_to_y_or_empty_str(self):
        res = self.beginner.enroll("java", ['a'], "re")
        self.assertEqual({"java": []}, self.beginner.courses)
        self.assertEqual("Course has been added.", res)

    def test_add_notes_if_course_exist(self):
        res = self.advanced.add_notes("phyton", 'd')
        self.assertEqual({"phyton": ['a', 'b', 'c', 'd']}, self.advanced.courses)

        self.assertEqual("Notes have been updated", res)

    def test_add_notes_if_new_course_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.beginner.add_notes("phyton", 'd')

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_if_course_exists(self):
        res = self.advanced.leave_course("phyton")
        self.assertEqual("Course has been removed", res)

    def test_leave_course_if_course_not_exists_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.advanced.leave_course("java")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()
