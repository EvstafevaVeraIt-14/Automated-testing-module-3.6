import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_button_add_to_basket_is_present(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    
    browser.get(link)
    time.sleep(30)
    
    try:
        button = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket"))
        )
        
        assert button.is_displayed(), "Кнопка добавления в корзину не найдена!"
        print(f"\nТекст на кнопке: '{button.text}'")
        
    except Exception as e:
        print(f"\nНе удалось найти кнопку. Ошибка: {e}")
        browser.save_screenshot("error_screenshot.png") 
        raise