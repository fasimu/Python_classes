"""
Python Classes: Medical Insurance Project
This project aims to develop a system that makes it easier to manage patient data.
All we have to do is create a class that does the following:
1. Takes in patient parameters regarding their personal information
2. Contains methods that allow users to update their information
3. Gives patients insight into their potential medical fees.

Let's get started!
"""

class Patient:
  def __init__(self, name, age, sex, bmi, num_of_children, smoker):
    self.name = name
    self.age = age
    self.sex = sex
    self.bmi = bmi
    self.num_of_children = num_of_children
    self.smoker = smoker
  
  # Adding Functionality
  def estimated_insurance_cost(self):
    estimated_cost = 250* self.age - 128* self.sex + 370* self.bmi + 425* self.num_of_children + 24000* self.smoker - 12500
    return "{}’s estimated insurance costs is {} dollars.".format(self.name, estimated_cost)

  # Update Methods
  def update_age(self, new_age):
    self.age = new_age
    return "{} is now {} years old.".format(self.name, self.age) + " " + self.estimated_insurance_cost()

  def update_num_children(self, new_num_children):
    self.num_of_children = new_num_children

    if self.num_of_children <= 1:
      return "{} has {} child.".format(self.name, self.num_of_children) + " " + self.estimated_insurance_cost()
    else:
      return "{} has {} children.".format(self.name, self.num_of_children) + " " + self.estimated_insurance_cost()
  
  def update_bmi(self, new_bmi):
    while True:
      try:
        self.bmi = int(new_bmi)
        return "{} is now has bmi {}.".format(self.name, self.bmi) + " " + self.estimated_insurance_cost()
      except ValueError as e:
        return "The value is not a proper integer! Try it again."

  def update_smoking_status(self, new_smoker_status):
    self.smoker = new_smoker_status
    if self.smoker == 0:
      return "{} is not a smoker now.".format(self.name) + " " + self.estimated_insurance_cost()
    else:
      return "{} is a smoker now.".format(self.name) + " " + self.estimated_insurance_cost()

  # Storing Patient Information
  def patient_profile(self):
    patient_info = {}
    patient_info["Name"] = self.name
    patient_info["Age"] = self.age
    patient_info["Sex"] = self.sex
    patient_info["BMI"] = self.bmi
    patient_info["Number of Children"] = self.num_of_children
    patient_info["Smoker"] = self.smoker
    return patient_info


# check class functionality
# added data
patient1 = Patient('John Doe', 25, 1, 22.2, 0, 0)

print(patient1.name)
# output: John Doe
print(patient1.estimated_insurance_cost())
# output: John Doe’s estimated insurance costs is 1836.0 dollars.
print(patient1.update_age(26))
# output: John Doe is now 26 years old. John Doe’s estimated insurance costs is 2086.0 dollars.
print(patient1.update_num_children(1))
# output: John Doe has 1 child. John Doe’s estimated insurance costs is 2511.0 dollars.
print(patient1.update_bmi(25.1))
# output: John Doe is now has bmi 25. John Doe’s estimated insurance costs is 3547 dollars.
print(patient1.update_smoking_status(1))
# output: John Doe is a smoker now. John Doe’s estimated insurance costs is 27547 dollars.
print(patient1.patient_profile())
# output: {'Name': 'John Doe', 'Age': 26, 'Sex': 1, 'BMI': 22.2, 'Number of Children': 1, 'Smoker': 0}