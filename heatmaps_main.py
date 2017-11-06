"""
Heat maps modules
"""

# Third-party libraries import
import pandas as pd
import pygal
import plotly as ply
import webbrowser

# Custom modules import
import main as parent


def main(data):
    """ Main function with data """
    print("\n*****  Heat maps chart categories  *****")
    print("1) Heat map by countries")
    print("""Type "BACK" return to main menu""")
    print("""Type "EXIT" to terminate program""")

    choice = input("Type number of chart which you want : ")

    if choice.lower() == "exit":
        parent.do_exit()
    if choice.lower() == "back":
        parent.menu_main()

    choice = int(choice)

    if choice == 1:
        map_country(data)


def map_country(data):
    """ Generate heatmaps by plotly """
    country_name = list(
        ['Afghanistan', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antigua and Barbuda',
         'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas, The', 'Bahrain', 'Bangladesh',
         'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina',
         'Botswana', 'Brazil', 'British Virgin Islands', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burma', 'Burundi',
         'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile',
         'China', 'Colombia', 'Comoros', 'Congo, Democratic Republic of the', 'Congo, Republic of the', 'Cook Islands',
         'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Curacao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti',
         'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia',
         'Ethiopia', 'Falkland Islands (Islas Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France',
         'French Polynesia',
         'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guam',
         'Guatemala', 'Guernsey', 'Guinea-Bissau', 'Guinea', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong', 'Hungary',
         'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica',
         'Japan',
         'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 'Kosovo', 'Kuwait',
         'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania',
         'Luxembourg', 'Macau', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta',
         'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia, Federated States of', 'Moldova',
         'Monaco',
         'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Namibia', 'Nepal', 'Netherlands', 'New Caledonia',
         'New Zealand', 'Nicaragua', 'Nigeria', 'Niger', 'Niue', 'Northern Mariana Islands', 'Norway', 'Oman',
         'Pakistan',
         'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto Rico',
         'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin',
         'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino',
         'Sao Tome and Principe',
         'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten', 'Slovakia',
         'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan',
         'Suriname',
         'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste',
         'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine',
         'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela',
         'Vietnam', 'Virgin Islands', 'West Bank', 'Yemen', 'Zambia', 'Zimbabwe'])  # Country names
    country_code = list(
        ['AFG', 'ALB', 'DZA', 'ASM', 'AND', 'AGO', 'AIA', 'ATG', 'ARG', 'ARM', 'ABW', 'AUS', 'AUT', 'AZE', 'BHM', 'BHR',
         'BGD', 'BRB', 'BLR', 'BEL', 'BLZ', 'BEN', 'BMU', 'BTN', 'BOL', 'BIH', 'BWA', 'BRA', 'VGB', 'BRN', 'BGR', 'BFA',
         'MMR', 'BDI', 'CPV', 'KHM', 'CMR', 'CAN', 'CYM', 'CAF', 'TCD', 'CHL', 'CHN', 'COL', 'COM', 'COD', 'COG', 'COK',
         'CRI', 'CIV', 'HRV', 'CUB', 'CUW', 'CYP', 'CZE', 'DNK', 'DJI', 'DMA', 'DOM', 'ECU', 'EGY', 'SLV', 'GNQ', 'ERI',
         'EST', 'ETH', 'FLK', 'FRO', 'FJI', 'FIN', 'FRA', 'PYF', 'GAB', 'GMB', 'GEO', 'DEU', 'GHA', 'GIB', 'GRC', 'GRL',
         'GRD', 'GUM', 'GTM', 'GGY', 'GNB', 'GIN', 'GUY', 'HTI', 'HND', 'HKG', 'HUN', 'ISL', 'IND', 'IDN', 'IRN', 'IRQ',
         'IRL', 'IMN', 'ISR', 'ITA', 'JAM', 'JPN', 'JEY', 'JOR', 'KAZ', 'KEN', 'KIR', 'KOR', 'PRK', 'KSV', 'KWT', 'KGZ',
         'LAO', 'LVA', 'LBN', 'LSO', 'LBR', 'LBY', 'LIE', 'LTU', 'LUX', 'MAC', 'MKD', 'MDG', 'MWI', 'MYS', 'MDV', 'MLI',
         'MLT', 'MHL', 'MRT', 'MUS', 'MEX', 'FSM', 'MDA', 'MCO', 'MNG', 'MNE', 'MAR', 'MOZ', 'NAM', 'NPL', 'NLD', 'NCL',
         'NZL', 'NIC', 'NGA', 'NER', 'NIU', 'MNP', 'NOR', 'OMN', 'PAK', 'PLW', 'PAN', 'PNG', 'PRY', 'PER', 'PHL', 'POL',
         'PRT', 'PRI', 'QAT', 'ROU', 'RUS', 'RWA', 'KNA', 'LCA', 'MAF', 'SPM', 'VCT', 'WSM', 'SMR', 'STP', 'SAU', 'SEN',
         'SRB', 'SYC', 'SLE', 'SGP', 'SXM', 'SVK', 'SVN', 'SLB', 'SOM', 'ZAF', 'SSD', 'ESP', 'LKA', 'SDN', 'SUR', 'SWZ',
         'SWE', 'CHE', 'SYR', 'TWN', 'TJK', 'TZA', 'THA', 'TLS', 'TGO', 'TON', 'TTO', 'TUN', 'TUR', 'TKM', 'TUV', 'UGA',
         'UKR', 'ARE', 'GBR', 'USA', 'URY', 'UZB', 'VUT', 'VEN', 'VNM', 'VGB', 'WBG', 'YEM', 'ZMB',
         'ZWE'])  # Country Codes

    result = pd.DataFrame(country_name, country_code)
    result.reset_index(inplace=True)
    result.columns = [['Code', 'Country']]
    country = data.groupby('country_txt')['iyear'].count().to_frame()
    country = country.merge(result, left_index=True, right_on='Country', how='left')
    country.columns = [['Activities', 'Code', 'Country']]

    data = [dict(
        type='choropleth',
        autocolorscale=False,
        colorscale='Viridis',
        reversescale=True,
        showscale=True,
        locations=country['Code'],
        z=country['Activities'],
        locationmode='Code',
        text=country['Country'].unique(),
        marker=dict(
            line=dict(color='rgb(200,200,200)', width=0.5)),
        colorbar=dict(autotick=True, tickprefix='',
                      title='Activities')
    )
    ]

    layout = dict(
        title='Terrorist Activities By Country',
        geo=dict(
            showframe=True,
            showocean=True,
            oceancolor='rgb(0,255,255)',
            projection=dict(
                type='Mercator',

            ),
        ),
    )
    fig = dict(data=data, layout=layout)
    ply.offline.iplot(fig, validate=False, filename='worldmap')

    print("Map generated!")
    print("Opening map...\n")
    url = "https://psit.wiput.me/map"
    webbrowser.open(url, new=2)

    main(data)
