import requests

def get_rest_api_data(token_x, web_api):
    print(f"\n{'__'*40} \nGet Rest API\n")

    header = {
        'Content-Type': 'application/json; odata.metadata=minimal; charset=utf-8'
        , 'Authorization': f'Token {token_x}'
    }

    response = requests.get(web_api
                             , headers=header)

    print(response.status_code)

    if response.status_code != 200 and response.status_code != 201:
        print('ERROR: Get Token failed')
        print(f"HTTP: {response.status_code}  \nReason: {response.reason} \nMessage: {response.text}")

        return

    else:
        print("Successfully")
        print(f"HTTP: {response.status_code}  \nReason: {response.reason}")

        return response


if __name__ == "__main__":

    output_x = get_rest_api_data(token_x, web_api)

else:
    pass

