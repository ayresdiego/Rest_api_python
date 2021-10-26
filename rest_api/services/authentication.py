import requests
import json
from datetime import datetime, timedelta
import os


import inspect
import sys
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from credentials import Login, Password


def get_token(token_address):
    print(f"\n{'__'*40} \nGetting Token\n")

    # Dictionary with Credentials
    dict_credentials = {'Credentials':
                            {'Password': Password
                              , 'Username': Login}
                        }

    login_json = json.dumps(dict_credentials) # converts python object into json Json String format

    # Header contain meta-data associated with the API request and response
    header = {
        'Content-Type': 'application/json; odata.metadata=minimal'
        , 'prefer': 'respond-async'
    }

    # response = requests.post(token_address)
    r = requests.post(token_address
                      , data=login_json # login data in the Json String format
                      , headers=header
                      )

    if r.status_code == 200:
        print("Authenticated")
        print(f"HTTP: {r.status_code}  \nReason: {r.reason} \nMessage: {r.text}")

        j = r.json()
        token_x = j["value"]
        print(token_x)

        with open(os.path.join(path_x, 'token_key.txt'), 'w') as f:
            # json.dump(token_x, f)  # save the Json file
            f.write(token_x)
            f.write("\n" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") )

        print(f'\nToken: Successfully created \n')

        return

    else:
        print('ERROR: Get Token failed')
        input(f"HTTP: {r.status_code}  \nReason: {r.reason} \nMessage: {r.text}")
        return


def get_delta(l, r): # amount of hours between date
    return abs(int((l-r).total_seconds())) / 3600


def get_amount_hours_last_update():
    end_date_time = datetime.now()

    with open(os.path.join(path_x, 'token_key.txt')) as f:
        data = f.readlines()
        start_date_time = data[1]

        start_date_time = datetime.strptime(start_date_time, "%Y-%m-%d %H:%M:%S")

        hours_amount = get_delta(start_date_time, end_date_time)

        return hours_amount

def main_function(token_address):
    print(f"\n{'__' * 40} \nAuthentication\n")

    # print(os.path.join(path_x, 'token_key.txt'))
    try:
        hours_amount = get_amount_hours_last_update()
    except:
        hours_amount = 25

    if hours_amount > 24 :
        get_token(token_address)

    else:
        print(f"\nToken still valid\n")
        # pass


    with open( os.path.join(path_x, 'token_key.txt') ) as f: # test 2
        data = f.readlines()
        token_x = data[0]


    return token_x[:-1] # remove the \n


global path_x
path_x = r"output_data"

if __name__ == "__main__":
    main_function(token_address)
