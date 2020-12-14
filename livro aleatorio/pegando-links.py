from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome(r'chromedriver.exe') as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.amazon.com.br/gp/bestsellers/books/")

    wait = WebDriverWait(driver, 10)

    aPaginas = driver.find_elements_by_xpath('//*[@id="zg_browseRoot"]/ul/ul/li/a')

    linksPaginas = []
    links = linksPaginas

    for i in range(len(aPaginas)):
        linksPaginas.append(aPaginas[i].get_attribute('href'))

    for i in range(len(linksPaginas)):
        driver.get(linksPaginas[i])

        a = driver.find_elements_by_xpath('//*[@id="zg-center-div"]/div[2]/div/ul/li[3]/a')

        for i in range(len(a)):
            links.append(a[i].get_attribute('href'))

    livros = []
    for i in range(len(links)):
        driver.get(links[i])

        aLivros = driver.find_elements_by_xpath('//*[@id="zg-ordered-list"]/li/span/div/span/a')

        for i in range(len(aLivros)):
            livros.append(aLivros[i].get_attribute('href'))


    print(livros)
