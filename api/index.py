# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def home():
    
#     #return 'Hello, World!'
#     with open('link.txt', 'r', encoding='utf-8') as file:
#         links = file.readlines()
#     return links

# @app.route('/about')
# def about():
#     return 'About'



import time
import schedule
from selenium import webdriver
import time
import re
from selenium.webdriver.chrome.options import Options
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def display_links():
    with open('link.txt', 'r', encoding='utf-8') as file:
        links = file.readlines()
    return render_template('display_links.html', links=links)


def python_scrap():
    global driver
    
    # Create Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # This line makes Chrome run in headless mode

    url = "https://www.real.discount/udemy-coupon-code/"

    # Initialize a webdriver (e.g., Chrome)
    driver = webdriver.Chrome( options=chrome_options)

    # Navigate to the URL
    driver.get(url)

    # Wait for the page to load completely (you can adjust the time as needed)
    driver.implicitly_wait(10)

    # Wait for an additional 10 minutes
    time.sleep(5)

    # Get the content after JavaScript execution
    dynamic_content = driver.page_source
    # Save dynamic_content to a text file
    with open('text.txt', 'w', encoding='utf-8') as file:
        file.write(dynamic_content)

    # Close the browser
    driver.quit()

    # Part 1: Extract links from html.txt and write to link.txt
    with open('text.txt', 'r', encoding='utf-8') as file:
        html_content = file.read()

    matches = re.findall(r'<a.*?href=[\'"](.*?/offer/.*?)["\']', html_content)

    with open('text.txt', 'w', encoding='utf-8') as file:
        for match in matches:
            file.write(match + '\n')

    # Part 2: Remove '/offer/`+ item[' from link.txt
    with open('text.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    cleaned_links = [line.replace('/offer/`+ item[', '') for line in lines]

    with open('text.txt', 'w', encoding='utf-8') as file:
        file.writelines(cleaned_links)

    # Read links from link.txt
    with open('text.txt', 'r', encoding='utf-8') as file:
        links = file.readlines()

    # Initialize a webdriver (e.g., Chrome)
    
    driver = webdriver.Chrome( options=chrome_options)


    all_contant = ''  # Initialize all_contant before the loop

    for url in links:
        # Construct the full URL
        full_url = "https://www.real.discount/" + url.strip()

        # Navigate to the URL
        driver.get(full_url)

        # Wait for the page to load completely (you can adjust the time as needed)
        driver.implicitly_wait(10)

        # Wait for an additional 3 seconds (if needed)
        time.sleep(3)

        # Get the content after JavaScript execution
        dynamic_content = driver.page_source
        all_contant += dynamic_content  # Concatenate the dynamic content

    with open('text.txt', 'w', encoding='utf-8') as file:
        file.write(all_contant + '\n')

    # Close the browser
    driver.quit()


    # the udlink.py which is use to join remaining link with /offer/ and jump to course link and extract each html page ######################

    # Part 1: Extract links from html.txt and write to link.txt
    with open('text.txt', 'r', encoding='utf-8') as file:
        html_content = file.read()


    
    matches = re.findall(r'<a.*?href=[\'"](.*?udemy.com/course.*?)["\']', html_content)

    
   
       # Part 1: Write cleaned links to link.txt
    with open('link.txt', 'a', encoding='utf-8') as file:
        for match in matches:
            # Remove text before "https://www.udemy.com/course"
            cleaned_match = re.sub(r'^.*https://www.udemy.com/course', 'https://www.udemy.com/course', match)
            # Convert to set to remove duplicates, then back to string
            file.write(cleaned_match + '\n')

    #the udlink.py which is use to extract udemy.com main course link for last sand link ends here #######################################



def python_try():
    
    def send_email(links, lines):
        lines_list = '\n'.join([f'<li>{line}</li>' for line in lines])
        links_list = '\n'.join([f'<li>{link}</li>' for link in links])

        html = f'''
            <h2>All Links:</h2>
            <ul>
                {lines_list}
            </ul>

            <h2>Interested Links:</h2>
            <ul>
                {links_list}
            </ul>
        '''

        sender_email = "hammadirshad305@outlook.com"
        receiver_emails = maillist

        message = MIMEMultipart()
        message['From'] = 'hammad irshad <hammadirshad305@outlook.com>'
        message['To'] = ', '.join(receiver_emails)
        message['Subject'] = 'Udemy coupon sender python'

        message.attach(MIMEText(html, 'html'))

        try:
            smtp_server = smtplib.SMTP('smtp.office365.com', 587)
            smtp_server.starttls()
            smtp_server.login(sender_email, 'tgyfajllloxuuuim')
            smtp_server.sendmail(sender_email, receiver_emails, message.as_string())
            smtp_server.quit()
            print("Message sent successfully")
        except Exception as e:
            print(f"Error sending email: {e}")


    # Initialize an empty list to store links
    links = []
    # Initialize an empty list to store lines
    lines = []
    temp = []

    # Define the list of email addresses
    maillist = [
        
        'hammadirshad23@gmail.com',
        'iqna2018@gmail.com',
    ]

    
    # Read the contents of text.txt
    with open('link.txt', 'r') as file:
        data = file.read()
        lines = list(set(data.split('\n')))
        # unique_lines = list(set(lines))
        # test = '\n'.join(unique_lines)
        # print('\n\ndata'+ data +'\n\n')
        # print('\n\ntest'+ test +'\n\n')

        # lines = test.strip()
        # lines = lines[1:] if lines.startswith('\n') else lines


        with open('temp.txt', 'r') as word_file:
            word = word_file.read()
            temp = word.split('\n')

            # Split the file content into an array of lines
            #lines = data.split('\n')
            print('\nword\n'+ word +'\n')
            print('\ndata\n'+ data +'\n')
            # Iterate through the lines
            for line in lines:
                if any(keyword in line for keyword in ['php', 'python', 'google', 'aws', 'azure', 'scrap', 'bootcamp', 
                                                       'js', 'language', 'microsoft', 'learn', 'react', 'gcp', 'project', 'learning'
                                                       'data','ielts','toefl','jquery','training'
                                                       ]):
                    links.append(line.strip())  # Strip to remove any extra spaces
            
            print("interested\n" + str(links))
            # If there are links, send an email

            if word != data:
                print("send email run")
                send_email(links, lines)

            with open('temp.txt', 'w') as temp_file:
                for line in lines:
                    # Check if line is not empty and does not start with a newline character
                    if line and not line.startswith('\n'):
                        temp_file.write(line + '\n')

            with open('link.txt', 'w') as temp_file:
                temp_file.write('')
                print("Data written to file successfully.")





def main():
    try:
        python_scrap()
        python_try()
        print("main run")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    try:
        # Schedule python_scrap() every 5 minutes
        schedule.every(0.1).minutes.do(python_scrap)

        # Schedule python_try() every 15 minutes
        schedule.every(15).minutes.do(python_try)

         # Start Flask app in a separate thread
        from threading import Thread
        Thread(target=app.run, kwargs={'debug': False, 'use_reloader': False}).start()

        while True:
            schedule.run_pending()
            time.sleep(1)
    except Exception as e:
        print(e)
