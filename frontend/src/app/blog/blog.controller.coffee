angular.module "angular"
.controller "BlogController", (Restangular, $location, $state) ->
  vm = this
  vm.categories = Restangular.all('blog_category').getList().$object
  vm.jumpToCategory = (slug) ->
    $state.go('blog.categories.posts', {'categorySlug': slug})
  return vm

