angular.module "angular"
.controller "BlogPostListController", ($timeout, $state, $stateParams,
                                       Restangular) ->
  vm = this
  vm.posts = Restangular.one('blog_category',
    $stateParams['categorySlug']).getList('posts').$object

  vm.jumpToPost = (slug) ->
    $state.go('blog.categories.posts.detail', {'postSlug': slug})

  return vm

