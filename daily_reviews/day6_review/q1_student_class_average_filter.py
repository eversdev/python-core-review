class Student:
    def __init__(self, name: str, grades: list):
        self.name = name
        self.grades = grades

    def av_grade(self) -> float:
        return sum(self.grades) / len(self.grades)
    
    threshold1 = 30
    threshold2 = 50
    
    def filter_grade(self) -> list:
        filtered_grade = list(filter(lambda grade: grade > Student.threshold1, self.grades))
        return filtered_grade
    
    def filter_above_threshold2(self, filtered_grade) -> list:
        new_list = [grade for grade in filtered_grade if grade > Student.threshold2]
        return new_list


        
s1 = Student("Tim", [10, 5, 7, 30, 80, 20])

print(s1.filter_grade())
print(s1.filter_above_threshold2(s1.filter_grade()))

