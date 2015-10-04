angular.module "angular"
  .config ($stateProvider, $urlRouterProvider) ->
    $stateProvider
      .state 'home',
        url: '/'
        templateUrl: "/app/main/main.html"
        controller: "MainController"
        controllerAs: "main"

      .state 'blog',
        url: '^/blog'
        templateUrl: "/app/blog/blog.html"
        controller: "BlogController"
        controllerAs: "blog"

      .state 'blog.category',
        url: "^/blog/categories/:categorySlug"
        templateUrl: "/app/blog/post_list/post_list.html"
        controller: "BlogPostListController"
        controllerAs: "postList"

      .state 'blog.post',
        url: "^/blog/post/:postSlug"
        templateUrl: "/app/blog/post/post.html"
        controller: "BlogPostController"
        controllerAs: "post"

    $urlRouterProvider.otherwise('/')



