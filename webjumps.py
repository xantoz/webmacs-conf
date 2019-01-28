from webmacs.commands.webjump import define_webjump, define_webjump_alias, WebJumpRequestCompleter
from PyQt5.QtCore import QUrl
import json

define_webjump_alias("ddg", "duckduckgo")

define_webjump("github", "http://github.com/search?q=%s&type=Everything")
define_webjump("gamefaqs", "http://www.gamefaqs.com/search?game=%s")
define_webjump("emacswiki",
               "https://startpage.com/do/search?cat=web&cmd=process_search&language=english&engine0=v1all&query=%s%20site%3Aemacswiki.org&abp=-1"# , $alternative="http://www.emacswiki.org/"
)
# define_webjump("emacswiki", "https://duckduckgo.com/?q=%s+site%3Aemacswiki.org")
define_webjump("orgmode-worg",
    "https://www.google.com/cse?cx=002987994228320350715%3Az4glpcrritm&q=%s&sa=Search&siteurl=orgmode.org%2Fworg"# , $alternative="http://orgmode.org/worg/"
) # Org-Mode Worg (~Wiki)
define_webjump("ratpoisonwiki", "http://ratpoison.wxcvbn.org/cgi-bin/wiki.pl?search=%s")
define_webjump("stumpwmwiki", "http://github.com/sabetts/stumpwm/search?q=%s")
define_webjump("cerise", "http://wiki.ceri.se/index.php?title=Special:Search&search=%s")
define_webjump("wa",     "http://www36.wolframalpha.com/input/?i=%s")
define_webjump("nyaa", "https://nyaa.si/?q=%s&f=0&c=0_0")
define_webjump("bakabt", "https://bakabt.me/browse.php?q=%s")
define_webjump("baka-updates", "http://www.baka-updates.com/search/search?searchitem=%s&submit.x=5&submit.y=15&submit=submit&searchradio=releases")
define_webjump("surugaya", "http://www.suruga-ya.jp/search?category=&search_word=%s")
define_webjump("yafuoku", "http://auctions.search.yahoo.co.jp/search?p=%s&aq=-1&oq=&x=0&y=0&ei=UTF-8&slider=0&tab_ex=commerce&auccat=")
define_webjump("amazon", "http://www.amazon.co.jp/s/ref=nb_sb_noss?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&url=search-alias%3Daps&field-keywords=%s")
define_webjump("sfx", "http://thejadednetwork.com/sfx/search/?keyword=%s&submitSearch=Search+SFX&x=")
define_webjump("mangasfx", "http://thejadednetwork.com/sfx/search/?keyword=%s&submitSearch=Search+SFX&x=")
define_webjump("jisho", "http://classic.jisho.org/words?jap=%s&eng=&dict=edict")
define_webjump("anidb", "http://anidb.net/perl-bin/animedb.pl?adb.search=%s&show=search&do.search=search")
define_webjump("gentoo-wiki", "http://www.gentoo-wiki.com/wiki/Special:Search?search=%s&go=Go")
define_webjump("youtube", "http://www.youtube.com/results?search_query=%s&search=Search")
define_webjump("youtube-user", "http://youtube.com/profile_videos?user=%s")
define_webjump("imdb", "http://imdb.com/find?q=%s")
# define_webjump("ebay", "http://www.ebay.com/sch/i.html?_odkw=derp&_osacat=0&_from=R40&_trksid=p2045573.m570.l1313.TR0.TRC0.H0.Xusb+sata+adapter.TRS0&_nkw=%s&_sacat=0")
define_webjump("ebay", "http://www.ebay.com/sch/i.html?_nkw=%s&_sacat=0")
define_webjump("ebayuk", "http://www.ebay.co.uk/sch/i.html?_from=R40&_sacat=0&_nkw=%s&_sop=15")
define_webjump("tradera", "http://www.tradera.com/search?sortBy=AddedOn&q=%s")
define_webjump("aliexpress", "https://www.aliexpress.com/wholesale?catId=0&initiative_id=SB_20170712071138&SearchText=%s")
define_webjump("webhallen", "https://www.webhallen.com/se/search?searchString=%s&sort=searchRating")
define_webjump("dustin", "https://www.dustin.se/sok/%s")
define_webjump("dustinhome", "https://www.dustinhome.se/sok/%s")

define_webjump("maps", "https://www.google.com/maps/search/%s/")
define_webjump("image", "https://www.google.com/images?q=%s");

def complete_wikipedia():
    return WebJumpRequestCompleter(
        lambda text: ("https://en.wikipedia.org/w/api.php?action=opensearch&search=" +
                      str(QUrl.toPercentEncoding(text), "utf-8")) if text else None,
        lambda response: json.loads(str(response, "utf-8"))[1]
    )

define_webjump("wikipedia", "https://en.wikipedia.org/wiki/Special:Search/?search=%s", complete_fn=complete_wikipedia)
