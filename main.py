import json
import hashlib

fail_txt = 'liks.txt'
fail_json = 'countries.json'
link_wiki = 'https://ru.wikipedia.org/wiki/'

class Wikipedia:
    def __iter__(self):
        return self

    def __init__(self,fail_json):
        with open(fail_json) as fail:
            country_json = json.load(fail)
            country_names = (country['name']['common'] for country in country_json)
            self.country_names_iter=iter(country_names)

# формирует ссылку
    def get_link(self,country_names):
        link_wikis = f"{link_wiki}{country_names}"
        return link_wikis

# Вывод страна - ссылка
    def __next__(self):
        country = next(self.country_names_iter)
        country_name_link = f'{country} - {self.get_link(country)}'
        return country_name_link

def get_hash(file_path):
    with open(file_path) as file:
        for line in file:
            yield hashlib.md5(line.encode()).hexdigest()

# Запись в файл
with open(fail_txt, 'w',  encoding= 'utf-8') as f:
    for country_name_links in Wikipedia(fail_json):
        f.write(f'{country_name_links}\n')

# При каждой итерации возвращает md5 хеш каждой строки файла
for hash_str in get_hash(fail_txt):
    print(hash_str)
