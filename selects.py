def select_all_female_dogs_name_and_breed():
    return cur.execute("""SELECT name, breed FROM dogs WHERE gender = 'F';""").fetchall()

def select_all_dogs_names_in_alphabetical_order():
    return cur.execute("""SELECT name FROM dogs ORDER BY name;""").fetchall()

def select_nameless_dog():
    return cur.execute("""SELECT * FROM dogs WHERE name IS NULL;""").fetchall()

def select_hungry_dogs_name_and_breed_ordered_by_youngest_to_oldest():
    return cur.execute("""SELECT name, breed FROM dogs WHERE hungry = '1' ORDER BY age;""").fetchall()

def select_name_age_and_temperament_of_oldest_dog():
    return cur.execute("""SELECT name, age, temperament FROM dogs ORDER BY age DESC LIMIT 1;""").fetchall()

def select_name_and_age_of_three_youngest_dogs():
    return cur.execute("""SELECT name, age FROM dogs ORDER BY age LIMIT 3;""").fetchall()

def select_name_and_breed_of_dogs_between_age_five_and_ten_ordered_by_oldest_to_youngest():
    return cur.execute("""SELECT name, breed FROM dogs WHERE age BETWEEN 5 and 10 ORDER BY age DESC;""").fetchall()

def select_name_age_and_hungry_of_hungry_dogs_between_age_two_and_seven_in_alphabetical_order():
    return cur.execute("""SELECT name, age, hungry FROM dogs WHERE hungry = '1' AND age BETWEEN 2 and 7 ORDER BY name;""").fetchall()
