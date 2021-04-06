yahoo = search.Yahoo()


def singlescan(url):
    """instance to scan single targeted domain"""

    if urlparse(url).query != '':
	@@ -67,7 +67,7 @@ def singleScan(url):
    return vulnerables


def initparser():
    """initialize parser arguments"""

    global parser
	@@ -80,7 +80,7 @@ def initParser():


if __name__ == "__main__":
    initparser()
    args = parser.parse_args()

    # find random SQLi by dork
	@@ -109,8 +109,14 @@ def initParser():
            exit(0)

        io.stdout("scanning server information")

        vulnerableurls = [result[0] for result in vulnerables]
        table_data = serverinfo.check(vulnerableurls)
        # add db name to info
        for result, info in zip(vulnerables, table_data):
            info.insert(1, result[1])  # database name

        io.fullprint(table_data)


    # do reverse domain of given site
	@@ -141,7 +147,7 @@ def initParser():

        vulnerables = []
        for domain in domains:
            vulnerables_temp = singlescan(domain)
            if vulnerables_temp:
                vulnerables += vulnerables_temp

	@@ -151,13 +157,18 @@ def initParser():
            exit(0)

        io.stdout("scanning server information")
        vulnerableurls = [result[0] for result in vulnerables]
        table_data = serverinfo.check(vulnerableurls)
        # add db name to info
        for result, info in zip(vulnerables, table_data):
            info.insert(1, result[1])  # database name

        io.fullprint(table_data)


    # scan SQLi of given site
    elif args.target:
        vulnerables = singlescan(args.target)

        if not vulnerables:
            exit(0)
	@@ -166,9 +177,9 @@ def initParser():
        io.stdout("getting server info of domains can take a few mins")
        table_data = serverinfo.check([args.target])

        io.printserverinfo(table_data)
        print ""  # give space between two table
        io.normalprint(vulnerables)


    # print help message, if no parameter is provided
