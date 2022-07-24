
task_run = int(input("Please enter number task. 0, 1 or 2 >>"))

if task_run == 0:

    data = ""

    result_string = []
    result_words = []

    while data:
        result_string.clear()
        for i in range(len(data)):
            if i % 2:
                data_chunk = f"{data[i-1]}{data[i]}"
                try:
                    data_chunk = chr(int(data_chunk, 16))
                except ValueError:
                    result_words.pop(-1)
                    print("\n".join(result_words))
                    exit()
                result_string.insert(0, data_chunk)

        data = "".join(result_string).split('|')

        if any(map(str.isdigit, data[0])):
            result_words.append(data[1].strip()[::-1])
            data = data[0].strip()[::-1]

        elif any(map(str.isdigit, data[1])):
            result_words.append(data[0].strip())
            data = data[1].strip()


elif task_run == 1:

    # frontend --------------------------
    info = """
    USER:\t\t{} 
    LAST CMD:\t{}
    """

    # database --------------------------
    database = {}

    # session ---------------------------
    current_user = 'anonimus'

    # backend ---------------------------
    working = True
    cmd = "null"

    while working:
        print(info.format(current_user, cmd))
        cmd = input(">> ")
        if cmd == "singin":
            login = input("login: ")
            if hash(login) not in database:
                password_1 = input("password: ")
                password_2 = input("repeat password: ")
                if password_1 == password_2:
                    database[hash(login)] = hash(password_1)

        elif cmd == "login":
            if current_user == 'anonimus':
                login = input("login: ")
                password = input("password: ")
                if hash(login) in database and database.get(hash(login)) == hash(password):
                    current_user = login

        elif cmd == "log out":
            current_user = 'anonimus'
        else:
            working = False
    else:
        print("WORK COMPLETED")

elif task_run == 2:

    # frontend ------------------------------------------
    bucket_3l_list = [" ", " ", " "]
    bucket_5l_list = [" ", " ", " ", " ", " "]
    clear = "\b" * 10000
    front = """

        3l             5l
                  _____________
                  \{7}{7}{7}{7}{7}{7}{7}{7}{7}{7}{7}/
    _________      \{6}{6}{6}{6}{6}{6}{6}{6}{6}/
    \{2}{2}{2}{2}{2}{2}{2}/       \{5}{5}{5}{5}{5}{5}{5}/ 
     \{1}{1}{1}{1}{1}/         \{4}{4}{4}{4}{4}/
      \{0}{0}{0}/           \{3}{3}{3}/ 
       ¯¯¯             ¯¯¯
    """

    # database ------------------------------------------
    database = {
        'bucket_3l': 0,
        'bucket_5l': 0,
    }

    # backend -------------------------------------------
    working = True
    count = 0

    while working:
        count += 1

        # --------------------------------------------------------------
        bucket_3l_list = (["@"] * database['bucket_3l'] + [" "] * 3)[:3]
        bucket_5l_list = (["@"] * database['bucket_5l'] + [" "] * 5)[:5]
        print(front.format(*(bucket_3l_list[:4] + bucket_5l_list)))
        cmd = input(">> ")
        # --------------------------------------------------------------

        if cmd == "fill_5l":
            database['bucket_5l'] = 5

        elif cmd == "fill_3l":
            database['bucket_3l'] = 3

        elif cmd == "pour_5l":
            database['bucket_5l'] = 0

        elif cmd == "pour_3l":
            database['bucket_3l'] = 0

        elif cmd == "pour_from_5_to_3":
            if 3 - (database['bucket_5l'] + database['bucket_3l']) < 0:
                database['bucket_5l'] = (database['bucket_5l'] + database['bucket_3l']) - 3
                database['bucket_3l'] = 3

            elif 3 - (database['bucket_5l'] + database['bucket_3l']) == 0:
                database['bucket_3l'] = 3
                database['bucket_5l'] = 0
            elif 3 - (database['bucket_5l'] + database['bucket_3l']) > 0:
                database['bucket_3l'] = database['bucket_5l'] + database['bucket_3l']
                database['bucket_5l'] = 0

        elif cmd == "pour_from_3_to_5":
            if 5 - (database['bucket_5l'] + database['bucket_3l']) < 0:
                database['bucket_3l'] = (database['bucket_5l'] + database['bucket_3l']) - 5
                database['bucket_5l'] = 5

            elif 5 - (database['bucket_5l'] + database['bucket_3l']) == 0:
                database['bucket_5l'] = 5
                database['bucket_3l'] = 0
            elif 5 - (database['bucket_5l'] + database['bucket_3l']) > 0:
                database['bucket_5l'] = database['bucket_5l'] + database['bucket_3l']
                database['bucket_3l'] = 0

        elif cmd == 'exit':
            print(f"Numbers of moves -{count}-!")
            exit()

        if database['bucket_5l'] == 4:
            print(f"!!!YOU WIN!!!Numbers of moves  {count}!")
            exit()

        print(clear)






