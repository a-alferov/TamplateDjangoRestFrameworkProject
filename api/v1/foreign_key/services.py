from datetime import date

from api.models import Reporter, Article


def article_create(
        reporter: Reporter,
        headline: str,
        pub_date: date,
) -> Article:
    """
    Creating article for reporter

    :param reporter: Reporter
    :type reporter: Reporter
    :param headline: Headline article
    :type headline: str
    :param pub_date: Publication date
    :type pub_date: date
    :return: Article
    :rtype: Article
    """
    article = reporter.article_set.create(reporter=reporter, headline=headline, pub_date=pub_date)
    return article
