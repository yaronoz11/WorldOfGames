from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def test_scores_service(url):
    """
    Function to check the score element of the webpage and ensure it's a number between 1 and 1000.

    Args:
        url (str): The URL of the page to test.

    Returns:
        bool: True if the score is a valid number between 1 and 1000, False otherwise.
    """
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        driver.get(url)

        try:
            score_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "score"))
            )

            score_value = score_element.text
            print(f"DEBUG: Found score text: {score_value}")

            # Extract the score value from the text
            try:
                score = int(score_value.split(":")[1].strip())
                print(f"DEBUG: Parsed score: {score}")


                if 1 <= score <= 1000:
                    return True
                else:
                    return False
            except ValueError:
                print(f"DEBUG: Failed to parse score from text: {score_value}")
                return False

        except Exception as e:
            print(f"Error: Could not find the element 'score'. Exception: {e}")
            return False

    finally:
        driver.quit()


def main_function(url):

    """
    The main function will return -1 as an OS exit
    code if the tests failed and 0 if they passed.
    """

    if test_scores_service(url):
        print("Test passed: The score is valid!")
        return 0  # Return 0 if the score is valid
    else:
        print("Test failed: The score is not valid.")
        return -1  # Return -1 if the score is invalid



if __name__ == "__main__":
    url = "http://127.0.0.1:8777/score"
    exit_code = main_function(url)
    print(f"Exit code: {exit_code}")
