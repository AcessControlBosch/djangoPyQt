import requests

def get_token():
    resp = requests.post('http://127.0.0.1:8000/login/', {'username': 'admin', 'password': 'admin'})
    print (resp.status_code)
    # url = "http://127.0.0.1:8000/admin/api/user/"
    # x = requests.get(url, auth=('admin', 'admin'))
    #
    # user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))

    # response = requests.post(url)
    # print(x)

def get_data():
    url = "http://127.0.0.1:8000/admin/api/user/"
    header = { 'Authorization': f'Token {get_token()}'}
    response = requests.get(url, headers=header)
    emp_data = response.json()
    for e in emp_data:
        print(e)

get_token()