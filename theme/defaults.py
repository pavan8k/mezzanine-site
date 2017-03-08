from mezzanine.conf import register_setting
register_setting(
    name="TEMPLATE_ACCESSIBLE_SETTINGS",
    description=("Sequence of setting names available within templates."),
    editable=False,
    default=("SOCIAL_LINK_FACEBOOK", "SOCIAL_LINK_TWITTER","SOCIAL_LINK_INSTA","TWITTER_EMBEDD","INSTA_EMBEDD","FACEBOOK_EMBEDD"),
    append=True,
)
register_setting(
    name="SOCIAL_LINK_FACEBOOK",
    label=("Facebook link"),
    description=("If present a Facebook icon linking here will be in the "
        "header."),
    editable=True,
    default="https://facebook.com/pavan39",
)
register_setting(
    name="SOCIAL_LINK_TWITTER",
    label=("Twitter link"),
    description=("If present a Twitter icon linking here will be in the "
        "header."),
    editable=True,
    default="https://twitter.com/elonmusk",
)
register_setting(
    name="SOCIAL_LINK_INSTA",
    label=("Insta link"),
    description=("If present a Insta icon linking here will be in the "
        "header."),
    editable=True,
    default="https://www.instagram.com/zomatoin/",
)
register_setting(
    name="TWITTER_EMBEDD",
    label=("Twitter Embedd"),
    description=("Link to embedd what admin wants from twitter in the site"),
    editable=True,
    default="",
						)
register_setting(
    name="INSTA_EMBEDD",
    label=("Insta Embedd"),
    description=("Link to embedd what admin wants from Insta in the site"),
    editable=True,
    default="",
    )
register_setting(
    name="FACEBOOK_EMBEDD",
    label=("Facebook Embedd"),
    description=("Link to embedd what admin wants from Facebook in the site"),
    editable=True,
    default="",
)