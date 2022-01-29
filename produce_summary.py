def print_info_from_file(line_text):
    line = line_text.rstrip()
    words = line_text.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]
    print(f"Delivered {count} {melon}s for total of ${amount}")


# print("Day 1")
the_file = open("um-deliveries-day-1.txt")
for line in the_file:
    print_info_from_file(line)
the_file.close()


print("Day 2")
the_file = open("um-deliveries-day-2.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]

    print(f"Delivered {count} {melon}s for total of ${amount}")
the_file.close()


print("Day 3")
the_file = open("um-deliveries-day-3.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]

    print(f"Delivered {count} {melon}s for total of ${amount}")
the_file.close()
