__author__ = 'bondgeek'

import json
import tornado

from jinja2 import Environment, PackageLoader

import webserver.cookie as cookie

import settings


class BaseHandler(tornado.web.RequestHandler):
    template_name = 'base.html'
    login_href = '/'
    error_template = 'error.html'

    env = Environment(loader=PackageLoader('shared', 'templates'))

    def get_current_user(self):
        return self.cookie.get(settings.COOKIE_USER_ID_NAME, None)

    def initialize(self):
        self.env.globals['static_url'] = self.static_url
        self.template = self.env.get_template(self.template_name)
        self.error_template = self.env.get_template(self.error_template)

    def prepare(self):
        self.cookie = cookie.from_json(self.get_secure_cookie(settings.COOKIE_NAME))
        self.user_id = self.current_user
        self.global_env = settings.TEMPLATE_GLOBAL_ENV

    def update_cookie(self):
        self.set_secure_cookie(settings.COOKIE_NAME, self.cookie.as_json(), expires_days=settings.COOKIE_EXPIRE_DAYS)

    def show_error(self, message):
        self.write(self.error_template.render(message=message, global_env=settings.TEMPLATE_GLOBAL_ENV))

    def write_template(self, *args, **kwgs):
        self.write(self.template.render(*args, global_env=settings.TEMPLATE_GLOBAL_ENV, **kwgs))


class IndexHandler(BaseCustomerHandler):
    template_name = 'index.html'

    def initialize(self):
        super(IndexHandler, self).initialize()

    def get(self):
        if self.current_user:
            self.set_all_cookie_values(self.current_user)
            self.redirect('/shop')
            return
        self.clear_all_cookies()

        self.write_template()


class NotFoundHandler(BaseHandler):

    def get_error_html(self, status_code, **kwargs):
        self.template = self.env.get_template(self.template_name)
        self.write_template()

    def prepare(self):
        self.env.globals['static_url'] = self.static_url
        self.template_name = '404.html'
        raise tornado.web.HTTPError(self._status_code)
