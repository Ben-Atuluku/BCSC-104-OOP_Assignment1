class Object:
    def __init__(self, durability, animation_len, costume_no, opacity):
        self.durability = durability
        self.animation_len = animation_len
        self.costume_no = costume_no
        self.opacity = opacity

class users:
    def __init__(self, name, email, dept, faculty, password):
        self.name = name
        self.email = email
        self.dept = dept
        self.faculty = faculty
        self.password = password

cardboard_box = Object(40, 1, 1, 100 )
metal_box = Object(120, 2, 1, 100 )
sand = Object(1, 3, 1, 25 )

print(metal_box.durability)