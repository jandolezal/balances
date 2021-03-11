# Bioenergy in Energy balances

Getting few information on bioenergy from Eurostat's [Energy balances](https://ec.europa.eu/eurostat/web/energy/data/energy-balances) database:

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

Jupyter notebooks parsing xlsb files from a zip file [Energy Balances in the MS Excel file format (2020 edition)](https://ec.europa.eu/eurostat/documents/38154/4956218/Energy-Balances-April-2020-edition.zip/69da6e9f-bf8f-cd8e-f4ad-50b52f8ce616) and producing csv exports for some variables or tidy datasets to be used elsewhere.
