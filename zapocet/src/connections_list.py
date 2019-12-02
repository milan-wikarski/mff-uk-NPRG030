import json
import re
from connection_detail import ConnectionDetail


detailLinksRegex = re.compile("data-share-url=\"(.+?)\"")


class ConnectionsList:
  def __init__(self,  request_builder, f, t):
    self.request_builder = request_builder

    self.f = f
    self.t = t

    self.connections = []

  def fetchList(self):
    # Build and send request
    request = self.request_builder.create().setParam("from", self.f).setParam(
        "to", self.t).build().send()

    # Get detail links and create ConnectionDetail objects
    for link in re.findall(detailLinksRegex, request.html):
      self.connections.append(ConnectionDetail(link, self.f, self.t))

    return self

  def fetchDetails(self):
    # Fetch details of all connections
    for connection in self.connections:
      connection.fetch(self.request_builder)

    return self

  def toJSON(self):
    res = []

    for connection in self.connections:
      res.append(connection.toJSON())

    return res
    # return "[" + ",".join(res) + "]"
