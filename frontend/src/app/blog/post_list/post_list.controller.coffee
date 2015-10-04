angular.module "angular"
.controller "BlogPostListController", ($timeout, $routeParams, $location,
                                       Restangular) ->
  vm = this
  vm.posts = Restangular.one('blog_category',
    $routeParams['categorySlug']).getList('posts').$object

  vm.jumpToPost = (slug) ->
    $location.path('/blog/post/' + slug)

  return vm

