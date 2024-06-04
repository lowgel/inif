## FAQ
**Q: Why is this written in Python (e.g. I thought it was supposed to be fast!!!)?"**

A: inif uses Selenium for webscraping, which does not have bindings in any good languages, so Python is necessary. Don't worry, all the heavy lifting is offloaded to C binaries like most python programs.

**Q: will this work on Windows?**

A: Not sure, haven't tested. As long as the curl commands are the same and you have installed the right pip modules, probably.

**Q: What is a "booru"-style website?**

A: It is a type of image board website that uses a standardized tagging format and layout. The subject matter of these sites differs greatly (like cats, anime, robots, etc.) but the scraping method is largely the same, so scripts are highly reusable. You can read more about boorus [here](https://tvtropes.org/pmwiki/pmwiki.php/Main/ImageBooru)

FINAL NOTE: This repo/README is still a work in progress. Tutorial soon. 
