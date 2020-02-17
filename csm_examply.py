import requests
from bs4 import BeautifulSoup
import ipdb;


def get_years(spage):
    # Use BeautifulSoup to pull all the Years out of source page
    years = [option['value'] for option in spage.find(id='fiscalYearSelect')]
    return years

def get_departments(spage):
    # Use BeautifulSoup to pull all the Departments out out of source page
    # it looks to be keyed off an ID numbe when it sends the next AJAX reques
    departments = [[option['value'], option.text.strip()] for option in spage.find("select", {"name":"aid"})]
    return departments # format: [['1', 'Name of Department 1'], ['2', 'Name of Department 2'], ...]

def get_data(url, year, job_department, job_class='', job_name=''):
    data = {
    'fy': year,
    'aid': job_department,
    'class': job_class,
    'name': job_name
    }
    response = requests.post(url, data=data)
    response_table = BeautifulSoup(response.text, 'html.parser')
    # This gives us our results; data is in an HTML tale under, id='sortableTable;
    table_rows = response_table.find(id='sortableTable').find_all('tr')
    data = []
    # Iterate over all trs in table extracting the data.  As of when i was looking, the headers looked like this..
    # <tr>
    #               <th>Year</th>
    #               <th>Name</th>
    #               <th>Gender</th>
    #               <th>Agency</th>
    #               <th>City/County</th>
    #               <th>Class</th>
    #               <th>Salary1</th>
    #               <th>Salary2</th>
    #               <th>Travel</th>
    #           </tr>
    for tr in table_rows:
        data.append([tr.text.strip() for tr in tr.find_all('td')])
    # Just return all value out as a list of lists; I assume you want it in a dataframe or something?
    # Current:
    # data = [['2004', 'WICHTENDAHL BETH A.', 'F', 'AUDITOR OF STATE', 'LINN', 'ASST AUDITOR 2', '1,688.00 BW', '43,607.20', '2,789.95'],
    #         ['2004', 'WIDEN CORINNE M', 'F', 'AUDITOR OF STATE', 'POLK', 'ASST AUDITOR 1', '1,348.00 BW', '34,272.90', '3,877.92'],
    #         ...,]
    return data


def main():
    weburl = 'https://www.legis.iowa.gov/publications/fiscal/salaryBook'
    page = requests.get(weburl)
    years = get_years(BeautifulSoup(page.text, 'html.parser'))
    print(years)
    departments = get_departments(BeautifulSoup(page.text, 'html.parser'))
    print(departments)
    # Short example
    table = get_data(weburl, 2004, 126)
    print(table)
    # # Iterate over all years and all departments, like...
    # for year in years:
    #     for department in department:
    #         # Not sure how you want to handle this so...
    #         data.append(get_data(weburl, year, department[0])) # department 0 as it's keyed off the ID #, not the name

if __name__ == "__main__":
    main()
