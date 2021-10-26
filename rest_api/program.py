
import services.authentication as au
from services.rest_api import get_rest_api_data

def run_program():
    # get the token.
    # token is valid for 24 hours. Therefore, once you get the token we should save it use it for the following 24h. Of course it differs from each data providers
    # Address to get the authentication
    token_address = "https://api...../Authentication/RequestToken"
    token_x = au.main_function(token_address)

    web_api = f"https://api....."
    response_2 = get_rest_api_data(
        token_x # token for authentication
        , web_api
    )

    str_output = response_2.text
    print(str_output)

    print("\033[1;30;46m Completed \033[m")

    return


if __name__ == "__main__":
    run_program()

