def do_something_with_file():
    try:
        # Открытие файла в режиме записи
        file = open("file.txt", "w")
        print("Successfully opened the file")
        # записываем в файл строку 'Hello!'
        file.write('Hello!')
    except FileNotFoundError:
        # Обработка исключения, возникающего в том случае, если файл не найден
        print("File Not Found Error: No such file or directory")
        exit()
    except PermissionError:
        # Обработка ошибок, связанных с разрешением на доступ к файлу
        print("Permission Denied Error: Access is denied")
    # закрываем файл даже в том случае, если выше возникло исключение
    finally:
        file.close()