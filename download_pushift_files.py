import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--type", dest="t", action="store", required=True)

save_folder = "./data_in/2020/"
start_year = 2020
end_year = 2021


def trigger_wget(file_type, url, year, month, ext):
    url = url.format(year, month, ext)
    output_file = f"{file_type}_{year}-{month}.{ext}"
    if os.path.exists(output_file):
        print("Skipping", url, "because", output_file, "exists")

    os.system(f"wget -O {save_folder}{output_file} {url}")


def submissions():
    def get_ext(year: int, month: int):
        if year <= 2010:
            return "xz"
        if year <= 2014:
            return "bz2"
        if year <= 2016:
            return "zst"
        if year == 2017:
            if month in [7, 11, 12]:
                return "xz"
            else:
                return "bz2"
        if year == 2018:
            if month < 11:
                return "xz"
            else:
                return "zst"
        return "zst"

    url_v1 = "https://files.pushshift.io/reddit/submissions/RS_{0}-{1}.{2}"
    url_v2 = "https://files.pushshift.io/reddit/submissions/RS_v2_{0}-{1}.{2}"
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            url = url_v2 if year <= 2010 else url_v1
            ext = get_ext(year, month)
            month = str(month) if month >= 10 else "0" + str(month)
            print("Downloading {0} - {1} - {2}".format(year, month, ext))
            trigger_wget("RS", url, year, month, ext)


def comments():
    def get_ext(year: int, month: int):
        if year <= 2016:
            return "bz2"
        if year == 2017:
            return "bz2" if month <= 11 else "xz"
        if year == 2018:
            return "xz" if month <= 9 else "zst"
        return "zst"

    url = "https://files.pushshift.io/reddit/comments/RC_{0}-{1}.{2}"
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            ext = get_ext(year, month)
            month = str(month) if month >= 10 else "0" + str(month)
            print("Downloading {0} - {1} - {2}".format(year, month, ext))
            trigger_wget("RC", url, year, month, ext)


def start():
    args = parser.parse_args()
    if args.t == "S":
        submissions()
    elif args.t == "C":
        comments()
    else:
        print("ERROR", args.t)


start()
