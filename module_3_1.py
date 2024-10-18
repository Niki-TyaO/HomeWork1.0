calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    cor = []
    cor.append(len(string))
    cor.append(string.upper())
    cor.append(string.lower())
    print(cor)


def is_contains(string, list_to_search):
    count_calls()
    for num in range(len(list_to_search)):
        list_to_search[num] = list_to_search[num].lower()

    print(list_to_search)

    if string.lower() in list_to_search:
        print(True)
    else:
        print(False)
        return list_to_search

string_info('Coconut')
string_info('Banana')
is_contains('MoUNt',['babs', 'MoUnT', 'sneak'])
is_contains('Mount',['babs', 'fly', 'sneak'])
print(calls)