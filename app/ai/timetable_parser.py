import re


VALID_DAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
]


def parse_timetable(text: str):
    """
    Converts timetable text into structured data.

    Example Input:

    Monday
    P1 DSP
    P2 Maths

    Tuesday
    P1 Embedded Systems

    Output:

    [
        {
            "day":"Monday",
            "period":1,
            "subject":"DSP"
        },
        ...
    ]
    """

    entries = []

    current_day = None

    lines = text.splitlines()

    for line in lines:

        line = line.strip()

        if not line:
            continue

        # Detect day
        if line.title() in VALID_DAYS:
            current_day = line.title()
            continue

        # Detect period
        match = re.match(
            r"P\s*(\d+)\s+(.+)",
            line,
            re.IGNORECASE
        )

        if match and current_day:

            period = int(match.group(1))

            subject = match.group(2).strip()

            entries.append(
                {
                    "day": current_day,
                    "period": period,
                    "subject": subject
                }
            )

    return entries