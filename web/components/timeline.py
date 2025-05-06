import dash_bootstrap_components as dbc
from dash import html

timeline_data = [
    # {
    #     "year": 2015,
    #     "description": """Opintolainan korkojen verovähennysoikeuden poistaminen 2015 alkaen. Opintorahan vuosittainen indeksikorotus 1.8.2015.""",
    # },
    # {"year": 2016, "description": """-"""},
    # {
    #     "year": 2017,
    #     "description": """Suomessa vuokralla asuvat opiskelijat yleisen asumistuen piiriin.
    #     Korkeakouluopiskelijoiden opintorahojen pienentäminen toisen asteen tasolle.
    #     Opintolainan kuukausimäärän korottaminen 400:sta 650 euroon. Kokonaistukiaika lyhentyy 64:stä 54 tukikuukauteen.""",
    # },
    {
        "year": 2018,
        "description": """Opintorahan huoltajakorotus.
        Vuositulorajojen ja takaisinperinnän euromäärien indeksikorotukset 2 vuoden välein.""",
    },
    {"year": 2019, "description": """Opintorahan oppimateriaalilisä"""},
    {"year": 2020, "description": """"""},
    {
        "year": 2021,
        "description": """Koronaepidemian aiheuttamia lievennyksiä opintojen edistymiseen liittyviin ehotihin.
        Korkeakouluopiskelijan ateriatuki suureni 1,94 eurosta 2,30 euroon.""",
    },
    {"year": 2022, "description": """-"""},
    {"year": 2023, "description": """-"""},
    {
        "year": 2024,
        "description": """Opintorahan indeksikorotusten jäädytys 2024-2027.""",
    },
]


def create_timeline():
    timeline = html.Div(
        [
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        item["description"], title=item["year"], item_id=item["year"]
                    )
                    for item in timeline_data
                ],
                id="timeline",
                active_item=timeline_data[0]["year"],
            ),
            html.Div(id="timeline-contents", className="mt-3"),
        ]
    )

    return timeline
