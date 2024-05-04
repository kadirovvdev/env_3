
def create(data, a):
    data.append(a)
    return data

def read(data):
    return data

def update(data, index, a):
    if index >= 0 and index < len(data):
        data[index] = a
    else:
        print("Index xato!")
    return data

def delete(data, index):
    if index >= 0 and index < len(data):
        del data[index]
    else:
        print("Index xato!")
    return data

if __name__ == "__main__":
    my_data = ["a1", "a2", "a3"]
    print("Asl ma'lumotlar:", my_data)

    my_data = create(my_data, "a4")
    print("CREATE natijasi:", my_data)

    print("READ natijasi:", read(my_data))

    my_data = update(my_data, 1, "updated_item")
    print("UPDATE natijasi:", my_data)

    my_data = delete(my_data, 2)
    print("DELETE natijasi:", my_data)
