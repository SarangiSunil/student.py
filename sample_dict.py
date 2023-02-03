python
Copy code
sample_dict = {"name": "John", "age": 5, "salary": 8000, "city": "New York"}

sample_dict["location"] = sample_dict.pop("city")

print("The updated dictionary is:", sample_dict)
