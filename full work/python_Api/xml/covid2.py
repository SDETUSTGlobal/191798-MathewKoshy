import requests
from assertpy import assert_that
from lxml import etree

from config import COVID_TRACKER_HOST
from print_helpers import pretty_print
def test_overall_covid_cases_match_sum_of_total_cases_by_country():
    response = requests.get(f'{COVID_TRACKER_HOST}/api/v1/summary/latest')
    pretty_print(response.headers)

    response_xml = response.text
    xml_tree = etree.fromstring(bytes(response_xml, encoding='utf8'))

    overall_cases = int(xml_tree.xpath("//data/summary/total_cases")[0].text)
    # Another way to specify XPath first and then use to evaluate
    # on an XML tree
    search_for = etree.XPath("//data//regions//total_cases")
    cases_by_country = 0
    for region in search_for(xml_tree):
        cases_by_country += int(region.text)

    assert_that(overall_cases).is_greater_than(cases_by_country)