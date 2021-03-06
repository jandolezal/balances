# Bioenergy in Energy balances

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jandolezal/balances/main)

Getting few information on bioenergy from Eurostat's [Energy balances](https://ec.europa.eu/eurostat/web/energy/data/energy-balances) database.

Jupyter notebooks parsing xlsb files from zip files for 2020 and 2021 editions and producing csv exports for selected variables to be used elsewhere.

Directory `eu` for whole EU, `selection` for AT, CZ, DK, NL, PL, SK.

Variables covered:
* Primary production
* Imports
* Exports
* Gross inland consumption
* Energy dependency (computed as Imports-Exports/Gross inland consumption, see Bioenegy Europe's [Bioenergy Landscape](https://bioenergyeurope.org/statistical-report.html)).

Fuels covered:
* Primary solid biofuels
* Biogases
* Liquid biofuels
* Renewable municipal waste
* Renewables and biofuels
