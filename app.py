from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

def dayfinder(num):
    if 1 <= num <= 28:
        month = "Boozer"
        start_day = 1
    elif 29 <= num <= 56:
        month = "Chipper"
        start_day = 29
    elif 57 <= num <= 84:
        month = "Kucheeder"
        start_day = 57
    elif 85 <= num <= 112:
        month = "Warder"
        start_day = 85
    elif 113 <= num <= 140:
        month = "Forgorder"
        start_day = 113
    elif 141 <= num <= 168:
        month = "Crabber"
        start_day = 141
    elif 169 <= num <= 196:
        month = "Monker"
        start_day = 169
    elif 197 <= num <= 224:
        month = "Mechanicer"
        start_day = 197
    elif 225 <= num <= 252:
        month = "Ferrer"
        start_day = 225
    elif 253 <= num <= 280:
        month = "Penner"
        start_day = 253
    elif 281 <= num <= 308:
        month = "Juler"
        start_day = 281
    elif 309 <= num <= 336:
        month = "Slother"
        start_day = 309
    else:
        month = "Skiver"
        start_day = 337

    day_of_month = num - start_day + 1
    last_digit = num % 10
    day_of_week = {
        1: "Murday",
        2: "Duoday",
        3: "Tresday",
        4: "Issiday",
        5: "Wensday",
        6: "Sexday",
        7: "Curryday",
        8: "Friday",
        9: "Saturday",
        0: "Verday"
    }.get(last_digit, "unknown")
    return month, day_of_month, day_of_week

@app.route("/")
def show_date():
    day_of_year = datetime.utcnow().date().timetuple().tm_yday-1
    month, day_of_month, day_of_week = dayfinder(day_of_year)

    # Determine the ordinal suffix for the day
    if 11 <= day_of_month <= 13:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(day_of_month % 10, "th")

    output_text = f"Today is {day_of_week}, the {day_of_month}{suffix} of {month}!"

    # HTML content with added CSS for centering and enlarging the text
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=2.0">
        <title>What day is today?</title>
        <style>
            body {{
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #9066a5;
                font-family: Arial, sans-serif;
            }}
            h1 {{
                font-size: 5em; /* Adjusts the font size */
                color: #ffffff;
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <h1>{output_text}</h1>
    </body>
    </html>
    """
    return render_template_string(html_content)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

