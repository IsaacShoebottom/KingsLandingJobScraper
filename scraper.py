import time
import urllib.request
import urllib.error

from bs4 import BeautifulSoup


# Made for a friend with love
# Tested with Python 3.10.7 on Windows 10

def scrape():
    contents = urllib.request.urlopen("https://kingslanding.nb.ca/employment/").read()
    soup = BeautifulSoup(contents, "html.parser")

    # Other ways to parse the HTML to check for differences

    # div_id = "wrapper"
    # whole_page = soup.find("div", {"id": div_id})

    # main_id = "main"
    # main_content = whole_page.find("main", {"id": main_id})

    text_id = "content-holder"
    text_content = soup.find("div", {"class": text_id})

    return text_content.text


if __name__ == '__main__':
    # start = time.time()

    # 60 seconds * 60 minutes * 3 hours
    timer = 60 * 60 * 3
    text = scrape()
    print("Started checking for new jobs, will check every 3 hours.")

    while True:
        try:
            tmp = scrape()
            if text != tmp:
                print("New job posting! Here's the text:")
                print(tmp)
                print("And here's the link: https://kingslanding.nb.ca/employment/")
                print("Do you want to keep checking? (y/n): ", end="")
                choice = input()
                if choice == "n" or choice == "N":
                    break
                else:
                    text = tmp
        except urllib.error.URLError as err:
            print("An error occurred when scraping: {}".format(err.reason))

        except Exception as err:
            print("An unknown error has occurred: {}".format(err))

        finally:
            time.sleep(timer)
