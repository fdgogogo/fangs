angular.module "angular"
  .config ($stateProvider, $urlRouterProvider) ->
    $stateProvider
      .state 'home',
        url: '/'
        templateUrl: "/app/main/main.html"
        controller: "MainController"
        controllerAs: "main"
        ncyBreadcrumb: {
          label: 'Home'
        }

      .state 'blog',
        url: '/blog'
        templateUrl: "/app/blog/blog.html"
        controller: "BlogController"
        controllerAs: "blog"
        ncyBreadcrumb: {
          label: 'Blog'
        }
      .state 'blog.categories',
        url: '/categories'
        templateUrl: "/app/blog/categories/categories.html"
        controller: "BlogCategoryController as blogCategory"
        ncyBreadcrumb: {
          label: 'Categories'
        }
      .state 'blog.categories.posts',
        url: "/{categorySlug}"
        templateUrl: "/app/blog/post_list/post_list.html"
        controller: "BlogPostListController as postList"
        ncyBreadcrumb: {
          label: 'Posts'
        }

      .state 'blog.categories.posts.detail',
        url: "/{postSlug}"
        templateUrl: "/app/blog/post_list/post/post.html"
        controller: "BlogPostController as post"
        ncyBreadcrumb: {
          label: 'Detail'
        }

    $urlRouterProvider.otherwise('/')



