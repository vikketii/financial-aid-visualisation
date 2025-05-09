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
        "description": """Provider supplement introduced.
        Indexation of annual income limits and euro amounts of recovery of benefits every 2 years.""",
    },
    {
        "year": 2019,
        "description": """Student's parents' income is taken into account as taxable income and the income thresholds are increased""",
    },
    {
        "year": 2020,
        "description": """Provider supplement increased.
        Study grants are increased annually on the basis of the National Pension Index (2020-2022).""",
    },
    {
        "year": 2021,
        "description": """The impact of the Covid-19 epidemic on study conditions is taken into account in the terms of the student loan compensation, student loan tax deduction.
        Meal subsidy increase.""",
    },
    {
        "year": 2022,
        "description": """Student's own income limits affecting study grant will be temporarily increased by 25 % in 2022.""",
    },
    {
        "year": 2023,
        "description": """The income thresholds for student financial aid raised by 50 per cent from the level of 2021.
     Meal subsidy increase.""",
    },
    {
        "year": 2024,
        "description": """No index changes to the level of the study grant in the years 2024-2027.
        Amount of the provider supplement and the amount of the state guarantee of the student loan are increased.""",
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
