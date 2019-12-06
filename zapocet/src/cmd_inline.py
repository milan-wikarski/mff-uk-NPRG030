from telegram import InlineQueryResultArticle, InputTextMessageContent
from module_state import state
from module_stops_manager import stops_manager


def cmd_inline(update, context):
  user = update.inline_query.id
  query = update.inline_query.query

  print(query)

  results = []

  if not query:
    print("No query")
    return

  if (query[0] == "/"):
    results.append(
        InlineQueryResultArticle(
            id="help",
            title="/help",
            input_message_content=InputTextMessageContent("/help")
        )
    )

  # At least one param from "to" and "from" is not set
  elif (user in state.search and (state.search[user].f is None or state.search[user].t is None)):
    to_search = query.lower()

    for stop in stops_manager.stops:
      if (to_search in stop.lower()):
        results.append(InlineQueryResultArticle(
            id=stop, title=stop, input_message_content=InputTextMessageContent(stop)))

    pass

  return context.bot.answer_inline_query(user, results)
