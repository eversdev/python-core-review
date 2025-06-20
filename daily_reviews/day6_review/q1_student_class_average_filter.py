class Student:
    """
    Represents a student with a name and a list of grades.
    
    Provides methods to:
    - Calculate the average grade.
    - Filter grades above a first threshold using a lambda with the `filter()` function.
    - Further filter the results using a second threshold and a list comprehension.
    """

    threshold1 = 30  # Baseline threshold for the first filter
    threshold2 = 50  # Baseline threshold for the second filter

    def __init__(self, name: str, grades: list):
        """
        Initializes a Student object with a name and a list of grades.
        """
        self.name = name
        self.grades = grades

    def av_grade(self) -> float:
        """
        Calculates and returns the average of the student's grades.
        Returns:
            float: The average grade.
        """
        return sum(self.grades) / len(self.grades)

    def filter_grade(self) -> list:
        """
        Filters the student's grades that are above the first threshold.

        Returns:
            list: Grades greater than threshold1.
        """
        return list(filter(lambda grade: grade > Student.threshold1, self.grades))

    def filter_above_threshold2(self, filtered_grade: list) -> list:
        """
        Further filters a given list of grades to include only those above the second threshold.

        Args:
            filtered_grade (list): A list of grades filtered by the first threshold.

        Returns:
            list: Grades greater than threshold2.
        """
        return [grade for grade in filtered_grade if grade > Student.threshold2]


# Example usage:
s1 = Student("Tim", [10, 5, 7, 30, 80, 20])

print(s1.filter_grade())                      # [80]
print(s1.filter_above_threshold2(s1.filter_grade()))  # [80]


