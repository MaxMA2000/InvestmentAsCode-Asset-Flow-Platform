echo "starting Superset"
# superset db upgrade
export FLASK_APP=superset
export SUPERSET_CONFIG_PATH=/Users/maxma/Desktop/InvestmentAsCode-Master-Repo/InvestmentAsCode-Asset-Flow-Platform/platform/local/superset_config.py
# superset fab create-admin
# superset init


superset run -p 8088 --with-threads --reload --debugger

# http://localhost:8088
# username: admin
# password: admin

# M1 Installation Guide: https://www.restack.io/docs/superset-knowledge-apache-superset-mac-m1-guide
# Official Installation: https://superset.apache.org/docs/installation/installing-superset-from-pypi

