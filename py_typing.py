import typing


# Old way
# student_name: str = "; DROP TABLE students; --"

# query = f"SELECT * FROM students WHERE name = {student_name}"

# print(query)

# New way
option: typing.Literal["YES", "NO"] = "YES"
