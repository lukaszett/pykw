import argparse
import sys
from datetime import date, datetime, timedelta


def get_kw_from_date(dt: date) -> int:
    _, week, _ = dt.isocalendar()
    return week


def main():
    parser = argparse.ArgumentParser(
        prog="kw",
        description="A simple tool to get the number of the current calendar week according to ISO8601.",
        usage="kw [-h] [-i N] [-f FORMAT] [-r KW] [date]",
    )

    parser.add_argument("date", default=date.today(), nargs="?")
    parser.add_argument(
        "-i",
        "--in",
        type=int,
        help="Don't get current KW, but KW in N weeks.",
        dest="delta",
        default=0,
        metavar="N",
    )
    parser.add_argument(
        "-f",
        "--format",
        type=str,
        help="Format to parse date.",
        default="%Y-%m-%d",
        metavar="FORMAT",
    )
    parser.add_argument(
        "-r",
        "--reverse",
        type=int,
        help="Get start and end date for given KW. Ignores all other args.",
        metavar="KW",
    )

    args = parser.parse_args()

    if args.reverse is not None:
        current_year = args.date.replace(month=1, day=1)
        date_in_target_week = current_year + timedelta(weeks=args.reverse)

        start_day = date_in_target_week - timedelta(days=date_in_target_week.weekday())
        end_day = start_day + timedelta(days=6)

        print(f"{start_day.strftime(args.format)}\n{end_day.strftime(args.format)}")
        return

    if isinstance(args.date, str):
        try:
            args.date = datetime.strptime(args.date, args.format).date()
        except ValueError:
            sys.exit("Please provide a valid date.")

    target_date = args.date + timedelta(weeks=args.delta)
    week = get_kw_from_date(target_date)

    print(week)


if __name__ == "__main__":
    main()
