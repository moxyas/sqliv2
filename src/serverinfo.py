import html


def init():
    signal.signal(signal.SIGINT, signal.SIG_IGN)

def check(urls):
	@@ -21,12 +21,12 @@ def check(urls):

    childs = []  # store child processes
    max_processes = multiprocessing.cpu_count() * 2
    pool = multiprocessing.Pool(max_processes, init)

    for url in urls:
        def callback(result, url=url):
            results[url] = result
        childs.append(pool.apply_async(__getserverinfo, (url, ), callback=callback))

    try:
        while True:
	@@ -49,12 +49,12 @@ def callback(result, url=url):
            domains_info.append([url, data[0], data[1]])
            continue

        domains_info.append([url, '', ''])

    return domains_info


def __getserverinfo(url):
    """get server name and version of given domain"""

    url = urlparse(url).netloc if urlparse(url).netloc != '' else urlparse(url).path.split("/")[0]
