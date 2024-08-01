shopping_list = []

def add_item(item):
    shopping_list.append(item)
    print(f'Added {item} to the list.')

def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f'Removed {item} from the list.')
    else:
        print(f'{item} not found in the list.')

def show_list():
    print(shopping_list)

def clear_list():
    shopping_list.clear()
    print(f'List is cleared: {shopping_list}')

def sort_list():
    shopping_list.sort()
    print(f'List is sorted: {shopping_list}')

def list_of_commands():
    print('add: add an item to the list')
    print('remove: remove an item from the list')
    print('show: show the list')
    print('clear: clear the list')
    print('sort: sort the list')
    print('quit: quit program')
    print('help: show the list of commands available')

while True:
    user_input = input("Enter a command or type 'help' for the list of commands: ")

    if user_input == 'help':
        list_of_commands()

    elif user_input == 'add':
        ele = input('Enter item to add to the list: ')
        add_item(ele)

    elif user_input == 'remove':
        ele = input('Item you want to remove from the list: ')
        remove_item(ele)

    elif user_input == 'show':
        show_list()

    elif user_input == 'clear':
        clear_list()

    elif user_input == 'sort':
        sort_list()

    elif user_input == 'quit':
        break

    else:
        print('Invalid command!')
