class Person():

    def is_adult(self, age):
        adult_age = 18
        return age >= adult_age

def test_is_adult_when_age_is_more_than18_true():
    person = Person()
    age = 20
    actual_result = person.is_adult(age)
    assert actual_result