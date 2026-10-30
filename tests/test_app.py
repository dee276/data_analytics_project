from vie_en_rose_analytics.app import app


def test_dashboard_has_title_and_description():
    children = app.layout.children

    assert children[0].children == "Analyse de données — La Vie en Rose"
    assert children[1].children == (
        "Notre tableau de bord de vente et d'analyse financière."
    )
