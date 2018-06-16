import requests
import time
from app import host_name

service_address = 'http://' + host_name + ':5000/'
print('0. Service address is: {0}'.format(service_address))
time.sleep(0.5)

print('1. GET /movies')
get_test = requests.get(service_address + 'movies')
print(get_test.text)
time.sleep(0.5)

print('2. GET /movies/Birdman')
get_test = requests.get(service_address + 'movies/Birdman')
print(get_test.text)
time.sleep(0.5)

print('3. GET 404 /movies/Birdmaan')
get_test = requests.get(service_address + 'movies/Birdmaan')
print(get_test.text)
time.sleep(0.5)

print('4. GET /movies/rating/9.0')
get_test = requests.get(service_address + 'movies/rating/9.0')
print(get_test.text)
time.sleep(0.5)

print('5. GET 404 /movies/rating/9.9')
get_test = requests.get(service_address + 'movies/rating/9.9')
print(get_test.text)
time.sleep(0.5)

print('6. GET 400 /movies/rating/11.5')
get_test = requests.get(service_address + 'movies/rating/11.5')
print(get_test.text)
time.sleep(0.5)

print('7. GET actor/Edward Norton')
get_test = requests.get(service_address + 'actor/Edward%20Norton')
print(get_test.text)
time.sleep(0.5)

print('8. GET 404 actor/Edward Morton')
get_test = requests.get(service_address + 'actor/Edward%20Morton')
print(get_test.text)
time.sleep(0.5)

print('9. POST empty movie')
post_test = requests.post(service_address + 'movies', json={"movieName": "Solo: A Star Wars Story"})
print(post_test.text)
time.sleep(0.5)

print('10. POST filled movie')
post_test = requests.post(service_address + 'movies', json={
    "movieData": {
        "actors": [{'actor': 'Russell Crowe', 'role': 'Maximus'}],
        "genre": "Action",
        "rating": 8.5,
        "year": 2000
    },
    "movieName": "Gladiator"
})
print(post_test.text)
time.sleep(0.5)

print('11. POST half filled movie')
post_test = requests.post(service_address + 'movies', json={
    "movieData": {
        "rating": 8.9,
        "year": 1994
    },
    "movieName": "Pulp Fiction"
})
print(post_test.text)
time.sleep(0.5)

print('12. PUT movies/Birdman/rating')
put_test = requests.put(service_address + 'movies/Birdman/rating', json={"rating": 10.0})
print(put_test.text)
time.sleep(0.5)

print('13. PUT 400 movies/Birdman/rating')
put_test = requests.put(service_address + 'movies/Birdman/rating', json={"rating": 25.1})
print(put_test.text)
time.sleep(0.5)

print('14. PUT 404 movies/Birdmaan/rating')
put_test = requests.put(service_address + 'movies/Birdmaan/rating', json={"rating": 8.5})
print(put_test.text)
time.sleep(0.5)

print('15. DELETE movies/12%20Angry%20Men/remove')
delete_test = requests.delete(service_address + 'movies/12%20Angry%20Men/remove')
print(delete_test.text)
time.sleep(0.5)

print('16. 404 DELETE movies/13%20Angry%20Men/remove')
delete_test = requests.delete(service_address + 'movies/13%20Angry%20Men/remove')
print(delete_test.text)
time.sleep(0.5)

print('17. GET count/movies')
get_test = requests.get(service_address + 'count/movies')
print(get_test.text)
time.sleep(0.5)

print('18. GET /movies')
get_test = requests.get(service_address + 'movies')
print(get_test.text)
time.sleep(0.5)
