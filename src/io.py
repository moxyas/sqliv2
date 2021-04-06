 return option

def stdout(message, end="\n"):
    """print a message for user in console"""

    symbol = colored("[MSG]", "yellow")
    currentime = colored("[{}]".format(time.strftime("%H:%M:%S")), "green")
    print("{} {} {}".format(symbol, currentime, message), end=end)

def stderr(message, end="\n"):
    """print an error for user in console"""

    symbol = colored("[ERR]", "red")
    currentime = colored("[{}]".format(time.strftime("%H:%M:%S")), "green")
    print("{} {} {}".format(symbol, currentime, message), end=end)

def showsign(message):
    """show vulnerable message"""

    print(colored(message, "magenta"))

def dump(array, filename):
    """save the given array into a file"""

    with open(filename, 'w') as output:
        for data in array:
            output.write(data + "\n")

def printserverinfo(data):
    """show vulnerable websites in table"""

    # [
    #   ["website", "server", "lang"],
    #   [sql.com", "apache", "php/5.5xxxx"]
    # ]

	@@ -74,13 +68,12 @@ def printServerInfo(data):
        return

    title = " DOMAINS "
    table_data = [["website", "server", "lang"]] + data

    table = SingleTable(table_data, title)
    print(table.table)

def normalprint(data):
    """show vulnerable websites in table"""

    # [
	@@ -91,26 +84,25 @@ def printVulnerables(data):
    title = " VULNERABLE URLS "
    table_data = [["index", "url"]]
    # add into table_data by one by one
    for index, url in enumerate(data):
        table_data.append([index+1, url])

    table = SingleTable(table_data, title)
    print(table.table)

def fullprint(data):
    """show vulnerable websites in table with server info"""

    # [
    #   ["index", "url", "db", server", "lang"],
    #   ["1", "sql.com", "mysql", apache", "php/5.5xxx"]
    # ]

    title = " VULNERABLE URLS "
    table_data = [["index", "url", "db", "server", "lang"]]
    # add into table_data by one by one
    for index, each in enumerate(data):
        table_data.append([index+1, each[0], each[1], each[2][0:30], each[3][0:30]])

    table = SingleTable(table_data, title)
    print(table.table)
