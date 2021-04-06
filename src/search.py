import sys

from lib import bing
from lib import google
from lib import yahoo
from urllib2 import HTTPError, URLError

bingsearch = bing.Bing()
	@@ -29,8 +29,8 @@ def search(self, query, pages=10):
            exit("[504] Gateway Timeout")
        except:
            exit("Unknown error occurred")
        else:
            return urls

class Bing(Search):
    def search(self, query, pages=10):
	
