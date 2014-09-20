
import tornado.ioloop
import tornado.web

import handlers
import settings


app_config = dict(
    template_path=settings.TEMPLATE_PATH,
    static_path=settings.STATIC_PATH,
    autoescape="xhtml_escape",
    cookie_secret=u'vdibtFYzQeiKwetyVy3wS89cnum660sMv1VVS1LyDR0=',
    login_url="/",
    debug=True
    )

application = tornado.web.Application([
    #views
    ('/', handlers.IndexHandler),
    
    # Errors
    (r'.*', handlers.NotFoundHandler),
    
], **app_config
)


def run(port=8888):
    print("listening on port {}".format(port))
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()
