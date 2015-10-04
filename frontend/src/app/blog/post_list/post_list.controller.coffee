angular.module "angular"
.controller "BlogPostListController", ($timeout, $state, $stateParams,
                                       Restangular) ->
  vm = this
  vm.posts = Restangular.one('blog_category',
    $stateParams['slug']).getList('posts').$object

  vm.jumpToPost = (slug) ->
    $state.go('blog.detail', {'slug': slug})

  return vm

