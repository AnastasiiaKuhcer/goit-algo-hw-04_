def write_to_file(path, data):
    try:
        with open(path, 'w', encoding='utf-8') as file:
            file.write('\n'.join(data))
        print(f"Дані успішно записані у файл {path}")
    except Exception as e:
        print(f"Під час запису виникла помилка: {e}")

cats_data = [
    "60b90c1c13067a15887e1ae1,Tayson,3",
    "60b90c2413067a15887e1ae2,Vika,1",
    "60b90c2e13067a15887e1ae3,Barsik,2",
    "60b90c3b13067a15887e1ae4,Simon,12",
    "60b90c4613067a15887e1ae5,Tessi,5"
]

write_to_file("cats_info.txt", cats_data)

def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_data = line.strip().split(',')
                cat_info = {"id": cat_data[0], "name": cat_data[1], "age": cat_data[2]}
                cats_info.append(cat_info)
        return cats_info
    except Exception as e:
        print(f"Помилка: {e}")
        return None

cats_info = get_cats_info("cats_info.txt")
if cats_info:
    for cat in cats_info:
        print(cat)



