import requests
from bs4 import BeautifulSoup as bs
import re

cbsa_index = 0  # Initializing the index to run through each CBSA request




state_fips = ['MD24&state=DC11&state=VA51&state=WV54',
                'FL12',
                'PA42&state=NJ34&state=DE10&state=MD24',
                'WA53',
                'GA13',
                'MD24',
                'MA25&state=NH33',
                'NY36',
                'VA51',
                'IL17&state=IN18&state=WI55',
                'CO8',
                'MI26',
                'MO29&state=KS20',
                'TX48',
                'HI15',
                'CA6',
                'CA6',
                'AL1',
                'CA6',
                'CA6',
                'MO29&state=IL17',
                'WI55',
                'PA42',
                'AZ4']
#DC, Miami, Philly, Seattle, Atlanta, Baltimore, Boston, Buffalo, Charlottesville  Chicago   Denver   Detroit    KC       Austin    Honolulu   San Fran   San Jose    Huntsville  Sacramento  San Diego  St Louis  Milwaukee
cbsa_code = ['47900',
                '33100',
                '37980',
                '42660',
                '12060',
                '12580',
                '14460',
                '15380',
                '16820',
                '16980',
                '19740',
                '19820',
                '28140',
                '12420',
                '46520',
                '41860',
                '41940',
                '26620',
                '40900',
                '41740',
                '41180',
                '33340']

for state_index in range(len(state_fips)):
    current_state_fips = state_fips[cbsa_index]
    current_cbsa_code = cbsa_code[cbsa_index]
    print('Requesting: '+current_cbsa_code+'...')
    #base_request = "http://mcdc.missouri.edu/cgi-bin/broker?_PROGRAM=websas.geocorr14.sas&_SERVICE=bigtime&site=OSEDA/MCDC/Univ.ofMissouri&state=%s&g1_=cbsa10&g2_=tract&wtvar=pop10&nozerob=1&csvout=1&listout=1&lstfmt=html&namoptf=b&namoptr=b&title=&counties=&metros=%s&places=&distance=&y0lat=&x0long=&locname=&nrings=&r1=&r2=&r3=&r4=&r5=&r6=&r7=&r8=&r9=&r10=&lathi=&latlo=&longhi=&longlo=&_DEBUG=0"%(current_state_fips,current_cbsa_code)
    base_request = "http://mcdc.missouri.edu/cgi-bin/broker?_PROGRAM=websas.geocorr14.sas&_SERVICE=bigtime&site=OSEDA/MCDC/Univ.ofMissouri&state=%s&g1_=cbsa10&g2_=state&g2_=tract&g2_=zcta5&g2_=ur&g2_=ua&g2_=puma12&g2_=metdiv10&wtvar=pop10&nozerob=1&csvout=1&listout=1&lstfmt=html&namoptf=b&namoptr=b&title=&counties=&metros=%s&places=&distance=&y0lat=&x0long=&locname=&nrings=&r1=&r2=&r3=&r4=&r5=&r6=&r7=&r8=&r9=&r10=&lathi=&latlo=&longhi=&longlo=&_DEBUG=0"%(current_state_fips,current_cbsa_code)
    final_csv_file_name = 'CBSA_'+current_cbsa_code+'.csv'
    response = requests.get(base_request)
    print(response)
    response_soup = bs(response.text,'lxml')
    all_links = response_soup.find_all('a',href=True)
    csv_link = str(all_links[1])

    find_to_period = re.compile(r"^([^.g]*).*")
    re_results_to_period = re.match(find_to_period,csv_link)
    re_results=re_results_to_period.group(1)

    file_number = []
    for letter in range(len(re_results)):
        if letter > 19:
            file_number.append(re_results[letter])
    file_number_string = ''.join(file_number)
    csv_base_url = 'http://mcdc.missouri.edu/tmpscratch/%s.geocorr14/geocorr14.csv'%(file_number_string)
    print('\n\n...\n\n')
    print(csv_base_url)
    csv_response = requests.get(csv_base_url)
    with open(final_csv_file_name,'wb') as out_file:
        out_file.write(csv_response.content)
    cbsa_index+=1
