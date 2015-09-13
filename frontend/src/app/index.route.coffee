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
      .state "blogPosts",
        url: "/blog/posts"
        templateUrl: "app/blog/post_list/post_list.html"
        controller: "BlogPostListController"
        controllerAs: "postList"
      .state "blogPost",
        url: "/blog/post"
        templateUrl: "app/blog/post/post_list.html"
        controller: "BlogPostController"
        controllerAs: "post"

    $urlRouterProvider.otherwise '/'
