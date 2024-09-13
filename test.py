import requests
from bs4 import BeautifulSoup
def get_projects_and_stack(username:str):
    URL = 'https://gitflic.ru/search?q='+username
    HTML = requests.get(URL)


    with open('htm.html','w',encoding='utf-8') as file:
        file.write(HTML.text)
    with open('htm.html','r',encoding='utf-8') as file:
        page = file.read()
    soup = BeautifulSoup(page,'html.parser')
    
    data ={}
    
    
    sours_projs_name = soup.find_all('a', class_ ="h6 text-primary font-weight-middle mb-0 mr-2")
    print(sours_projs_name)
    projs_name = []
    for proj in sours_projs_name:
        projs_name.append( proj.text.replace(" ","").replace("\n","").split('/')[-1])
    return projs_name
    
    '''
    user_name = soup.find_all('a', class_ = 'tm-user-info__username')
    title_name = soup.find_all('a',class_='tm-title__link')
    rating = soup.find_all('svg', class_ = 'tm-svg-img tm-votes-meter__icon tm-votes-meter__icon tm-votes-meter__icon_appearance-article')

    
    for i in time:
        Time.append(i.find('time').get('title'))
    for i in user_name:
        User_Name.append(i.text)
    for i in title_name:
        Title_Name.append(i.span.text)
    for i in title_name:
        URL_page.append(i.get('href'))
    for i in rating:
        Rating.append(i.find('title').text)


    Data = []
    for i in range(0,Title_Name.__len__()):
        Data.append({'Автор': User_Name[i],'Статья':Title_Name[i],'Время публикации':Time[i],'Ссылка':'https://habr.com'+URL_page[i],'Рейтинг':Rating[i]})
    '''
get_projects_and_stack('bashilova-2003')   