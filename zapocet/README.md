# PID Scrapper

## Installation

This project requires certain Python packages to function properly. To install them, run:

```console
$ pip install requests bs4 python-telegram-bot python-dotenv
```

## Running

To start the app, run the following command from project root directory:

```console
[user@device zapocet]$ python src/index.py
```

After that the bot will run in terminal until termination.

## File structure

```console
.
├── README.md
└── src
    ├── class_connection_detail.py
    ├── class_connections_list.py
    ├── class_day_time.py
    ├── class_route.py
    ├── class_search_query.py
    ├── class_time_location.py
    ├── cmd_help.py
    ├── cmd_inline.py
    ├── cmd_next.py
    ├── cmd_routes.py
    ├── cmd_search_params.py
    ├── cmd_search.py
    ├── cmd_start.py
    ├── index.py
    ├── module_request_builder.py
    ├── module_routes_manager.py
    ├── module_state.py
    ├── module_stops_manager.py
    └── data
        ├── points.json
        ├── routes.json
        ├── _sources.json
        └── stops.json
```

All python files are located in `/src` directory. `index.py` is the core file. All other `.py` files belong to one of three different categories:

- **Class** (`class_<class_name>.py`) - Contain some class definition.
- **Module** (`module_<module_name>.py`) - Contain a module. Module is an object of some class. There can only be on instance of this class per app and therefore it is created in the file itself and then can be imported and used in other files.
- **Command** (`cmd_<command_name>.py`) - Contains a command definition, which is a function with two parameters: `update` and `context` (see python-telegram-bot docs).

Data the app uses is stored in `src/data`. There are three core JSON files which contain data about:

- **Routes** (`routes.json`) - Data about public transport routes (eg. Tram 1: Sídliště Petřiny - Spojovací)

- **Stops** (`stops.json`) - Data about stops. The app only uses the names to check them against user input

- **Points** (`points.json`) - Data about location of stops. Not really used in app, but it is present just in case.

These JSON files are downloaded from `https://pid.cz/<endpoint>.json`, as can be seen in `_source.json`

## User interface

User interface of the app is provided by Telegram App. This bot only receives command (user messages) and responds to them accordingly.

Although it is possible to implement more advanced ways to interact with the app, this app only implements commands in form `/<command>`. The command it implements are:

- **`/start`** - Starts the communication with the bot
- **`/help`** - Display list of commands
- **`/routes`** - Display list of routes
- **`/search`** - Start a connection search dialog

### Routes

Furthermore command **`/routes`** only displays a list of more specific commands that user can use to display routes of particular mean of transport:

- **`/routes_tram`** for tram routes,
- **`/routes_bus`** for bus routes,
- **`/routes_metro`** for metro routes,
- **`/routes_train`** for train routes.

Since there are many routes, pagination has been implemented to ensure that the list of routes is not too long. The limit of the number of routes has been set to 10. Optional parameter page can be specified when calling command: **`/routes_<mean> <page>`**. For example, command **`/routes_bus 8`** will display routes 71-80 from a list of bus routes ordered by their numbers (IDs). The default value of `<page>` is 1 (first page).

### Search

Command **`/search`** is used to initiate search dialog. After that, the user will be asked to first provide the departure stop. User input will lead to one of two outcomes:

1. Either the stop exists and the dialog continues

or

2. The stop does not exist and user is asked to provide the departure stop again

After providing a correct (existing) departure stop, the user is asked to provide the arrival stop. The same error handling is implemented here, as is in departure stop input.
