import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def get_test_text(driver: webdriver.Chrome) -> str:
    text_div = driver.find_element(By.ID, "testText")
    text = "".join([div.text for div in text_div.find_elements(By.TAG_NAME, "div")])
    return text


if __name__ == "__main__":
    # Если вам нужен сертификат укажите путь к вашиму профилю Google, чтобы вебдрайвер использовал ваш аккаунт
    # Приблизительный путь: C:\Users\[Ваш пользователь]\AppData\Local\Google\Chrome\User Data
    # Убедитесь что ваш аккаунт не используется в данный момент во избежания ошибок
    user_path = r"C:\Users\s-and\AppData\Local\Google\Chrome\User Data"
    # --------------------------------------------------------------------------------------------------------

    root_url = "https://www.ratatype.com/ru/typing-test/"   # Ссылка на сайт
    language = "en"                                         # Установка языка
    root_url_with_language = f"{root_url}{language}/"       # Готовая ссылка с выбранным языком

    print("Скрипт написал XsSandreiSsX🔥",
          "Github: https://github.com/XsSandreiSsX", sep="\n")
    # Инициализация вебдрайвера
    options = webdriver.ChromeOptions()
    if user_path:
        options.add_argument(f"user-data-dir={user_path}")
    with webdriver.Chrome(options=options) as driver:
        driver.get(root_url_with_language)
        sleep(5)

        # Находим куда вводить текст
        text_input = driver.find_element(By.ID, "virtualInput")

        # Начинаем скоростной тест :>
        while True:
            try:
                test_text = get_test_text(driver)
                for letter in test_text:
                    text_input.send_keys(letter)
                    sleep(0.02)  # Если без задержки не дает закончить
            except selenium.common.exceptions.StaleElementReferenceException:
                break

        # Время для скачивания сертификата
        sleep(60)
