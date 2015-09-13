angular.module "angular"
  .config ($routeProvider) ->
    $routeProvider
      .when('/',
        templateUrl: "/app/main/main.html"
        controller: "MainController"
        controllerAs: "main"
      )
      .when('/blog',
        templateUrl: "/app/blog/blog.html"
        controller: "BlogController"
        controllerAs: "blog"
      )
      .when("/blog/categories/:categorySlug",
        templateUrl: "/app/blog/post_list/post_list.html"
        controller: "BlogPostListController"
        controllerAs: "postList"
      )
      .when("/blog/post/:postSlug",
        templateUrl: "/app/blog/post/post.html"
        controller: "BlogPostController"
        controllerAs: "post"
      )
      .otherwise(redirectTo: '/')
