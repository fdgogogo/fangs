angular.module "angular"
  .config ($stateProvider, $urlRouterProvider) ->
    $stateProvider
      .state "home",
        url: "/"
        templateUrl: "app/main/main.html"
        controller: "MainController"
        controllerAs: "main"
      .state "blog",
        url: "/blog"
        templateUrl: "app/blog/blog.html"
        controller: "BlogController"
        controllerAs: "blog"

    $urlRouterProvider.otherwise '/'
