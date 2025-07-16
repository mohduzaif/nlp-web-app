import json

class Database:

    # function to stored the user information
    def insert_data(self, name, email, password): 

        with open('user.json', 'r') as rf: 
            user_data = json.load(rf)

        if email in user_data:
            return 0
        else: 
            user_data[email] = [name, password]

        with open('user.json', 'w') as wf:
            json.dump(user_data, wf, indent=4)
            return 1
        
    # function to search the user and validate the user.
    def search_user(self, email, password):
        
        with open('user.json', 'r') as rf:
            data = json.load(rf)

            if email in data:
                user_info = data[email]
                if user_info[1] == password:
                    return 1
                else:
                    return 0
            else:
                return 0