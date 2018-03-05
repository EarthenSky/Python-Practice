# A person class with a weight and a gender.
# equality compares gender, while ge and gt compares weight
class person:
    def __init__(self, weight, gender):
        self.m_weight = weight
        self.m_gender = gender

    # These are the overloaded operators for this class
    def __ge__(self, other):
        return self.m_weight >= other.m_weight

    def __gt__(self, other):
        return self.m_weight >= other.m_weight

    def __eq__(self, other):
        return self.m_gender == other.m_gender
#end class

bob = person(70, "m")
kate = person(60, "f")
kim = person(59, "f")

print bob == kate # false
print bob >= kim # true
