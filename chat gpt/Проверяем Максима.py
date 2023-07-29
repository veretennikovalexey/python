import requests
from bs4 import BeautifulSoup

url = "https://pk.mpei.ru/inform/list581bacc.html"
response = requests.get(url)
if response.status_code == 200:
    print(f"Запрос выполнен успешно (код {response.status_code})")
    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.title
    print(title.text)

    # Поиск всех тегов tr
    tr_tags = soup.find_all('tr')

    # Перебираем найденные теги tr
    for tr_tag in tr_tags:
        # Проверяем наличие атрибута id и его значение
        if 'id' in tr_tag.attrs and tr_tag['id'] == 'p123473':
            # Выводим на экран тег tr, удовлетворяющий условию
            print(tr_tag)

            print("acceptedPoint - значит мы в списке:", tr_tag['class'])
