import pandas
import plotly.express as px

# Importing DB
table1 = pandas.read_csv("Python/Automation - Data handling and graphic/telecom_users.csv")

# Removing an useless columns & rows
table2 = table1.drop("Unnamed: 0", axis=1)
table2 = table2.dropna(how="all", axis=1)
table2 = table2.dropna(how="any", axis=0, subset="Churn")

# Correcting the database
table2.loc[table2["Aposentado"] == 0, "Aposentado"] = "Não"
table2.loc[table2["Aposentado"] == 1, "Aposentado"] = "Sim"

# Convert data types & coerce errors to null(NaN)
table2['TotalGasto'] = pandas.to_numeric(table2['TotalGasto'], errors='coerce')

# Total canceled clients
print(table2['Churn'].value_counts(normalize=True).map("{:.1%}".format))

# Create and display a graphic
graphic1 = px.histogram(table2, x="MesesComoCliente", color="Churn")
graphic1.show()

# Create and display a graphic for each column
for i in table2.columns:
    graphic1 = px.histogram(table2, x=i, color="Churn")
    graphic1.show()
