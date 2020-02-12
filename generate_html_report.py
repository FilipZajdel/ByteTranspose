from yattag import Doc
import os
import json

doc, tag, text = Doc().tagtext()

raport = {"functions": {
    "function1": {"PC_linux": 0.234, "PC_Win": 0.5, "RPi_Linux": 0.4},
    "function2": {"PC_linux": 0.112, "PC_Win": 0.5, "RPi_Linux": 0.4},
    "function3": {"PC_linux": 0.119, "PC_Win": 0.5, "RPi_Linux": 0.4}
}
}


def load_json_reports(directory):
    files = [d for d in os.listdir(directory) if ".json" in d]
    merged_report = {}

    for report in files:
        with open(f"{directory}/{report}", "r") as fp:
            merged_report[report] = json.load(fp)

    return merged_report


def get_function_names(reports):
    names = []

    for report in reports.values():
        for func_name in report.get("functions"):
            if func_name not in names:
                names.append(func_name)

    return names


def expsec_to_sec_postfix(val, precision=3):
    if val > 1:
        return f"{round(val, precision)}s"
    elif val > 10**(-3):
        return f"{round(val/(10**(-3)), precision)}ms"
    elif val > 10**(-6):
        return f"{round(val/(10**(-6)), precision)}µs"
    elif val >> 10**(-9):
        return f"{round(val/(10**(-9)), precision)}µs"

with tag("head"):
    doc.stag("link", rel="icon", href="static/img/logo.ico")
    doc.stag("meta", charset="UTF-8")
    doc.asis(
        "<style>table,th,td{border:1px solid magenta; border-collapse: collapse}</style>")

with tag("body", style="background: url(\"static/img/prism.png\") fixed"):
    with tag("title"):
        text("Byte Transpose Performance Tests")

    with tag("div", style="margin: auto; width: 75%; background-color: white; opacity: 0.5"):
        with tag("table", style="width: 100%"):
            reports = load_json_reports("Results")
            func_names = get_function_names(reports)
            columns = ["", *func_names]

            with tag("tr", style="font-size: 150%"):
                for column_name in columns:
                    with tag("th"):
                        text(column_name)

            for report in reports.values():
                with tag("tr", style="text-align:center; font-size: 130%"):
                    with tag("td"):
                        text(report.get("platform", "platform?"))
                        doc.stag("br")
                        text(report.get("cpu", ""))
                    for func_name in func_names:
                        with tag("td"):
                            if func_name in report.get("functions"):
                                time = report.get("functions").get(
                                    func_name, "-").get("avg_time")
                                time = expsec_to_sec_postfix(time)
                                text(f"{time}")
                            else:
                                text("-")

with open("docs/index.html", "w") as html_file:
    html_file.write(doc.getvalue())