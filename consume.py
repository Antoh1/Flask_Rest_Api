import requests

url = 'http://127.0.0.1:5000/'

data = [{'likes': 20, 'views':43, 'name':'Anaconda Tutorial'},
        {'likes': 67, 'views':45000, 'name':'Flask Tutorial'},
        {'likes': 30, 'views':3400, 'name':'Django Tutorial'},]

for i_d in range(len(data)):
    response = requests.put(url + 'user/' + str(i_d+1), data[i_d])
    print(response.json())
user_id = int(input())
response2 = requests.get(url + 'user/' + str(user_id))
print(response2.json())
patcho = {'name':'Code with Anto'}
user_id = int(input())
response4 = requests.patch(url + 'user/' + str(user_id), patcho)
print(response4.json())
# input()
# response3 = requests.delete(url + 'user/2')
# print(response3)
# input()
# response2 = requests.get(url + 'user/0')
# print(response2.json())
