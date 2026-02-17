import requests

BASE_URL = 'https://open.er-api.com/v6/latest/'

def get_latest_rate(base):
    url = BASE_URL + base.upper()

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        if data.get("result") == "success":
            return  data.get('base_code'), data.get('rates')
        else:
            print('API returned an error.')
            return None, None

    except requests.exceptions.Timeout:
        print('Error: The request timed out.')
    except requests.exceptions.ConnectionError:
        print('Error: No internet connection.')
    except requests.exceptions.HTTPError as er_http:
        print(f'HTTP error occurred: {er_http}')
    except Exception as e:
        print(f'Unexpected error: {e}')

    return None, None