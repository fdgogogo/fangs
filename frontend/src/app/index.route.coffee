angular.module "angular"
  .config ($stateProvider, $urlRouterProvider) ->
    $stateProvider
      .state 'home',
        url: '/'
        templateUrl: "/app/main/main.html"
        controller: "MainController"
        controllerAs: "main"

      .state 'blog',
        url: '/blog'
        templateUrl: "/app/blog/blog.html"
        controller: "BlogController"
        controllerAs: "blog"

      .state 'blog.category',
        url: "^/categories/{slug}"
        templateUrl: "/app/blog/post_list/post_list.html"
        controller: "BlogPostListController as postList"

      .state 'blog.post',
        url: "/post/:slug"
        templateUrl: "/app/blog/post/post.html"
        controller: "BlogPostController as post"

    $urlRouterProvider.otherwise('/')



