users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
n_total = len(users)
n_uniq_users = len(set(users))
dict_ = {
    "Общее количество":0,
    "Уникальные посещения":0,
}

dict_["Общее количество"] = n_total
dict_["Уникальные посещения"] = n_uniq_users
print(dict_)

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
