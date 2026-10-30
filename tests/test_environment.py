def test_analysis_dependencies_are_available():
    import dash
    import mysql.connector
    import pandas
    import requests
    from bs4 import BeautifulSoup

    assert dash.__version__
    assert mysql.connector.__version__
    assert pandas.__version__
    assert requests.__version__
    assert BeautifulSoup
