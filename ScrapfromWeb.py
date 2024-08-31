from bs4 import BeautifulSoup
import requests
import time

print('Put some skill that you are not familiar with:')
unfamiliar_skill = input('>')
print(f'Filtering out jobs that require {unfamiliar_skill}...')


def find_jobs():
    html_text = requests.get(
        "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=Python&txtKeywords=Python&txtLocation=").text

    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    found_job = False  # To track if any job is found
    for job in jobs:
        pub_date = job.find('span', class_='sim-posted').span.text
        if 'few' in pub_date:
            company_name = job.find('h3', class_='joblist-comp-name').text
            skills = job.find('span', class_='srp-skills').text.lower()
            more_info = job.header.h2.a['href']
            if unfamiliar_skill.lower() not in skills:

                print(f'Company Name: {company_name.strip()}')
                print(f'Skills: {skills.strip()}')
                print(f'Link to job: {more_info}')
                print('')

                found_job = True

    if not found_job:
        print('No job found')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        time.sleep(time_wait * 60)
        print(f'Waiting{time_wait} minutes...')

"""
Explanation:

1. `from bs4 import BeautifulSoup`: Imports the BeautifulSoup class from the `bs4` module, which is used for parsing HTML and XML documents.
2. `import requests`: Imports the `requests` library, which is used to make HTTP requests in Python.
3. `import time`: Imports the `time` module, which provides various time-related functions, such as sleeping for a specified duration.

4. `print('Put some skill that you are not familiar with:')`: Prints a message asking the user to input a skill they are not familiar with.
5. `unfamiliar_skill = input('>')`: Captures the user input and stores it in the variable `unfamiliar_skill`.
6. `print(f'Filtering out jobs that require {unfamiliar_skill}...')`: Prints a message indicating that the script will filter out jobs requiring the specified skill.

7. `def find_jobs():`: Defines a function called `find_jobs`, which will search for jobs and filter out those that require the unfamiliar skill.
8. `html_text = requests.get(...)`: Sends an HTTP GET request to the TimesJobs website to search for Python jobs. The returned HTML content is stored in the `html_text` variable.
9. `soup = BeautifulSoup(html_text, 'lxml')`: Parses the HTML content using the BeautifulSoup library with the 'lxml' parser and stores it in the `soup` variable.
10. `jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')`: Finds all job postings on the page that match the specified HTML structure and stores them in the `jobs` list.

11. `found_job = False`: Initializes a flag variable `found_job` to `False`, which will be used to check if any suitable jobs are found.
12. `for job in jobs:`: Loops through each job posting found on the page.
13. `pub_date = job.find('span', class_='sim-posted').span.text`: Extracts the publication date of the job posting.
14. `if 'few' in pub_date:`: Checks if the job was posted recently (indicated by the word 'few' in the publication date).
15. `company_name = job.find('h3', class_='joblist-comp-name').text`: Extracts the company name from the job posting.
16. `skills = job.find('span', class_='srp-skills').text.lower()`: Extracts the skills required for the job and converts the text to lowercase for easier comparison.
17. `more_info = job.header.h2.a['href']`: Extracts the URL of the job posting.
18. `if unfamiliar_skill.lower() not in skills:`: Checks if the unfamiliar skill is not in the required skills list.

19. `print(f'Company Name: {company_name.strip()}')`: Prints the company name after stripping any extra spaces.
20. `print(f'Skills: {skills.strip()}')`: Prints the required skills after stripping any extra spaces.
21. `print(f'Link to job: {more_info}')`: Prints the URL to the job posting.
22. `print('')`: Adds a blank line for better readability.

23. `found_job = True`: Sets the `found_job` flag to `True`, indicating that a suitable job was found.

24. `if not found_job:`: If no suitable job was found, prints "No job found".

25. `if __name__ == '__main__':`: Ensures that the following code runs only if the script is executed directly (not when imported as a module).
26. `while True:`: Creates an infinite loop that will continuously search for jobs at specified intervals.
27. `find_jobs()`: Calls the `find_jobs` function to search for jobs.
28. `time_wait = 10`: Sets the waiting time between searches to 10 minutes.
29. `time.sleep(time_wait * 60)`: Pauses the script for `time_wait` minutes before searching for jobs again.
30. `print(f'Waiting {time_wait} seconds...')`: Prints a message indicating how long the script will wait before the next job search.
"""
