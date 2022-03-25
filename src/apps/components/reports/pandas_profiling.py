import datetime
import os
from pandas_profiling import ProfileReport
import dash_html_components as html
import dash_bootstrap_components as dbc


class Report:
    title: str = "Dataset Report for Fake Data"
    explorative: bool = True
    reports: list = []
    report_directory: str = "./data/reports"

    def __init__(self) -> None:
        pass

    def create_pandas_profiling_report(self, dataframe):

        date = datetime.datetime.now()
        profile = ProfileReport(
            dataframe,
            title=self.title,
            explorative=self.explorative

        )
        profile.to_file("./data/reports/{}.{}.{}_dataset_report.html".format(date.day, date.month, date.year))

    def display_list_of_reports(self):
        for report_name in os.listdir(self.report_directory):
            path = os.path.join(self.report_directory, report_name)
            if os.path.isfile(path) and report_name.endswith("html"):
                self.reports.append(report_name)
        return self.reports

    def getMissingValues(self, df):
        n_missing = df.isna().sum()

        return sum(n_missing)

    def generate_dataset_overview(self, df, max_rows=10):
        value = self.getMissingValues(df)
        missing_cell = value / 100
        results = {
            "Number of variables": len(df.columns),
            "Number of observations": len(df),
            "Missing cells": self.getMissingValues(df),
            "Missing cells (%)": missing_cell,

        }

        row_count = []
        for k, v in results.items():
            row_count.append(html.Tr([html.Td("{}".format(k)), html.Td("{}".format(v))]))

        render_table = dbc.Table([
            html.Tbody([
                x for x in row_count
            ])
        ], bordered=False, className="dataset_statistics_table")

        return render_table
