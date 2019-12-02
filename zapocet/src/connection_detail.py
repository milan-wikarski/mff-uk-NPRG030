import json
import re


dateRegex = re.compile(
    "<h2 class=\"reset date\">(\d{1,2}:\d{1,2})<span class=\"date-after\">(.+?)</span>"
)
partsNameRegex = re.compile("(Tram \d+|Metro [ABC]|Bus \d+)")
partsTimeRegex = re.compile("<p class=\"reset time\">(\d{1,2}:\d{1,2})</p>")
partsLocationRegex = re.compile("<strong class=\"name\">(.+?)</strong>")


class ConnectionDetail:
  def __init__(self, link, f, t):
    self.link = link
    self.f = f
    self.t = t

  def fetch(self, request_builder):
    # Build and send request
    request = request_builder.create(self.link).build().send()

    # Parse date and time
    datetime = list(reversed(list(re.findall(dateRegex, request.html)[0])))
    self.date = datetime[0]
    self.time = datetime[1]

    # Parse parts
    self.parts = []

    parts_names = re.findall(partsNameRegex, request.html)
    parts_times = re.findall(partsTimeRegex, request.html)
    parts_locations = re.findall(partsLocationRegex, request.html)

    for i in range(len(parts_names)):
      self.parts.append({
          "link": parts_names[i],
          "departure": {
              "time": parts_times[i * 2],
              "location": parts_locations[i * 2]
          },
          "arrival": {
              "time": parts_times[i * 2 + 1],
              "location": parts_locations[i * 2 + 1]
          }
      })

  def toJSON(self):
    return {
        "from": self.f,
        "to": self.t,
        "detail": self.link,
        "date": self.date,
        "time": self.time,
        "parts": self.parts
    }
