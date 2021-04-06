import html


def init():
    signal.signal(signal.SIGINT, signal.SIG_IGN)

def scan(urls):
	@@ -19,12 +19,12 @@ def scan(urls):

    childs = []  # store child processes
    max_processes = multiprocessing.cpu_count() * 2
    pool = multiprocessing.Pool(max_processes, init)

    for url in urls:
        def callback(result, url=url):
            results[url] = result
        childs.append(pool.apply_async(__sqli, (url, ), callback=callback))

    try:
        while True:
	@@ -40,13 +40,13 @@ def callback(result, url=url):
        pool.join()

    for url, result in results.items():
        if result[0] == True:
            vulnerables.append((url, result[1]))

    return vulnerables


def __sqli(url):
    """check SQL injection vulnerability"""

    io.stdout("scanning {}".format(url), end="")
	@@ -59,10 +59,12 @@ def __checkSQLi(url):
        return False

    website = domain + "?" + ("&".join([param + "'" for param in queries]))
    source = html.getHTML(website)
    if source:
        vulnerable, db = sqlerrors.check(source)
        if vulnerable and db != None:
            io.showsign(" vulnerable")
            return True, db

    print ""  # move cursor to new line
    return False, None
