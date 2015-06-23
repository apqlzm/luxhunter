# -*- coding: utf-8 -*-
__author__ = 'arturc'
import luxhunter
import argparse
from lxml import etree

def download_ids(session):
    # cityid, postid, serviceid
    main_page_url = 'https://portalpacjenta.luxmed.pl/PatientPortal/'
    ids_url = 'https://portalpacjenta.luxmed.pl/PatientPortal/Home/GetFilter?cityId={}&postId={}&serviceId={}'

    r = session.get(main_page_url)

    parser = etree.HTMLParser()
    tree = etree.fromstring(r.text, parser)

    # (1) extract city names and ids
    cities = dict()
    city_elements = tree.xpath('//select[@id="CityId"]/option[@class=""]')
    for city_element in city_elements:
        city_name = city_element.text
        city_id = city_element.get('value')
        cities[city_name] = city_id

    # (2) for each city get clinic
    clinics = dict()
    for k, v in cities.iteritems():
        # params['cityId'] = v
        ids_new_url = ids_url.format(v, '', '')
        r = session.post(ids_new_url)

        tree = etree.fromstring(r.text, parser)
        clinic_elements = tree.xpath('//select[@id="ClinicId"]/option[@class=""]')

        for clinic_element in clinic_elements:
            clinic_name = clinic_element.text
            clinic_id = clinic_element.get('value')
            clinics[clinic_name] = clinic_id

    # (3) for each clinic in Warsaw get service
    services = dict()
    for k, v in clinics.iteritems():
        ids_new_url = ids_url.format('1', v, '')
        r = session.post(ids_new_url)

        tree = etree.fromstring(r.text, parser)
        service_elements = tree.xpath('//select[@id="ServiceId"]/option[@class=""]')

        for service_element in service_elements:
            service_name = service_element.text
            service_id = service_element.get('value')
            services[service_name] = service_id

    print '*** CITIES ***'
    print dict_to_string(cities)
    print '*** CLINICS ***'
    print dict_to_string(clinics)
    print '*** SERVICES ***'
    print dict_to_string(services)


def dict_to_string(adict):
    out = ''
    for k, v in adict.iteritems():
        out += k + '\t' + v + '\n'
    return out


def main():
    parser = argparse.ArgumentParser(description='Download list of ids from Luxmed website.')
    parser.add_argument('lxlogin', help='Luxmend account login')
    parser.add_argument('lxpass', help='Luxmed account password')
    args = parser.parse_args()

    session = luxhunter.log_in(args.lxlogin, args.lxpass)
    download_ids(session)
    luxhunter.log_out(session)

if __name__ == '__main__':
    main()
