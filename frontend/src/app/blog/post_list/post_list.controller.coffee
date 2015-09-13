angular.module "angular"
.controller "BlogPostListController", ($timeout, $routeParams, Restangular) ->
  vm = this
  vm.posts = Restangular.one('blog_category',
    $routeParams['categorySlug']).getList('posts').$object
  return vm

