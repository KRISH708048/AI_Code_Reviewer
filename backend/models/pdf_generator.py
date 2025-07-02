class PDFReportGenerator:
    def generate(self, report, path):
        with open(path, "w") as f:
            f.write(str(report))