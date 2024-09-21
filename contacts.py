contacts = {
    "number": 5,
    "students":
        [
            {"name":"Brian LeMaster", "email":"brian@example.com"},
            {"name":"George Jefferson", "email":"george@example.com"},
            {"name":"Oscar Wilde", "email":"oscar@example.com"},
            {"name":"Beatrice McGee", "email":"bea@example.com"}
        ]
}

print('Student emails:')
for student in contacts['students']:
    print(student['name'], student['email'], sep=" >> ")