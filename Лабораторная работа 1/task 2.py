# TODO Найдите количество книг, которое можно разместить на дискете

disk_volume_mb = 1.44
number_of_pages = 100
number_of_lanes = 50
lane_simbles = 25
volume_for_one_unit = 4

disk_volume_kb = disk_volume_mb * 1024 * 1024

volume_for_1_book_kb = number_of_pages * number_of_lanes * lane_simbles * volume_for_one_unit

Avaulable_number_of_books = int(disk_volume_kb / volume_for_1_book_kb)

print("Количество книг, помещающихся на дискету:", Avaulable_number_of_books)
