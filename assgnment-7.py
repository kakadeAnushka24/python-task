# data-Dictionary
data = {
    "employees": [
        [
            "id", 101,
            "name", "Alice",
            "skills", ["Python", "SQL", "GCP"],
            "projects", [
                {"project_id": "P1", "status": "Completed"},
                {"project_id": "P2", "status": "Ongoing"}
            ],
            
            ["id", 102,
            "name", "Bob",
            "skills", ["Python", "SQL", "GCP"],
            "projects", [
                {"project_id": "P1", "status": "Completed"},
                {"project_id": "P2", "status": "Ongoing"}]
            ]
        ]
    ]
}
# employees----Is a key
bob_data = data["employees"][0][8]

# 'id', 102
print(bob_data[0:2])

# 'name', 'Bob'
print(bob_data[2:4])



