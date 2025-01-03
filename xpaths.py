# xpaths.py

from lxml.etree import XPath

# Define XPath expressions for cleaning
CLEAN_XPATHS = [
    XPath(".//header"),
    XPath(".//footer"),
    XPath(".//nav"),
    XPath(".//aside"),
    XPath(".//form"),
    XPath(".//iframe"),
    XPath(".//script"),
    XPath(".//style"),
    XPath(".//*[contains(@class, 'advertisement')]"),
    XPath(".//*[contains(@class, 'sidebar')]"),
    # Additions from AUTHOR_DISCARD_XPATHS
    XPath(
        """.//*[self::a or self::div or self::section or self::span][@id='comments' or @class='comments' or @class='title' or @class='date' or
    contains(@id, 'commentlist') or contains(@class, 'commentlist') or contains(@class, 'sidebar') or contains(@class, 'is-hidden') or contains(@class, 'quote')
    or contains(@id, 'comment-list') or contains(@class, 'comments-list') or contains(@class, 'embedly-instagram') or contains(@id, 'ProductReviews') or
    starts-with(@id, 'comments') or contains(@data-component, "Figure") or contains(@class, "article-share") or contains(@class, "article-support") or contains(@class, "print") or contains(@class, "category") or contains(@class, "meta-date") or contains(@class, "meta-reviewer")
    or starts-with(@class, 'comments') or starts-with(@class, 'Comments')
    ]"""
    ),
    XPath("//time|//figure"),
    # Additions from COMMENTS_DISCARD_XPATH
    XPath('.//*[self::div or self::section][starts-with(@id, "respond")]'),
    XPath(".//cite|.//quote"),
    XPath(
        """.//*[@class="comments-title" or contains(@class, "comments-title") or
    contains(@class, "nocomments") or starts-with(@id|@class, "reply-") or
    contains(@class, "-reply-") or contains(@class, "message")
    or contains(@class, "signin") or
    contains(@id|@class, "akismet") or contains(@style, "display:none")]"""
    ),
    # Additions from REMOVE_COMMENTS_XPATH
    XPath(
        """.//*[self::div or self::list or self::section][
    starts-with(translate(@id, "C","c"), 'comment') or
    starts-with(translate(@class, "C","c"), 'comment') or
    contains(@class, 'article-comments') or contains(@class, 'post-comments')
    or starts-with(@id, 'comol') or starts-with(@id, 'disqus_thread')
    or starts-with(@id, 'dsq-comments')
    ]"""
    ),
    # Additions from OVERALL_DISCARD_XPATH
    XPath(
        """ .//*[self::div or self::item or self::list
            or self::p or self::section or self::span][
    contains(translate(@id, "F","f"), "footer") or contains(translate(@class, "F","f"), "footer")
    or contains(@id, "related") or contains(@class, "elated") or
    contains(@id|@class, "viral") or
    starts-with(@id|@class, "shar") or
    contains(@class, "share-") or
    contains(translate(@id, "S", "s"), "share") or
    contains(@id|@class, "social") or contains(@class, "sociable") or
    contains(@id|@class, "syndication") or
    starts-with(@id, "jp-") or starts-with(@id, "dpsp-content") or
    contains(@class, "embedded") or contains(@class, "embed") or
    contains(@id|@class, "newsletter") or
    contains(@class, "subnav") or
    contains(@id|@class, "cookie") or
    contains(@id|@class, "tags") or contains(@class, "tag-list") or
    contains(@id|@class, "sidebar") or
    contains(@id|@class, "banner") or contains(@class, "bar") or
    contains(@class, "meta") or contains(@id, "menu") or contains(@class, "menu") or
    contains(translate(@id, "N", "n"), "nav") or contains(translate(@role, "N", "n"), "nav")
    or starts-with(@class, "nav") or contains(@class, "avigation") or
    contains(@class, "navbar") or contains(@class, "navbox") or starts-with(@class, "post-nav")
    or contains(@id|@class, "breadcrumb") or
    contains(@id|@class, "bread-crumb") or
    contains(@id|@class, "author") or
    contains(@id|@class, "button")
    or contains(translate(@class, "B", "b"), "byline")
    or contains(@class, "rating") or contains(@class, "widget") or
    contains(@class, "attachment") or contains(@class, "timestamp") or
    contains(@class, "user-info") or contains(@class, "user-profile") or
    contains(@class, "-ad-") or contains(@class, "-icon")
    or contains(@class, "article-infos") or
    contains(@class, "nfoline")
    or contains(@data-component, "MostPopularStories")
    or contains(@class, "outbrain") or contains(@class, "taboola")
    or contains(@class, "criteo") or contains(@class, "options") or contains(@class, "expand")
    or contains(@class, "consent") or contains(@class, "modal-content")
    or contains(@class, " ad ") or contains(@class, "permission")
    or contains(@class, "next-") or contains(@class, "-stories")
    or contains(@class, "most-popular") or contains(@class, "mol-factbox")
    or starts-with(@class, "ZendeskForm") or contains(@id|@class, "message-container")
    or contains(@class, "yin") or contains(@class, "zlylin")
    or contains(@class, "xg1") or contains(@id, "bmdh")
    or contains(@class, "slide") or contains(@class, "viewport")
    or @data-lp-replacement-content
    or contains(@id, "premium") or contains(@class, "overlay")
    or contains(@class, "paid-content") or contains(@class, "paidcontent")
    or contains(@class, "obfuscated") or contains(@class, "blurred")]"""
    ),
]
