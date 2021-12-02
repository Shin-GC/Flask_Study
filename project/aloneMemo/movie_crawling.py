import requests
from bs4 import BeautifulSoup


def crawling(movie_name):
    doc = {}
    url = 'https://movie.naver.com/movie/search/result.naver?section=movie&query='
    url += movie_name

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    movie_list = soup.select('#old_content > ul.search_list_1> li')
    for movie in movie_list:
        title = movie.select_one('dl > dt > a')
        link = f"https://movie.naver.com{movie.select_one('p > a')['href']}"

        detail_data = requests.get(link, headers=headers)
        detail_soup = BeautifulSoup(detail_data.text, 'html.parser')

        og_image = detail_soup.select_one('meta[property="og:image"]')['content']
        og_desc = detail_soup.select_one('meta[property="og:description"]')['content']

        give_title = title.text
        give_img = og_image
        give_desc = og_desc
        give_link = link

        doc = {
            'title': give_title,
            'img': give_img,
            'desc': give_desc,
            'link': give_link,
        }
    return doc


def crawling_one(movie_name):
    doc = {}
    url = 'https://movie.naver.com/movie/search/result.naver?section=movie&query='
    url += movie_name

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    link = soup.select_one('#old_content > ul.search_list_1 > li:nth-child(1) > p > a')['href']
    add_url = 'https://movie.naver.com'
    link = add_url + link

    data = requests.get(link, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    og_title = soup.select_one('meta[property="og:title"]')['content']
    og_image = soup.select_one('meta[property="og:image"]')['content']
    og_desc = soup.select_one('meta[property="og:description"]')['content']

    doc = {
        'title': og_title,
        'og_image': og_image,
        'og_desc': og_desc,
        'url': link,
    }
    return doc


