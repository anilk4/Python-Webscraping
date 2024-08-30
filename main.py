from bs4 import BeautifulSoup

# Load the HTML content
with open('home.html', 'r') as html_file:
    content = html_file.read()

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(content, 'lxml')

    # Find the section with id 'services'
    service_section = soup.find('section', id='services')

    if service_section:
        # Find all 'tr' elements within the 'tbody' of the table
        rows = service_section.find('tbody').find_all('tr')

        # Iterate over each row to extract service name and price
        for index, row in enumerate(rows):
            cells = row.find_all('td')
            service_name = cells[0].text.strip()  # First cell: Service name
            price = cells[2].text.strip()  # Third cell: Price
            print(f"{index + 1}. {service_name} : {price}")
    else:
        print("No section with id 'services' found.")
