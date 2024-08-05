calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    i = str(string)
    answer = (len(i), i.upper(), i.lower())
    count_calls()
    return answer


def is_contains(string, search_list):
    string = str(string).lower()
    search_list = list(search_list)
    count_calls()
    for i in range(len(search_list)):
        if search_list[i].lower() == string:
            answer = True
        else:
            answer = False
    return answer


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)