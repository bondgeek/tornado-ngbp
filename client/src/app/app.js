(function(app) {

    app.config(function ($stateProvider, $urlRouterProvider) {
        $urlRouterProvider.otherwise('/home');
    });

    app.run(function () {});

    app.controller('AppController', function ($scope) {

    });

}(angular.module("tornado-ngbp", [
    'tornado-ngbp.home',
    'tornado-ngbp.about',
    'templates-app',
    'templates-common',
    'ui.router.state',
    'ui.router',
])));
